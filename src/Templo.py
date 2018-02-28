class Templo:
    """
    O templo é representado por 5 cartas que reserva os artefatos.

    Até o final do jogo todos os artefatos em baixo serão retirados.
    """
    def __init__(self, baralho):
        self.baralho = baralho

    def montar(self, inca_templo):
        """
        Guarda os artefatos.

        :param inca_templo: guarda os artefatos.
        :return: Nada
        """

        pass

    def virardegrau(self):
        """
        Templo mostra Artefato 1
        Templo mostra Artefato 2
        Templo mostra Artefato 3
        Templo mostra Artefato 4
        Templo mostra Artefato 5
        :return: Baralho
        """
        self.baralho.embaralha()
