class joia:
    """
    Recompensa recebida no jogo do tesouro Inca
    """
    def __init__(self,decisão):
        """
        Construção do objeto joia

        :param decisão: Uma referência para o objeto decisão
        """

        self.decisão = decisão

    def envia(self):
        """
        As joias são distribuídas chamando este método

        Após o envio das joias a decisão deve ser tomada
        :return:
        """
        self.decisão()
        pass

