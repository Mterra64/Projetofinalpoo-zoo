from models.tarefa import Tarefa


class LimpezaHabitat(Tarefa):
    def __init__(self, animal, tratador, area):
        super().__init__("Limpeza do Habitat", animal, tratador)
        self.area = area

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Área: {self.area}"

    def executar(self):
        return f"{self.tratador.nome} limpou a área {self.area} de {self.animal.nome}"