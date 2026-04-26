class Animal:
def __init__(self, nome, especie, idade):
self.nome = nome
self.especie = especie
self.idade = idade

def exibir_dados(self):
# [span_1](start_span)Retorna a string básica de dados comum a todos os animais[span_1](end_span)
return f"Nome: {self.nome} | Espécie: {self.especie} | Idade: {self.idade}"

def emitir_som(self):
return "Som genérico de animal"
