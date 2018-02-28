class Artefato:
    """item de valor do jogo"""
    def __init__(self,tenda):
      self.tenda = tenda

    def partilha(self, jogador):
        """entrega artefatos ao jogador desistente"""
        self.tenda.guarda()

    def apresentase(self, mesa):
        """ Artefato é mostrado e recolhido pela mesa """
        self.mesa.recolhe()

    def esconder(self):
        """
        Artefato 1 se esconde embaixo do templo
        Artefato 2 se esconde embaixo do templo
        Artefato 3 se esconde embaixo do templo
        Artefato 4 se esconde embaixo do templo
        Artefato 5 se esconde embaixo do templo
        :return: Templo
        """
        self.templo.virardegrau
