import json
from funcionarios import Funcionario

def test_nif_telemovel(input):
    if len(input) != 9 and input.isdigit():
        raise ValueError("Número inválido!")

def test_iban(input):
    if len(input) == 21 and input.isdigit():
        return "PT50" + input
    else:
        raise ValueError("IBAN inválido!")

def test_numbers(input):
    if not input.isdigit():
        raise ValueError("Insira um número!")

def criar_funcionario():
    print("Criar funcionário")
    # Criar novo funcionário
      
    nome = input("Insira o nome: ")
    morada = input("Insira a morada: ")
    telemovel = input("Insira o telemóvel: ")
    test_nif_telemovel(telemovel)
        
    nif = input("Insira o NIF: ")
    test_nif_telemovel(nif)
        
    sexo = input("Insira o sexo: ")
    iban = input("Insira o IBAN (sem PT50): ")
    iban_completo = test_iban(iban)
        
    doencas = input("Insira a(s) doença(s) separadas por vírgulas: ")
    
    ferias = input("Insira o número de dias de férias: ")
    test_numbers(ferias)
    ferias = int(ferias)
    
    salario = input("Insira o salário: ")
    test_numbers(salario)
    salario = salario + "€"
    
    horario = input("Insira o horário (inicioH - fimH): ")
    folgas = input("Insira os dias de folgas (separados por vírgula): ")
    
    with open('data/funcionarios.json', 'r', encoding="utf-8") as arquivo_funcionarios:
        funcionarios = json.load(arquivo_funcionarios)
        id = max(funcionario['id'] for funcionario in funcionarios) + 1
    
    with open('data/departamentos.json', 'r', encoding="utf-8") as arquivo_departamentos:
        departamentos = json.load(arquivo_departamentos)
        input_sigla = input("Insira a sigla do departamento: ").upper()
        id_departamento = 0
        found = False
        for departamento in departamentos:
            if input_sigla.upper() == departamento['sigla']:
                id_departamento = departamento['id']
                found = True
                
        if not found:
            print("Departamento não encontrado!")
            
    faltas = {"justificadas": 0, "injustificadas": 0}
    dados = [id, id_departamento, nome, morada, telemovel, nif, sexo, iban_completo, doencas, ferias, faltas, salario, horario, folgas]
    funcionario = Funcionario(dados)
    funcionario.colocar_funcionario()
    funcionario.__str__()
    
def editar_funcionario():
    with open('data/funcionarios.json', 'r', encoding="utf-8") as f:
        funcionarios = json.load(f)

    id_func = int(input("ID do funcionário a editar: "))
    funcionario = next((f for f in funcionarios if f['id'] == id_func), None)

    if not funcionario:
        print("Funcionário não encontrado.")
        return

    print("Deixa em branco para manter o valor atual.")
    nome = input(f"Nome ({funcionario['nome']}): ") or funcionario['nome']
    morada = input(f"Morada ({funcionario['morada']}): ") or funcionario['morada']
    telemovel = input(f"Telemóvel ({funcionario['telemovel']}): ") or funcionario['telemovel']
    nif = input(f"NIF ({funcionario['nif']}): ") or funcionario['nif']
    sexo = input(f"Sexo ({funcionario['sexo']}): ") or funcionario['sexo']
    iban = input(f"IBAN ({funcionario['iban']}): ") or funcionario['iban']
    doencas = input(f"Doenças ({funcionario['doencas']}): ") or funcionario['doencas']
    ferias = input(f"Férias ({funcionario['ferias']}): ") or funcionario['ferias']
    salario = input(f"Salário ({funcionario['salario']}): ") or funcionario['salario']
    horario = input(f"Horário ({funcionario['horario']}): ") or funcionario['horario']
    folgas = input(f"Folgas ({funcionario['folgas']}): ") or funcionario['folgas']

    funcionario.update({
        'nome': nome,
        'morada': morada,
        'telemovel': telemovel,
        'nif': nif,
        'sexo': sexo,
        'iban': iban,
        'doencas': doencas,
        'ferias': ferias,
        'salario': salario,
        'horario': horario,
        'folgas': folgas
    })

    with open('data/funcionarios.json', 'w', encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4)
    print("Funcionário atualizado com sucesso.")
    
def remover_funcionario():
    # Lê o arquivo de funcionários
    try:
        with open('data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
        return
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")
        return

    # Solicita o ID do funcionário a ser removido
    id_func = int(input("ID do funcionário a remover: "))

    # Encontra o funcionário com o ID fornecido
    funcionario = next((f for f in funcionarios if f['id'] == id_func), None)

    if not funcionario:
        print("Funcionário não encontrado.")
        return

    # Remove o funcionário
    funcionarios = [f for f in funcionarios if f['id'] != id_func]

    # Atualiza o arquivo de funcionários
    with open('data/funcionarios.json', 'w', encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4)
    
    print(f"Funcionário com ID {id_func} removido com sucesso.")

    
def listar_funcionarios():
    try:
        with open('data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)

        # Verifica se há funcionários para listar
        if funcionarios:
            print("\n == Lista de Funcionários == ")
            for funcionario in funcionarios:
                print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']}")
        else:
            print("Não há funcionários registrados.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")


def criar_departamento():
    nome = input("Nome do novo departamento: ")
    sigla = input("Sigla (ex: INF): ").upper()

    with open('data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    novo_id = max(d['id'] for d in departamentos) + 1 if departamentos else 1
    novo_departamento = {
        "id": novo_id,
        "nome": nome,
        "sigla": sigla
    }

    departamentos.append(novo_departamento)

    with open('data/departamentos.json', 'w', encoding="utf-8") as f:
        json.dump(departamentos, f, indent=4)

    print(f"Departamento '{nome}' criado com sucesso.")

def remover_departamento():
    sigla = input("Sigla do departamento a remover: ").upper()

    with open('data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    novo_lista = [d for d in departamentos if d['sigla'] != sigla]

    if len(novo_lista) == len(departamentos):
        print("Departamento não encontrado.")
    else:
        with open('data/departamentos.json', 'w', encoding="utf-8") as f:
            json.dump(novo_lista, f, indent=4)
        print(f"Departamento com sigla '{sigla}' removido.")

def editar_departamento():
    sigla = input("Sigla do departamento a editar: ").upper()

    with open('data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    for d in departamentos:
        if d['sigla'] == sigla:
            print("Deixa em branco para manter o valor atual.")
            novo_nome = input(f"Novo nome ({d['nome']}): ") or d['nome']
            nova_sigla = input(f"Nova sigla ({d['sigla']}): ").upper() or d['sigla']
            d.update({
                "nome": novo_nome,
                "sigla": nova_sigla
            })

            with open('data/departamentos.json', 'w', encoding="utf-8") as f:
                json.dump(departamentos, f, indent=4)
            print("Departamento atualizado com sucesso.")
            return

    print("Departamento não encontrado.")

def listar_departamentos():
    try:
        with open('data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        # Verifica se há departamentos para listar
        if departamentos:
            i = 0
            print("\n == Lista de Departamentos == ")
            for departamento in departamentos:
                print(f"{i+1} - {departamento['nome']} ({departamento['sigla']})")
                i+=1
        else:
            print("Não há departamentos registrados.")
    except FileNotFoundError:
        print("O arquivo de departamentos não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de departamentos.")