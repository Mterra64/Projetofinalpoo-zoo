import json

from models.mamifero import Mamifero
from models.ave import Ave
from models.reptil import Reptil

from models.tratador_mamiferos import TratadorMamiferos
from models.tratador_aves import TratadorAves
from models.tratador_reptil import TratadorReptil

from models.alimentacao import Alimentacao
from models.limpeza_habitat import LimpezaHabitat
from models.consulta_veterinaria import ConsultaVeterinaria
from models.reabilitacao import Reabilitacao


class SistemaZoologico:

    def __init__(self):
        self.animais = []
        self.tratadores = []
        self.tarefas = []

    # ---------------- SALVAR ---------------- #

    def salvar_dados(self):
        dados = {
            "animais": [
                {"nome": a.nome, "especie": a.especie, "status": a.status}
                for a in self.animais
            ],
            "tratadores": [
                {"nome": t.nome, "setor": t.setor, "matricula": t.matricula}
                for t in self.tratadores
            ],
            "tarefas": [
                t.exibir_dados() for t in self.tarefas
            ]
        }

        with open("dados_zoo.json", "w") as f:
            json.dump(dados, f, indent=4)

    # ---------------- ANIMAIS ---------------- #

    def cadastrar_animal(self):
        print("\n1 Mamífero | 2 Ave | 3 Réptil")
        tipo = input("Tipo: ").strip()

        nome = input("Nome: ").strip()
        especie = input("Espécie: ").strip()
        idade = input("Idade: ").strip()

        if not nome or not especie or not idade:
            print("Dados inválidos")
            return

        print("\nDestino:")
        print("1 - Zoológico")
        print("2 - Reabilitação")
        destino = input("Escolha: ").strip()

        if tipo == "1":
            animal = Mamifero(nome, especie, idade, input("Pelo: "))
        elif tipo == "2":
            animal = Ave(nome, especie, idade, input("Envergadura: "))
        elif tipo == "3":
            animal = Reptil(nome, especie, idade, input("Escama: "))
        else:
            print("Tipo inválido")
            return

        if destino == "2":
            animal.iniciar_reabilitacao()

        self.animais.append(animal)
        self.salvar_dados()

        print("✅ Animal cadastrado!")

    def listar_animais(self):
        print("\n=== ANIMAIS ===")
        print("ID | Nome | Espécie | Status")
        for i, a in enumerate(self.animais, start=1):
            print(f"{i} | {a.nome} | {a.especie} | {a.status}")

    # ---------------- TRATADORES ---------------- #

    def cadastrar_tratador(self):
        print("\n1 Mamíferos | 2 Aves | 3 Répteis")
        tipo = input("Tipo: ").strip()

        nome = input("Nome: ").strip()
        mat = input("Matrícula: ").strip()
        setor = input("Setor: ").strip()

        if not nome or not mat or not setor:
            print("Dados inválidos")
            return

        if tipo == "1":
            t = TratadorMamiferos(nome, mat, setor)
        elif tipo == "2":
            t = TratadorAves(nome, mat, setor)
        else:
            t = TratadorReptil(nome, mat, setor)

        self.tratadores.append(t)
        self.salvar_dados()

        print("✅ Tratador cadastrado!")

    def listar_tratadores(self):
        print("\n=== TRATADORES ===")
        print("ID | Nome | Setor | Matrícula")
        for i, t in enumerate(self.tratadores, start=1):
            print(f"{i} | {t.nome} | {t.setor} | {t.matricula}")

    # ---------------- TAREFAS ---------------- #

    def registrar_tarefa(self):

        if not self.animais or not self.tratadores:
            print("Cadastre animais e tratadores primeiro")
            return

        print("\nAnimais:")
        for i, a in enumerate(self.animais, start=1):
            print(f"{i} - {a.nome}")

        entrada = input("Escolha: ").strip()
        if not entrada:
            print("Entrada inválida")
            return
        animal = self.animais[int(entrada) - 1]

        print("\nTratadores:")
        for i, t in enumerate(self.tratadores, start=1):
            print(f"{i} - {t.nome}")

        entrada = input("Escolha: ").strip()
        if not entrada:
            print("Entrada inválida")
            return
        tratador = self.tratadores[int(entrada) - 1]

        print("\n1 Alimentação | 2 Limpeza | 3 Consulta | 4 Reabilitação")
        tipo = input("Tipo: ").strip()

        if tipo == "1":
            tarefa = Alimentacao(animal, tratador, input("Horário: "))
        elif tipo == "2":
            tarefa = LimpezaHabitat(animal, tratador, input("Área: "))
        elif tipo == "3":
            tarefa = ConsultaVeterinaria(animal, tratador, input("Veterinário: "))
        elif tipo == "4":
            tarefa = Reabilitacao(animal, tratador)
        else:
            print("Tipo inválido")
            return

        self.tarefas.append(tarefa)

        print("Resultado:", tarefa.executar())
        self.salvar_dados()

    def listar_tarefas(self):
        print("\n=== TAREFAS ===")
        print("ID | Tratador | Animal | Tipo")
        for i, t in enumerate(self.tarefas, start=1):
            print(f"{i} | {t.tratador.nome} | {t.animal.nome} | {t.__class__.__name__}")
            