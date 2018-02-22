class Descarte:
    """
    O descarte é para onde vão as cartas que não participarão até o fim do jogo.

    Artefatos perdidos são descartados ao fim da rodada. Cartas de perigo repetidas também.
    """
    def __init__(self, baralho):
        """
        Constrói o monte de descarte.

        :param baralho: Referência para o baralho do jogo.
        """
        self.baralho = baralho

    def descarte(self, carta_descartada):
        """
        Retira do baralho a carta que não participa mais do jogo.

        :param carta_descartada: A carta que deve ser excluída do baralho.
        :return: Nada.
        """
        self.baralho.retira(carta_descartada)