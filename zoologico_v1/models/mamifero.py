from models.animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, especie, idade, pelo):
        super().__init__(nome, especie, idade)
        self.pelo = pelo

    def alimentar(self):
        return f"{self.nome} comendo ração"

    def tratar(self):
        return f"{self.nome} tratado (mamífero)"
        