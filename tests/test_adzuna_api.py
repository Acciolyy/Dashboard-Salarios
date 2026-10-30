import unittest
from unittest import mock

import requests

import adzuna_api
from adzuna_api import AdzunaAPIError, buscar_historico_salarial, consultar_historico_salarial


def resposta(status=200, json_data=None, json_erro=False):
    r = mock.Mock(status_code=status, text="corpo")
    if status >= 400:
        r.raise_for_status.side_effect = requests.exceptions.HTTPError(response=r)
    else:
        r.raise_for_status.return_value = None
    if json_erro:
        r.json.side_effect = ValueError("json inválido")
    else:
        r.json.return_value = json_data
    return r


class BuscarHistoricoSalarialTest(unittest.TestCase):
    def setUp(self):
        buscar_historico_salarial.clear()
        patcher = mock.patch.multiple(adzuna_api, ADZUNA_APP_ID="id", ADZUNA_APP_KEY="key")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_sucesso_calcula_media_minimo_maximo(self):
        with mock.patch("requests.get", return_value=resposta(json_data={"month": {"2025-01": 10, "2025-02": 20, "2025-03": 30}})):
            self.assertEqual(
                buscar_historico_salarial("Data Scientist", "us"),
                {"media": 20, "minimo": 10, "maximo": 30},
            )

    def test_segunda_chamada_usa_cache(self):
        with mock.patch("requests.get", return_value=resposta(json_data={"month": {"a": 1}})) as get:
            buscar_historico_salarial("Data Analyst", "br")
            buscar_historico_salarial("Data Analyst", "br")
        self.assertEqual(get.call_count, 1)

    def test_credenciais_ausentes(self):
        with mock.patch.multiple(adzuna_api, ADZUNA_APP_ID=None, ADZUNA_APP_KEY=None):
            with self.assertRaisesRegex(AdzunaAPIError, "não configuradas"):
                buscar_historico_salarial("Data Scientist", "us")

    def test_timeout(self):
        with mock.patch("requests.get", side_effect=requests.exceptions.Timeout("url?app_key=key")):
            with self.assertRaisesRegex(AdzunaAPIError, "demorou") as ctx:
                buscar_historico_salarial("Data Scientist", "us")
        self.assertNotIn("key", str(ctx.exception))

    def test_erro_de_conexao(self):
        with mock.patch("requests.get", side_effect=requests.exceptions.ConnectionError()):
            with self.assertRaisesRegex(AdzunaAPIError, "conectar"):
                buscar_historico_salarial("Data Scientist", "us")

    def test_status_http(self):
        casos = {401: "inválidas", 429: "Limite", 500: "indisponível"}
        for status, trecho in casos.items():
            with self.subTest(status=status):
                buscar_historico_salarial.clear()
                with mock.patch("requests.get", return_value=resposta(status=status)):
                    with self.assertRaisesRegex(AdzunaAPIError, trecho):
                        buscar_historico_salarial("Data Scientist", "us")

    def test_json_invalido(self):
        with mock.patch("requests.get", return_value=resposta(json_erro=True)):
            with self.assertRaisesRegex(AdzunaAPIError, "inválida"):
                buscar_historico_salarial("Data Scientist", "us")

    def test_month_vazio_ou_ausente(self):
        for corpo in ({"month": {}}, {}):
            with self.subTest(corpo=corpo):
                buscar_historico_salarial.clear()
                with mock.patch("requests.get", return_value=resposta(json_data=corpo)):
                    with self.assertRaisesRegex(AdzunaAPIError, "não retornou dados"):
                        buscar_historico_salarial("Data Scientist", "us")

    def test_falha_nao_e_cacheada(self):
        with mock.patch("requests.get", return_value=resposta(status=500)) as get:
            for _ in range(2):
                with self.assertRaises(AdzunaAPIError):
                    buscar_historico_salarial("Data Scientist", "us")
        self.assertEqual(get.call_count, 2)


class ConsultarHistoricoSalarialTest(unittest.TestCase):
    def setUp(self):
        buscar_historico_salarial.clear()
        adzuna_api._falhas_recentes.clear()
        patcher = mock.patch.multiple(adzuna_api, ADZUNA_APP_ID="id", ADZUNA_APP_KEY="key")
        patcher.start()
        self.addCleanup(patcher.stop)

    def test_falha_recente_nao_chama_a_api_de_novo(self):
        with mock.patch("requests.get", return_value=resposta(status=500)) as get:
            for _ in range(3):
                with self.assertRaisesRegex(AdzunaAPIError, "indisponível"):
                    consultar_historico_salarial("Data Scientist", "us")
        self.assertEqual(get.call_count, 1)

    def test_falha_expira_apos_o_ttl(self):
        with mock.patch("requests.get", return_value=resposta(status=500)) as get:
            with mock.patch("time.monotonic", return_value=1000.0):
                with self.assertRaises(AdzunaAPIError):
                    consultar_historico_salarial("Data Scientist", "us")
            with mock.patch("time.monotonic", return_value=1000.0 + adzuna_api.FALHA_TTL + 1):
                with self.assertRaises(AdzunaAPIError):
                    consultar_historico_salarial("Data Scientist", "us")
        self.assertEqual(get.call_count, 2)

    def test_falha_de_uma_combinacao_nao_afeta_outra(self):
        with mock.patch("requests.get", side_effect=[resposta(status=500), resposta(json_data={"month": {"a": 5}})]):
            with self.assertRaises(AdzunaAPIError):
                consultar_historico_salarial("Data Scientist", "us")
            self.assertEqual(consultar_historico_salarial("Data Scientist", "br")["media"], 5)

    def test_sucesso_limpa_a_falha_registrada(self):
        adzuna_api._falhas_recentes[("Data Scientist", "us")] = (0.0, "antiga")
        with mock.patch("time.monotonic", return_value=adzuna_api.FALHA_TTL + 1):
            with mock.patch("requests.get", return_value=resposta(json_data={"month": {"a": 5}})):
                consultar_historico_salarial("Data Scientist", "us")
        self.assertNotIn(("Data Scientist", "us"), adzuna_api._falhas_recentes)


if __name__ == "__main__":
    unittest.main()
