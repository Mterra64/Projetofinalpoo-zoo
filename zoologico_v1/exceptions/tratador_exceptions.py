from exceptions.base_exception import SistemaZoologicoException

class TratadorInvalidoException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Dados do tratador inválidos.")

class TratadorNaoEncontradoException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Tratador não encontrado.")

class ListaTratadoresVaziaException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Nenhum tratador cadastrado.")
