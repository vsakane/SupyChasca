import unittest
from unittest.mock import MagicMock
from jogo import Jogo


class JogoTesta(unittest.TestCase):
    def testa_jogo_inicia(self):
        """monta o templo"""
        templo = MagicMock("templo")
        jogo = Jogo(templo)
        jogo.inicia()