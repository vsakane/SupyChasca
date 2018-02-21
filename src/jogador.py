class Jogador:
    """
    A pessoa que participa do jogo do Tesouro Inca.
    """
    def __init__(self, perigo):
        """
        Construção do objeto Jogador.

        :param perigo: Uma referência para o objeto Perigo.
        """
        self.perigo = perigo
    def sair (self):
        """
        O jogador do Tesouro Inca chama este método quando outra carta de perigo apresenta-se igual a uma anteriormente apresentada.

        O jogador sai quando duas cartas iguais de perigo se apresentam. Outra forma é quando no fim da rodada ele opta por sair em oposição a ficar.
        :return:
        """
        self.perigo.apresentese()