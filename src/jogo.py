from Templo import Templo


class Jogo:
    """
    O módulo principal do jogo do tesouro Inca.
    """
    def __init__(self, templo):
        """
        Construção do objeto Jogo.

        :param templo: Uma referência para o objeto Templo.
        """
        self.templo = templo

    def inicia(self):
        """
        O jogo do Tesouro Inca começa chamando este método

        Ao iniciar o jogo o Templo deve ser montado
        :return:
        """
        self.templo.montar()


if __name__ == "__main__":
    Jogo(Templo()).inicia()