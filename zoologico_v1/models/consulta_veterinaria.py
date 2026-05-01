class ConsultaVeterinaria:
    def __init__(self, animal, tratador, veterinario):
        self.animal = animal
        self.tratador = tratador
        self.veterinario = veterinario

    def executar(self):
        return self.animal.tratar()

    def exibir_dados(self):
        return f"{self.animal.nome} consultado por {self.veterinario}"
        