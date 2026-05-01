from models.mamifero import Mamifero
from models.ave import Ave
from models.reptil import Reptil

from models.tratador_mamiferos import TratadorMamiferos
from models.tratador_aves import TratadorAves
from models.tratador_reptil import TratadorReptil

from models.tarefa import Tarefa
from models.alimentacao import Alimentacao
from models.limpeza_habitat import LimpezaHabitat
from models.consulta_veterinaria import ConsultaVeterinaria
from models.reabilitacao import Reabilitacao

class SistemaZoologico:

    def __init__(self):
        self.animais = []
        self.tratadores = []
        self.tarefas = []

    def cadastrar_animal(self):
        print("\n1 Mamífero | 2 Ave | 3 Réptil")
        tipo = input("Tipo: ")

        nome = input("Nome: ")
        especie = input("Espécie: ")
        idade = input("Idade: ")

        if tipo == "1":
            animal = Mamifero(nome, especie, idade, input("Pelo: "))
        elif tipo == "2":
            animal = Ave(nome, especie, idade, input("Envergadura: "))
        elif tipo == "3":
            animal = Reptil(nome, especie, idade, input("Escama: "))
        else:
            return

        self.animais.append(animal)
        print("Animal cadastrado!")

    def listar_animais(self):
        for i, a in enumerate(self.animais):
            print(i, a.exibir_dados())

    def cadastrar_tratador(self):
        print("\n1 Mamíferos | 2 Aves | 3 Répteis")
        tipo = input("Tipo: ")

        nome = input("Nome: ")
        mat = input("Matrícula: ")
        setor = input("Setor: ")

        if tipo == "1":
            t = TratadorMamiferos(nome, mat, setor)
        elif tipo == "2":
            t = TratadorAves(nome, mat, setor)
        else:
            t = TratadorReptil(nome, mat, setor)

        self.tratadores.append(t)
        print("Tratador cadastrado!")

    def listar_tratadores(self):
        for i, t in enumerate(self.tratadores):
            print(i, t.exibir_dados())

    def registrar_tarefa(self):

        print("\nAnimais:")
        for i, a in enumerate(self.animais):
            print(i, a.nome)
        animal = self.animais[int(input("Escolha: "))]

        print("\nTratadores:")
        for i, t in enumerate(self.tratadores):
            print(i, t.nome)
        tratador = self.tratadores[int(input("Escolha: "))]

        print("\n1 Alimentação | 2 Limpeza | 3 Consulta | 4 Reabilitação")
        tipo = input("Tipo: ")

        if tipo == "1":
            tarefa = Alimentacao(animal, tratador, input("Horário: "))
        elif tipo == "2":
            tarefa = LimpezaHabitat(animal, tratador, input("Área: "))
        elif tipo == "3":
            tarefa = ConsultaVeterinaria(animal, tratador, input("Veterinário: "))
        elif tipo == "4":
            tarefa = Reabilitacao(animal, tratador)
        else:
            return

        self.tarefas.append(tarefa)

        # 🔥 EXECUTA NA HORA
        print("Resultado:", tarefa.executar())

    def listar_tarefas(self):
        for i, t in enumerate(self.tarefas):
            print(i, t.exibir_dados())
            