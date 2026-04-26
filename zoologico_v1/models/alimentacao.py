from models.tarefa import Tarefa


class Alimentacao(Tarefa):
    def __init__(self, animal, tratador, horario):
        super().__init__("Alimentação", animal, tratador)
        self.horario = horario

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Horário: {self.horario}"

    def executar(self):
        return f"{self.tratador.nome} alimentou {self.animal.nome} às {self.horario}"