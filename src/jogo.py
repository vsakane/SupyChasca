from Templo import Templo
from baralho import Baralho

class Jogo:
    """
    O módulo principal do jogo do tesouro Inca.
    """
    def __init__(self, templo = None):
        """
        Construção do objeto Jogo.

        :param templo: Uma referência para o objeto Templo.
        """
        self.baralho = Baralho()
        self.templo = templo

    def inicia(self):
        """
        O jogo do Tesouro Inca começa chamando este método

        Ao iniciar o jogo o Templo deve ser montado
        :return:
        """
        #self.templo.montar()
        self.baralho.embaralha()
        print (self.baralho.deque_de_cartas)


if __name__ == "__main__":
    Jogo().inicia()