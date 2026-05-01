class Reabilitacao:
    def __init__(self, animal, tratador):
        self.animal = animal
        self.tratador = tratador
        self.animal.iniciar_reabilitacao()

    def executar(self):
        return self.animal.evoluir_reabilitacao()

    def exibir_dados(self):
        return f"{self.animal.nome} em reabilitação"

        