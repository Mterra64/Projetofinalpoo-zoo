from models.animal import Animal

class Ave(Animal):
    def __init__(self, nome, especie, idade, envergadura):
        super().__init__(nome, especie, idade)
        self.envergadura = envergadura

    def alimentar(self):
        return f"{self.nome} comendo sementes"

    def tratar(self):
        return f"{self.nome} tratado (ave)"
        