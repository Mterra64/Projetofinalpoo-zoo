class LimpezaHabitat:
    def __init__(self, animal, tratador, area):
        self.animal = animal
        self.tratador = tratador
        self.area = area

    def executar(self):
        return f"Habitat de {self.animal.nome} limpo"

    def exibir_dados(self):
        return f"{self.tratador.nome} limpou {self.animal.nome}"

        