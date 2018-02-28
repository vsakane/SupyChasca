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

    def testa_embaralha(self):
        baralho = Baralho()
        lista = baralho.deque_de_cartas [:]
        baralho.embaralha ()
        lista1 = baralho.deque_de_cartas
        assert lista1 != lista, (lista1, lista)
        