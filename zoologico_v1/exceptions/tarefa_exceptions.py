from exceptions.base_exception import SistemaZoologicoException

class TarefaInvalidaException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Tipo de tarefa inválido.")

class ListaTarefasVaziaException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Nenhuma tarefa registrada.")

class DependenciaNaoAtendidaException(SistemaZoologicoException):
    def __init__(self):
        super().__init__("Cadastre animais e tratadores primeiro.")
