import unittest
from unittest.mock import MagicMock
from jogador import Jogador


class Testa_JogadorRecolher(unittest.TestCase):
    def testa_recolher(self):
        perigo= MagicMock()
        jogador= Jogador(perigo)
        jogador.recolhe()



