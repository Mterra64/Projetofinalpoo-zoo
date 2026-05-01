class Alimentacao:
    def __init__(self, animal, tratador, horario):
        self.animal = animal
        self.tratador = tratador
        self.horario = horario

    def executar(self):
        return self.animal.alimentar()

    def exibir_dados(self):
        return f"{self.tratador.nome} alimentou {self.animal.nome}"

        