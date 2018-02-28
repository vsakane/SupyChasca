from random import shuffle


class Baralho:
    """
    Contém as cartas do jogo exceto as cartas decisão
    """
    def __init__(self):
        self.deque_de_cartas = list('abcdefgh')

    def recebe(self, carta):
        """Prepara deck"""
        self.deque_de_cartas.append(carta)

    def embaralha(self):
        """
        O baralho embaralha-se
        :param self:
        :return:
        """
        shuffle(self.deque_de_cartas)