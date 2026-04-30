from sistema import SistemaZoologico
from utils.menu import exibir_menu
from exceptions.base_exception import SistemaZoologicoException


def main():
    sistema = SistemaZoologico()

    while True:
        try:
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
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida.")

        except SistemaZoologicoException as e:
            print(f"Erro do sistema: {e}")

        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()
