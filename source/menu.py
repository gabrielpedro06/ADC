import funcoes as f
from funcionarios import Funcionario

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
            f.criar_funcionario()
        elif opcao == "2":
            f.listar_funcionarios()
            f.editar_funcionario()
        elif opcao == "3":
            f.listar_funcionarios()
        elif opcao == "4":
            f.listar_funcionarios()
            f.remover_funcionario()
        elif opcao == "5":
            f.criar_departamento()
        elif opcao == "6":
            f.listar_departamentos()
            f.editar_departamento()
        elif opcao == "7":
            f.listar_departamentos()
        elif opcao == "8":
            f.listar_departamentos()
            f.remover_departamento()
        elif opcao == "9":
            break
        else:
            print("Opção inválida!")

def menu_funcionario(funcionarios, utilizador):
    # Menu do funcionário
    for funcionario in funcionarios:
        if funcionario["id"] == utilizador:
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
            Funcionario.editar_dados()
        elif opcao == "2":
            Funcionario.consultar_ferias()
        elif opcao == "3":
            Funcionario.consultar_faltas()
        elif opcao == "4":
            Funcionario.consultar_salario()
        elif opcao == "5":
            Funcionario.consultar_folgas()
        elif opcao == "6":
            break
        else:
            print("Opção inválida!")

def menu_gestor(departamentos, funcionarios, utilizador):
    for funcionario in funcionarios:
        if funcionario["id"] == utilizador:
            nome = funcionario["nome"]
            departamento = funcionario["id_departamento"]
            
    for d in departamentos:
        if d["id"] == departamento:
            nome_departamento = d["nome"]
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
            f.consultar_funcionarios_departamento(utilizador.departamento)
        elif opcao == "2":
            f.atribuir_funcionario_departamento()
        elif opcao == "3":
            f.remover_funcionario_departamento()
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
