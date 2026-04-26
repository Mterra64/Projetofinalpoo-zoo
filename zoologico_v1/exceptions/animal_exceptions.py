from exceptions.base_exception import SistemaZoologicoException

class AnimalInvalidoException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Dados do animal inválidos.")

class AnimalNaoEncontradoException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Animal não encontrado.")

class ListaAnimaisVaziaException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Nenhum animal cadastrado.")
