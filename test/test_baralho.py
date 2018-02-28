import unittest
from unittest.mock import MagicMock
from baralho import Baralho


class BaralhoTeste(unittest.TestCase):
    def testa_recebe(self):
        baralho = Baralho()
        baralho2 = baralho
        artefato = MagicMock()
        baralho.recebe(artefato)
        # testar se o baralho contêm o artefato recebido
        assert baralho == baralho2, (baralho, baralho2)
        assert artefato in baralho.deque_de_cartas
