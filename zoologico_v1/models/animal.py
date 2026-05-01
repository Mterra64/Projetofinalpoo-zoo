from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

        self.status = "zoologico"
        self.progresso = 0

    def iniciar_reabilitacao(self):
        self.status = "reabilitacao"
        self.progresso = 0

    def evoluir_reabilitacao(self):
        if self.status != "reabilitacao":
            return "Animal não está em reabilitação"

        self.progresso += 25

        if self.progresso >= 100:
            self.status = "liberado"
            return f"{self.nome} foi devolvido à natureza 🌿"

        return f"{self.nome} em reabilitação {self.progresso}%"

    def exibir_dados(self):
        return f"{self.nome} ({self.especie})"

    @abstractmethod
    def alimentar(self):
        pass

    @abstractmethod
    def tratar(self):
        pass
        