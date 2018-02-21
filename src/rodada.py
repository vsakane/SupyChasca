class Rodada:
    """
    Distribuição de cartas aos jogadores para iniciar a partida
    """
    def __init__(self, artefato):
        """
        objeto valioso
        :param artefato: uma referencia para a carta artefato
        """
        self.artefato = artefato
    def inicia(self):
        """
        A partida de Tesouro Inca inicia quando outra rodada acaba e ainda restam artefatos ou pedras para se ganhar

        artefato-esconder
        :return:
        """
        self.artefato.esconder()