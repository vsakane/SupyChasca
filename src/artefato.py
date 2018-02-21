class Artefato:
    """item de valor do jogo"""
    def __init__(self,tenda):
      self.tenda = tenda

    def partilha(self):
        """entrega artefatos ao jogador desistente"""
        self.tenda.guarda