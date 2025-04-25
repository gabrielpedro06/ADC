from admin import Admin
from gestor import Gestor
from funcionarios import Funcionario
from departamentos import Departamento

def menu_admin():
    # Menu de administração
    while True:
        print("\n == Menu de Administração ==")
        print("                              ")
        print("|  1 - Criar Funcionário     |")
        print("|  2 - Editar Funcionário    |")
        print("|  3 - Listar Funcionário    |")
        print("|  4 - Remover Funcionário   |")
        print("|  5 - Criar Departamento    |")
        print("|  6 - Editar Departamento   |")
        print("|  7 - Listar Departamento   |")
        print("|  8 - Remover Departamento  |")
        print("|  9 - Sair                  |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Funcionario.criar_funcionario()
        elif opcao == "2":
            Funcionario.listar_funcionarios()
            Funcionario.editar_funcionario()
        elif opcao == "3":
            Funcionario.listar_funcionarios()
        elif opcao == "4":
            Funcionario.listar_funcionarios()
            Funcionario.remover_funcionario()
        elif opcao == "5":
            Departamento.criar_departamento()
        elif opcao == "6":
            Departamento.listar_departamentos()
            Departamento.editar_departamento()
        elif opcao == "7":
            Departamento.listar_departamentos()
        elif opcao == "8":
            Departamento.listar_departamentos()
            Departamento.remover_departamento()
        elif opcao == "9":
            break
        else:
            print("Opção inválida!")

def menu_funcionario(funcionarios, utilizador):
    # Menu do funcionário
    funcionario = next((f for f in funcionarios if f["id"] == utilizador), None)
    if funcionario is None:
        print("Funcionário não encontrado.")
        return

    nome = funcionario["nome"]
    
    while True:
        print(f"\n == Menu de Funcionário - {nome} == ")
        print("                               ")
        print("|  1 - Editar Dados Pessoais  |")
        print("|  2 - Consultar Férias       |")
        print("|  3 - Consultar Faltas       |")
        print("|  4 - Consultar Salário      |")
        print("|  5 - Consultar Folgas       |")
        print("|  6 - Sair                   |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            Funcionario.editar_dados(utilizador)
        elif opcao == "2":
            Funcionario.consultar_ferias(utilizador)
        elif opcao == "3":
            Funcionario.consultar_faltas(utilizador)
        elif opcao == "4":
            Funcionario.consultar_salario(utilizador)
        elif opcao == "5":
            Funcionario.consultar_folgas(utilizador)
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")

def menu_gestor(departamentos, funcionarios, utilizador):
    funcionario = next((f for f in funcionarios if f["id"] == utilizador), None)
    if not funcionario:
        print("Gestor não encontrado.")
        return

    nome = funcionario["nome"]
    departamento = funcionario["id_departamento"]
    nome_departamento = next((d["nome"] for d in departamentos if d["id"] == departamento), "Departamento desconhecido")

    # Menu do gestor
    while True:
        print(f"\n == Menu de Gestor - {nome} | {nome_departamento} == ")
        print("                                             ")
        print("|  1 - Consultar Funcionários               |")
        print("|  2 - Atribuir Funcionário a Departamento  |")
        print("|  3 - Remover Funcionário de Departamento  |")
        print("|  4 - Sair                                 |")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            # Consulta os funcionários do mesmo departamento
            Gestor.consultar_funcionarios_departamento(departamento)
        elif opcao == "2":
            # Atribui um funcionário ao departamento
            funcionario_id = input("Digite o ID do funcionário a ser atribuído: ")
            novo_departamento = input("Digite o ID do novo departamento: ")
            Gestor.atribuir_funcionario_departamento(funcionario_id, novo_departamento)
        elif opcao == "3":
            # Remove um funcionário do departamento
            funcionario_id = input("Digite o ID do funcionário a ser removido: ")
            Gestor.remover_funcionario_departamento(funcionario_id)
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")

