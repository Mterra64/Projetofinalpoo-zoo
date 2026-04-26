from models.animal import Animal


class Mamifero(Animal):
    def __init__(self, nome, especie, idade, tipo_pelo):
        super().__init__(nome, especie, idade)
        self.tipo_pelo = tipo_pelo

    def exibir_dados(self):
        return (
            f"{super().exibir_dados()} | Classe: Mamífero | Tipo de pelo: {self.tipo_pelo}"
        )

    def emitir_som(self):
        return "Som de mamífero"