import unittest
from relatorio.cria import relatorio

class TestCria(unittest.TestCase):
    def test_cria_relatori(self):
        R = relatorio("Meu relatório", "Eu mesmo")
        self.assertEqual(R.titulo, "Meu relatório")
