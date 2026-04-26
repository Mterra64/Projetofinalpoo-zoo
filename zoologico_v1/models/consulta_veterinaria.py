from models.tarefa import Tarefa


class ConsultaVeterinaria(Tarefa):
    def __init__(self, animal, tratador, veterinario):
        super().__init__("Consulta Veterinária", animal, tratador)
        self.veterinario = veterinario

    def exibir_dados(self):
        return f"{super().exibir_dados()} | Veterinário: {self.veterinario}"

    def executar(self):
        return (
            f"{self.animal.nome} foi encaminhado por {self.tratador.nome} "
            f"para consulta com {self.veterinario}"
        )