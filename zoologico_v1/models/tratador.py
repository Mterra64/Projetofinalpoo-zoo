class Tratador:
    def __init__(self, nome, matricula, setor):
        self.nome = nome
        self.matricula = matricula
        self.setor = setor

    def exibir_dados(self):
        return f"{self.nome} - {self.setor}"

        