from random import shuffle


class Baralho:
"""
Contém as cartas do jogo exceto as cartas decisão
"""
    def __init__(self,baralho):
        self.baralho = list("abcdefgh")

    def recebe(self, carta):
        """Prepara deck"""
        self.baralho.recebe()

    def embaralha(self):
        """
        O baralho embaralha-se
        :param self:
        :return:
        """
        shuffle(self.baralho)