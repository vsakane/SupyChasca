    class Carta:
        """
        Objeto que define as açoes do jogo do tesouro Inca.
        """
        def __init__ (self, carta):
            """
            apresenta uma ação na mesa do Jogo Inca
            :param carta: uma referência para o objeto carta
            """
            self.carta = carta
        def apresenta (self):
            """
            O jogo do Tesouro Inca chama este método após apresentar artefato.
            :return:
            """
            self.carta.partilha()