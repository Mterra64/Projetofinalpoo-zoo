class Tarefa:
    def __init__(self, tipo, animal, tratador):
        self.tipo = tipo
        self.animal = animal
        self.tratador = tratador

    def exibir_dados(self):
        return (
            f"Tarefa: {self.tipo} | Animal: {self.animal.nome} | "
            f"Tratador: {self.tratador.nome}"
        )

    def executar(self):
        return f"Executando tarefa: {self.tipo}"