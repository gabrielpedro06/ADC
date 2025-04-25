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
    funcao = input("Insira a função (Funcionário/Gestor/Admin): ")
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
    
    with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as arquivo_funcionarios:
        funcionarios = json.load(arquivo_funcionarios)
        id = max(funcionario['id'] for funcionario in funcionarios) + 1
    
    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as arquivo_departamentos:
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
    dados = [id, id_departamento, funcao, nome, morada, telemovel, nif, sexo, iban_completo, doencas, ferias, faltas, salario, horario, folgas]
    funcionario = Funcionario(dados)
    funcionario.colocar_funcionario()
    funcionario.__str__()
    
def editar_funcionario():
    with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
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

    with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4)
    print("Funcionário atualizado com sucesso.")
    
def remover_funcionario():
    # Lê o arquivo de funcionários
    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
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
    with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4)
    
    print(f"Funcionário com ID {id_func} removido com sucesso.")

    
def listar_funcionarios():
    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)

        # Carregar os departamentos para obter as siglas
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        # Verifica se há funcionários para listar
        if funcionarios:
            print("\n == Lista de Funcionários == ")
            for funcionario in funcionarios:
                # Encontrar o departamento do funcionário e pegar a sigla
                departamento = next((dep for dep in departamentos if dep['id'] == funcionario['id_departamento']), None)
                sigla_departamento = departamento['sigla'] if departamento else 'Desconhecido'

                print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']} ({sigla_departamento})")
        else:
            print("Não há funcionários registrados.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")


def criar_departamento():
    nome = input("Nome do novo departamento: ")
    sigla = input("Sigla (ex: INF): ").upper()

    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    novo_id = max(d['id'] for d in departamentos) + 1 if departamentos else 1
    novo_departamento = {
        "id": novo_id,
        "nome": nome,
        "sigla": sigla
    }

    departamentos.append(novo_departamento)

    with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
        json.dump(departamentos, f, indent=4)

    print(f"Departamento '{nome}' criado com sucesso.")

def remover_departamento():
    sigla = input("Sigla do departamento a remover: ").upper()

    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    novo_lista = [d for d in departamentos if d['sigla'] != sigla]

    if len(novo_lista) == len(departamentos):
        print("Departamento não encontrado.")
    else:
        with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
            json.dump(novo_lista, f, indent=4)
        print(f"Departamento com sigla '{sigla}' removido.")

def editar_departamento():
    sigla = input("Sigla do departamento a editar: ").upper()

    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
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

            with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
                json.dump(departamentos, f, indent=4)
            print("Departamento atualizado com sucesso.")
            return

    print("Departamento não encontrado.")

def listar_departamentos():
    try:
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
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
        
#Funções Gestores

def consultar_funcionarios_departamento(id_departamento):
    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
        
        # Filtra os funcionários do departamento
        funcionarios_departamento = [f for f in funcionarios if f['id_departamento'] == id_departamento]

        if funcionarios_departamento:
            print("\n == Funcionários do Departamento == ")
            for funcionario in funcionarios_departamento:
                print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']}")
        else:
            print("Nenhum funcionário encontrado para este departamento.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")

def atribuir_funcionario_departamento():
    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
        
        id_funcionario = int(input("Insira o ID do funcionário: "))
        funcionario = next((f for f in funcionarios if f['id'] == id_funcionario), None)

        if funcionario:
            print(f"Funcionário encontrado: {funcionario['nome']}")
            novo_id_departamento = int(input("Insira o novo ID do departamento: "))
            funcionario['id_departamento'] = novo_id_departamento

            # Atualiza o arquivo com as mudanças
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios, f, indent=4)
            print(f"Funcionário {funcionario['nome']} foi atribuído ao departamento com ID {novo_id_departamento}.")
        else:
            print("Funcionário não encontrado.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")

def remover_funcionario_departamento():
    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
        
        id_funcionario = int(input("Insira o ID do funcionário a ser removido do departamento: "))
        funcionario = next((f for f in funcionarios if f['id'] == id_funcionario), None)

        if funcionario:
            print(f"Funcionário encontrado: {funcionario['nome']}")
            funcionario['id_departamento'] = None  # Remove o funcionário do departamento

            # Atualiza o arquivo com as mudanças
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios, f, indent=4)
            print(f"Funcionário {funcionario['nome']} removido do departamento.")
        else:
            print("Funcionário não encontrado.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")
        
def lista_func_semana(id_departamento):
    dias_da_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
    disponiveis = {dia: [] for dia in dias_da_semana}

    try:
        # Carregar os funcionários
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)

        # Carregar os departamentos
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        # Encontrar o departamento correspondente
        departamento = next((d for d in departamentos if d['id'] == id_departamento), None)
        if not departamento:
            print("Departamento não encontrado.")
            return

        # Filtrar os funcionários do departamento
        funcionarios_do_departamento = [
            f for f in funcionarios if f['id_departamento'] == id_departamento
        ]

        # Verificar folgas e preencher dias disponíveis
        for funcionario in funcionarios_do_departamento:
            for dia in dias_da_semana:
                if dia not in funcionario['folgas']:
                    disponiveis[dia].append(funcionario['nome'])

        # Imprimir resultados
        print(f"\n== Disponibilidade dos Funcionários do Departamento {departamento['nome']} ({departamento['sigla']} - {departamento['id']}) ==\n")
        for dia, nomes in disponiveis.items():
            print(f"{dia}:")
            if nomes:
                for nome in nomes:
                    print(f"  {nome}")
            else:
                print("  Nenhum funcionário disponível.")

    except FileNotFoundError:
        print("O arquivo de dados não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler os arquivos de dados.")



