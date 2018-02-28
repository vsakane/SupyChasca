import unittest
from unittest.mock import MagicMock
from jogador import Jogador


class JogadorTeste(unittest.TestCase):
    def jogador_recebe(self):
        jogador = Jogador
        joias = MagicMock()
        jogador.recebe(MagicMock)
