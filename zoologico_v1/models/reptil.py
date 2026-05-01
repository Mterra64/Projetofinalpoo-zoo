from models.animal import Animal

class Reptil(Animal):
    def __init__(self, nome, especie, idade, escama):
        super().__init__(nome, especie, idade)
        self.escama = escama

    def alimentar(self):
        return f"{self.nome} comendo insetos"

    def tratar(self):
        return f"{self.nome} tratado (réptil)"
        