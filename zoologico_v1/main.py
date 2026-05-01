from sistema import SistemaZoologico
from utils.menu import exibir_menu


def main():
    sistema = SistemaZoologico()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            sistema.cadastrar_animal()

        elif opcao == "2":
            sistema.listar_animais()

        elif opcao == "3":
            sistema.cadastrar_tratador()

        elif opcao == "4":
            sistema.listar_tratadores()

        elif opcao == "5":
            sistema.registrar_tarefa()

        elif opcao == "6":
            sistema.listar_tarefas()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    main()
    