class Tarefa:
    def __init__(self, descricao, animal, tratador):
        self.descricao = descricao
        self.animal = animal
        self.tratador = tratador

    def exibir_dados(self):
        return f"{self.descricao} - {self.animal.nome}"


        