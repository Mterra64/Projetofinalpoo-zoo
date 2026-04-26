from models.animal import Animal


class Reptil(Animal):
    def __init__(self, nome, especie, idade, tipo_escama):
        super().__init__(nome, especie, idade)
        self.tipo_escama = tipo_escama

    def exibir_dados(self):
        return (
            f"{super().exibir_dados()} | Classe: Réptil | Escama: {self.tipo_escama}"
        )

    def emitir_som(self):
        return "Som de réptil"