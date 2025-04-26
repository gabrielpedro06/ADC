import funcoes as f
from funcionarios import Funcionario

def menu_admin():
    # Menu de administração
    while True:
        print("\n == Menu de Administração ==")
        print("                              ")
        print("|  1 - Criar Funcionário     |")
        print("|  2 - Editar Funcionário    |")
        print("|  3 - Listar Funcionários   |")
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
            print("A voltar ao menu inicial!")
            return
        else:
            print("Opção inválida!")

def menu_funcionario(funcionarios, utilizador):
    # Encontrar o funcionário com o ID correspondente ao utilizador
    funcionario = next((f for f in funcionarios if f["id"] == utilizador), None)
    if not funcionario:
        print("Funcionário não encontrado!")
        return

    nome = funcionario["nome"]
    funcionario_atual = Funcionario(funcionario)

    while True:
        print(f"\n == Menu de Funcionário - {nome} == ")
        print("                               ")
        print("|  1 - Editar Dados Pessoais  |")
        print("|  2 - Consultar Férias       |")
        print("|  3 - Consultar Faltas       |")
        print("|  4 - Consultar Salário      |")
        print("|  5 - Consultar Folgas       |")
        print("|  6 - Consultar Perfil       |")
        print("|  7 - Sair                   |")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            funcionario_atual.editar_dados()
        elif opcao == "2":
            funcionario_atual.consultar_ferias()
        elif opcao == "3":
            funcionario_atual.consultar_faltas()
        elif opcao == "4":
            funcionario_atual.consultar_salario()
        elif opcao == "5":
            funcionario_atual.consultar_folgas()
        elif opcao == "6":
            funcionario_atual.consultar_perfil()
        elif opcao == "7":
            print("A voltar ao menu inicial!")
            return
        else:
            print("Opção inválida!")


def menu_gestor(departamentos, funcionarios, utilizador):
    # Encontrar o funcionário com o ID correspondente ao utilizador
    funcionario = next((f for f in funcionarios if f['id'] == utilizador), None)
    if funcionario:
        nome = funcionario['nome']
        departamento = funcionario['id_departamento']

        # Encontrar o nome do departamento com base no id_departamento
        nome_departamento = next((d['nome'] for d in departamentos if d['id'] == departamento), None)

        if nome_departamento:
            # Menu do gestor
            while True:
                print(f"\n == Menu de Gestor - {nome} | {nome_departamento} == ")
                print("                                             ")
                print("|  1 - Consultar Funcionários               |")
                print("|  2 - Disponibilidade Semanal              |")
                print("|  3 - Atribuir Funcionário a Departamento  |")
                print("|  4 - Remover Funcionário de Departamento  |")
                print("|  5 - Sair                                 |")
                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    f.consultar_funcionarios_departamento(departamento)
                elif opcao == "2":
                    f.lista_func_semana(departamento)
                elif opcao == "3":
                    f.atribuir_funcionario_departamento()
                elif opcao == "4":
                    f.remover_funcionario_departamento()
                elif opcao == "5":
                    print("A voltar ao menu inicial!")
                    return
                else:
                    print("Opção inválida!")
        else:
            print("Departamento não encontrado!")
    else:
        print("Funcionário não encontrado!")