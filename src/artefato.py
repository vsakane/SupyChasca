class Artefato:
    """item de valor do jogo"""
    def __init__(self,tenda):
      self.tenda = tenda

    def partilha(self, jogador):
        """entrega artefatos ao jogador desistente"""
        self.tenda.guarda()

    def apresenta_se(self, mesa):
        """ Artefato é mostrado e recolhido pela mesa """
        self.mesa.recolhe()
