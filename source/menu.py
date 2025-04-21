import funcoes as f
from funcionarios import Funcionario
def menu_admin(funcionarios, departamentos):
    # Menu de administração
    while True:
        print("\n == Menu de Administração ==")
        print("                              ")
        print("|  1 - Criar Funcionário     |")
        print("|  2 - Editar Funcionário    |")
        print("|  3 - Remover Funcionário   |")
        print("|  4 - Criar Departamento    |")
        print("|  5 - Editar Departamento   |")
        print("|  6 - Remover Departamento  |")
        print("|  7 - Sair                  |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Criar novo funcionário
            f.criar_funcionario()
        elif opcao == "2":
            # Editar funcionário
            Funcionario.editar_dados()
        elif opcao == "3":
            # Remover funcionário
            pass  # Implementar remoção de funcionário
        elif opcao == "4":
            # Criar novo departamento
            pass  # Implementar criação de departamento
        elif opcao == "5":
            # Editar departamento
            pass  # Implementar edição de departamento
        elif opcao == "6":
            # Remover departamento
            pass  # Implementar remoção de departamento
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")

def menu_funcionario(funcionarios, user):
    # Menu do funcionário
    while True:
        print(f"\n == Menu de Funcionário - {user['nome']} == ")
        print("                               ")
        print("|  1 - Editar Dados Pessoais  |")
        print("|  2 - Consultar Férias       |")
        print("|  3 - Consultar Faltas       |")
        print("|  4 - Consultar Salário      |")
        print("|  5 - Consultar Folgas       |")
        print("|  6 - Sair                   |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            user.editar_dados()
        elif opcao == "2":
            user.consultar_ferias()
        elif opcao == "3":
            user.consultar_faltas()
        elif opcao == "4":
            user.consultar_salario()
        elif opcao == "5":
            user.consultar_folgas()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")

def menu_gestor(departamentos, funcionarios, user):
    # Menu do gestor
    while True:
        print(f"\n == Menu de Gestor - {user['nome']} == ")
        print("                                             ")
        print("|  1 - Consultar Funcionários               |")
        print("|  2 - Atribuir Funcionário a Departamento  |")
        print("|  3 - Remover Funcionário de Departamento  |")
        print("|  4 - Sair                                 |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Consultar funcionários do departamento
            pass  # Consultar funcionários
        elif opcao == "2":
            # Atribuir funcionário a departamento
            pass  # Atribuir funcionário
        elif opcao == "3":
            # Remover funcionário de departamento
            pass  # Remover funcionário
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
