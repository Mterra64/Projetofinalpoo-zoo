class Tratador:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def exibir_dados(self):
        return f"Nome: {self.nome} | Matrícula: {self.matricula}"

    def especialidade(self):
        return "Tratador geral"