from models.tratador import Tratador


class TratadorMamiferos(Tratador):
    def __init__(self, nome, matricula, setor):
        super().__init__(nome, matricula)
        self.setor = setor

    def exibir_dados(self):
        return (
            f"{super().exibir_dados()} | Especialidade: Mamíferos | Setor: {self.setor}"
        )

    def especialidade(self):
        return "Cuidados com mamíferos"