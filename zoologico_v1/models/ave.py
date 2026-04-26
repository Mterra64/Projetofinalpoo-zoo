from models.animal import Animal


class Ave(Animal):
    def __init__(self, nome, especie, idade, envergadura_asas):
        super().__init__(nome, especie, idade)
        self.envergadura_asas = envergadura_asas

    def exibir_dados(self):
        return (
            f"{super().exibir_dados()} | Classe: Ave | Envergadura: {self.envergadura_asas} cm"
        )

    def emitir_som(self):
        return "Canto de ave"