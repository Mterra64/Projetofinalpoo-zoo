from models.mamifero import Mamifero
from models.ave import Ave
from models.reptil import Reptil

from models.tratador_mamiferos import TratadorMamiferos
from models.tratador_aves import TratadorAves

from models.tarefa import Tarefa
from models.alimentacao import Alimentacao
from models.limpeza_habitat import LimpezaHabitat
from models.consulta_veterinaria import ConsultaVeterinaria

# Exceptions
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
        self.animais = []
        self.tratadores = []
        self.tarefas = []

    # ---------------- ANIMAIS ---------------- #

    def cadastrar_animal(self):
        print("\n=== Cadastro de Animal ===")
        print("1 - MamÃ­fero")
        print("2 - Ave")
        print("3 - RÃ©ptil")
        tipo = input("Escolha o tipo: ").strip()

        nome = input("Nome: ").strip()
        especie = input("EspÃ©cie: ").strip()
        idade = input("Idade: ").strip()

        #Fluxo para dados invalidos
        if not nome or not especie or not idade:
            raise AnimalInvalidoException()

        if tipo == "1":
            tipo_pelo = input("Tipo de pelo: ").strip()
            if not tipo_pelo:
                raise AnimalInvalidoException()
            animal = Mamifero(nome, especie, idade, tipo_pelo)

        elif tipo == "2":
            envergadura = input("Envergadura: ").strip()
            if not envergadura:
                raise AnimalInvalidoException()
            animal = Ave(nome, especie, idade, envergadura)

        elif tipo == "3":
            escama = input("Tipo de escama: ").strip()
            if not escama:
                raise AnimalInvalidoException()
            animal = Reptil(nome, especie, idade, escama)

        else:
            raise AnimalInvalidoException()

        self.animais.append(animal)
        print("â Animal cadastrado!")

    def listar_animais(self):
        if not self.animais:
            raise ListaAnimaisVaziaException()

        for i, animal in enumerate(self.animais, start=1):
            print(f"{i}. {animal.exibir_dados()}")

    # ---------------- TRATADORES ---------------- #

    def cadastrar_tratador(self):
        print("\n=== Cadastro de Tratador ===")
        print("1 - MamÃ­feros")
        print("2 - Aves")
        tipo = input("Escolha o tipo: ").strip()

        nome = input("Nome: ").strip()
        matricula = input("MatrÃ­cula: ").strip()
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
        print("â Tratador cadastrado!")

    def listar_tratadores(self):
        if not self.tratadores:
            raise ListaTratadoresVaziaException()

        for i, tratador in enumerate(self.tratadores, start=1):
            print(f"{i}. {tratador.exibir_dados()}")

    # ---------------- TAREFAS ---------------- #

    def registrar_tarefa(self):
        if not self.animais or not self.tratadores:
            raise DependenciaNaoAtendidaException()

        print("\nAnimais:")
        for i, a in enumerate(self.animais):
            print(f"{i} - {a.nome}")

        try:
            animal = self.animais[int(input("Escolha o animal: "))]
        except:
            raise AnimalNaoEncontradoException()

        print("\nTratadores:")
        for i, t in enumerate(self.tratadores):
            print(f"{i} - {t.nome}")

        try:
            tratador = self.tratadores[int(input("Escolha o tratador: "))]
        except:
            raise TratadorNaoEncontradoException()

        print("\nTipos de tarefa:")
        print("1 - AlimentaÃ§Ã£o")
        print("2 - Limpeza")
        print("3 - Consulta")
        print("4 - GenÃ©rica")

        tipo = input("Escolha: ").strip()

        if tipo == "1":
            horario = input("HorÃ¡rio: ").strip()
            tarefa = Alimentacao(animal, tratador, horario)

        elif tipo == "2":
            area = input("Ãrea: ").strip()
            tarefa = LimpezaHabitat(animal, tratador, area)

        elif tipo == "3":
            vet = input("VeterinÃ¡rio: ").strip()
            tarefa = ConsultaVeterinaria(animal, tratador, vet)

        elif tipo == "4":
            desc = input("DescriÃ§Ã£o: ").strip()
            tarefa = Tarefa(desc, animal, tratador)

        else:
            raise TarefaInvalidaException()

        self.tarefas.append(tarefa)
        print("â Tarefa registrada!")

    def listar_tarefas(self):
        if not self.tarefas:
            raise ListaTarefasVaziaException()

        for i, tarefa in enumerate(self.tarefas, start=1):
            print(f"{i}. {tarefa.exibir_dados()}")
            