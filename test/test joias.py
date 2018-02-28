import unittest
from unittest.mock import MagicMock
from joia import Joia


class JoiaTeste(unittest.TestCase):
    def teste_joia_distribui(self):
        joia = MagicMock()
        joia.distribuir = MagicMock()
        joia = Joia
        joia1 = joia