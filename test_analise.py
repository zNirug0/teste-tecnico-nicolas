import unittest
import pandas as pd
from analise_atendimentos import taxa_conversao, palavras, horario_pico

df = pd.read_csv("C:/Users/Nirug/Desktop/DESAFIO ESTAGIO/data/atendimentos_feira.csv")

class TestAnaliseAtendimentos(unittest.TestCase):

    def test_taxa_conversao_valida(self):
        """Verifica se a taxa de conversão está entre 0 e 100"""
        total, taxa = taxa_conversao()
        self.assertTrue(0 <= taxa <= 100, "Taxa de conversão deve estar entre 0 e 100")

    def test_top_10_palavras(self):
        """Verifica se a função palavras retorna exatamente 10 palavras"""
        top10 = palavras()
        self.assertEqual(len(top10), 10, "A função palavras deve retornar exatamente 10 itens")

    def test_periodo_pico_valido(self):
        """Verifica se o período de pico está na lista esperada"""
        periodo_pico, atendimentos_pico = horario_pico()
        self.assertIn(periodo_pico, ["Manhã", "Tarde", "Noite"], "Período de pico deve ser Manhã, Tarde ou Noite")

if __name__ == "__main__":
    unittest.main()
