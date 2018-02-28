class Jogador:
    """
    A pessoa que participa do jogo do Tesouro Inca.

    Decide as suas ações durante o jogo se sai ou continua no templo quando surge algum perigo.
    """
    def __init__(self, perigo):
        """
        Construção do objeto Jogador.

        :param perigo: Uma referência para o objeto Perigo
        """
        self.perigo = perigo
    def sair (self):
        """
        O jogador do Tesouro Inca chama este método quando outra carta de perigo apresenta-se igual a uma anteriormente apresentada.

        O jogador sai quando duas cartas iguais de perigo se apresentam. Outra forma é quando no fim da rodada ele opta por sair em oposição a ficar.
        :return:
        """
        self.perigo.apresentese()

    def executar(self):
        """
        Decidir se sai ou continua no templo
        :return: chamar decisão
        """
        self.carta.decide()

    def decidir(self):
        """
        Sair do Jogo
        :return: fora da rodada
        """
    def recebe(self):
        """
        O jogador recebe os tesouros que estavam fora da tenda
        :return: chamar tenda
        """
        self.tenda.guarda()
    def recolhe(self):
        """
        O jogador recolhe as joias
        :return: ganha a rodada
        """
        self.rodada.inicia()

