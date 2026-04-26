import pickle
import os
from models.mamifero import Mamifero
from models.ave import Ave
from models.reptil import Reptil

from models.tratador_mamiferos import TratadorMamiferos
from models.tratador_aves import TratadorAves

from models.tarefa import Tarefa
from models.alimentacao import Alimentacao
from models.limpeza_habitat import LimpezaHabitat
from models.consulta_veterinaria import ConsultaVeterinaria

# [span_5](start_span)Exceptions[span_5](end_span)
from exceptions.animal_exceptions import (
AnimalInvalidoException,
AnimalNaoEncontradoException,
ListaAnimaisVaziaException,
)
from exceptions.tratador_exceptions import (
TratadorInvalidoException,
TratadorNaoEncontradoException,
ListaTratadoresVaziaException,
)
from exceptions.tarefa_exceptions import (
TarefaInvalidaException,
ListaTarefasVaziaException,
DependenciaNaoAtendidaException,
)

class SistemaZoologico:

def __init__(self):
self.arquivo_dados = 'dados_zoo.pkl'
# [span_6](start_span)Tenta carregar dados existentes ao iniciar (Tarefa 5)[span_6](end_span)
self.animais, self.tratadores, self.tarefas = self.carregar_dados_arquivo()

# -[span_7](start_span)--------------- PERSISTÊNCIA (TAREFA 5)[span_7](end_span) ---------------- #

def salvar_dados_arquivo(self):
"""Salva o estado atual das listas em um arquivo binário."""
try:
with open(self.arquivo_dados, 'wb') as f:
dados = {'animais': self.animais, 'tratadores': self.tratadores, 'tarefas': self.tarefas}
pickle.dump(dados, f)
except Exception as e:
print(f"Erro ao salvar arquivos: {e}")

def carregar_dados_arquivo(self):
"""Carrega os dados do arquivo se ele existir (Tarefa 5)."""
if os.path.exists(self.arquivo_dados):
try:
with open(self.arquivo_dados, 'rb') as f:
dados = pickle.load(f)
return dados['animais'], dados['tratadores'], dados['tarefas']
except:
return [], [], []
return [], [], []

# ---------------- ANIMAIS ---------------- #

def cadastrar_animal(self):
print("\n=== Cadastro de Animal ===")
print("1 - Mamífero\n2 - Ave\n3 - Réptil")
tipo = input("Escolha o tipo: ").strip()
nome = input("Nome: ").strip()
especie = input("Espécie: ").strip()
idade = input("Idade: ").strip()

if not nome or not especie or not idade:
raise AnimalInvalidoException()

if tipo == "1":
tipo_pelo = input("Tipo de pelo: ").strip()
animal = Mamifero(nome, especie, idade, tipo_pelo)
elif tipo == "2":
envergadura = input("Envergadura: ").strip()
animal = Ave(nome, especie, idade, envergadura)
elif tipo == "3":
escama = input("Tipo de escama: ").strip()
animal = Reptil(nome, especie, idade, escama)
else:
raise AnimalInvalidoException()

self.animais.append(animal)
[span_8](start_span)self.salvar_dados_arquivo() # Gravação automática[span_8](end_span)
print("✅ Animal cadastrado!")

def listar_animais(self):
if not self.animais:
raise ListaAnimaisVaziaException()
for i, animal in enumerate(self.animais, start=1):
print(f"{i}. {animal.exibir_dados()}")

# ---------------- TRATADORES ---------------- #

def cadastrar_tratador(self):
print("\n=== Cadastro de Tratador ===")
print("1 - Mamíferos\n2 - Aves")
tipo = input("Escolha o tipo: ").strip()
nome = input("Nome: ").strip()
matricula = input("Matrícula: ").strip()
setor = input("Setor: ").strip()

if not nome or not matricula or not setor:
raise TratadorInvalidoException()

if tipo == "1":
tratador = TratadorMamiferos(nome, matricula, setor)
elif tipo == "2":
tratador = TratadorAves(nome, matricula, setor)
else:
raise TratadorInvalidoException()

self.tratadores.append(tratador)
self.salvar_dados_arquivo()
print("✅ Tratador cadastrado!")

def listar_tratadores(self):
if not self.tratadores:
raise ListaTratadoresVaziaException()
for i, tratador in enumerate(self.tratadores, start=1):
print(f"{i}. {tratador.exibir_dados()}")

# -[span_9](start_span)[span_10](start_span)--------------- TAREFAS (RASTREAMENTO TAREFA 7)[span_9](end_span)[span_10](end_span) ---------------- #

def registrar_tarefa(self):
if not self.animais or not self.tratadores:
raise DependenciaNaoAtendidaException()

print("\nAnimais:")
for i, a in enumerate(self.animais):
print(f"{i} - {a.nome}")
animal = self.animais[int(input("Escolha o animal: "))]

print("\nTratadores:")
for i, t in enumerate(self.tratadores):
print(f"{i} - {t.nome}")
tratador = self.tratadores[int(input("Escolha o tratador: "))]

print("\n1 - Alimentação\n2 - Limpeza\n3 - Consulta\n4 - Genérica")
tipo = input("Escolha: ").strip()

if tipo == "1":
horario = input("Horário: ").strip()
tarefa = Alimentacao(animal, tratador, horario)
elif tipo == "2":
area = input("Área: ").strip()
tarefa = LimpezaHabitat(animal, tratador, area)
elif tipo == "3":
vet = input("Veterinário: ").strip()
tarefa = ConsultaVeterinaria(animal, tratador, vet)
elif tipo == "4":
desc = input("Descrição: ").strip()
tarefa = Tarefa(desc, animal, tratador)
else:
raise TarefaInvalidaException()

self.tarefas.append(tarefa)
self.salvar_dados_arquivo()
print("✅ Tarefa registrada!")

def listar_tarefas(self):
[span_11](start_span)[span_12](start_span)"""Rastreamento de atividades pelo administrador (Tarefa 7)[span_11](end_span)[span_12](end_span)."""
if not self.tarefas:
raise ListaTarefasVaziaException()
[span_13](start_span)print("\n=== PAINEL DO ADMINISTRADOR: RASTREAMENTO[span_13](end_span) ===")
for i, tarefa in enumerate(self.tarefas, start=1):
print(f"{i}. {tarefa.exibir_dados()}")
