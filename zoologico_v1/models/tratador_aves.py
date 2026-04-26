from models.tratador import Tratador


class TratadorAves(Tratador):
    def __init__(self, nome, matricula, setor):
        super().__init__(nome, matricula)
        self.setor = setor

    def exibir_dados(self):
        return (
            f"{super().exibir_dados()} | Especialidade: Aves | Setor: {self.setor}"
        )

    def especialidade(self):
        return "Cuidados com aves"