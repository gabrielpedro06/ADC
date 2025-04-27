import json
from getpass import getpass 
from funcionarios import Funcionario

def test_nif_telemovel(valor):
    if len(valor) != 9 or not valor.isdigit():
        raise ValueError("Número inválido! Deve ter exatamente 9 dígitos.")

def test_iban(iban):
    if len(iban) == 21 and iban.isdigit():
        return "PT50" + iban
    else:
        raise ValueError("IBAN inválido! Deve ter 21 dígitos numéricos (sem PT50).")

def test_numbers(valor):
    if not valor.isdigit():
        raise ValueError("Insira um número válido!")

def validar_funcao(funcao):
    opcoes_validas = ["Funcionário", "Gestor", "Admin"]
    if funcao.capitalize() not in opcoes_validas:
        raise ValueError(f"Função inválida! Escolha uma das seguintes: {', '.join(opcoes_validas)}")
    return funcao.capitalize()

def validar_folgas(input_folgas):
    dias_validos = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    folgas = [dia.strip() for dia in input_folgas.split(",")]
    for dia in folgas:
        if dia not in dias_validos:
            raise ValueError(f"Dia de folga inválido: {dia}. Use dias exatamente como: {', '.join(dias_validos)}.")
    return folgas

def validar_horario(horario):
    partes = horario.split(",")
    if len(partes) != 2:
        raise ValueError("Formato de horário inválido! Use o formato 'hora_início,hora_fim' (ex: 10,18).")
    
    inicio, fim = partes

    if not (inicio.isdigit() and fim.isdigit()):
        raise ValueError("As horas devem ser números inteiros.")

    inicio = int(inicio)
    fim = int(fim)

    if not (0 <= inicio <= 23 and 0 <= fim <= 23):
        raise ValueError("As horas devem estar entre 0 e 23.")

    if inicio >= fim:
        raise ValueError("A hora de início deve ser menor que a hora de fim.")

    return f"{inicio}h-{fim}h"

def validar_sexo(sexo):
    sexo = sexo.upper()
    if sexo not in ['M', 'F']:
        raise ValueError("Sexo inválido. Deve ser 'M' ou 'F'.")
    return sexo


def criar_funcionario():
    print("Criar funcionário")

    nome = input("Insira o nome: ")

    while True:
        try:
            funcao = validar_funcao(input("Insira a função (Funcionário/Gestor/Admin): "))
            break
        except ValueError as e:
            print(e)

    morada = input("Insira a morada: ")

    while True:
        try:
            telemovel = input("Insira o telemóvel: ")
            test_nif_telemovel(telemovel)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            nif = input("Insira o NIF: ")
            test_nif_telemovel(nif)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            sexo = input("Insira o sexo (M/F): ")
            validar_sexo(sexo)
            sexo = sexo.upper()
            break
        except ValueError as e:
<<<<<<< HEAD
             print(e)
=======
            print(e)
>>>>>>> ferias_teste


    while True:
        try:
            iban = input("Insira o IBAN (sem PT50): ")
            iban_completo = test_iban(iban)
            break
        except ValueError as e:
            print(e)

    doencas = input("Insira a(s) doença(s) separadas por vírgulas: ")

    while True:
        try:
            ferias = input("Insira o número de dias de férias: ")
            test_numbers(ferias)
            ferias = int(ferias)
            break
        except ValueError as e:
            print(e)

    while True:
        try:
            salario = input("Insira o salário: ")
            test_numbers(salario)
            salario = salario + "€"
            break
        except ValueError as e:
            print(e)

<<<<<<< HEAD
    

=======
>>>>>>> ferias_teste
    while True:
        try:
            horario = input("Insira o horário (formato hora_início,hora_fim, ex: 10,18): ")
            horario = validar_horario(horario)
            break
        except ValueError as e:
<<<<<<< HEAD
         print(e)
             
=======
            print(e)
>>>>>>> ferias_teste

    while True:
        try:
            folgas = validar_folgas(input("Insira os dias de folgas (ex: segunda,domingo): "))
            break
        except ValueError as e:
            print(e)

    password = getpass("Insira a password do funcionário: ")

    with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as arquivo_funcionarios:
        funcionarios = json.load(arquivo_funcionarios)
        id = max(funcionario['_id'] for funcionario in funcionarios) + 1

    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as arquivo_departamentos:
        departamentos = json.load(arquivo_departamentos)
        while True:
            input_sigla = input("Insira a sigla do departamento: ").upper()
            encontrado = next((d for d in departamentos if d['_sigla'] == input_sigla), None)
            if encontrado:
                id_departamento = encontrado['_id']
                break
            else:
                print("Departamento não encontrado! Tente novamente.")

    faltas = {"justificadas": 0, "injustificadas": 0}

    dados = {
        "_id": id,
        "_id_departamento": id_departamento,
        "_funcao": funcao,
        "_nome": nome,
        "_morada": morada,
        "_telemovel": telemovel,
        "_nif": nif,
        "_sexo": sexo,
        "_iban": iban_completo,
        "_doencas": [d.strip() for d in doencas.split(",")],
        "_ferias": ferias,
        "_ferias_status": ferias if ferias > 0 else None,
        "_faltas": faltas,
        "_salario": salario,
        "_horario": horario,
        "_folgas": folgas,
        "_password": password
    }

    funcionario = Funcionario(dados)
    funcionario.colocar_funcionario()
    print(f"Funcionário '{nome}' criado com sucesso.")

    
def editar_funcionario():
    def input_valido(prompt, atual, tipo="str", max_len=None, numero_digitos=None, validar_func=None):
        valor = input(f"{prompt} ({atual}): ").strip()
        if not valor:
            return atual

        try:
            if validar_func:
                return validar_func(valor)
            if tipo == "int":
                test_numbers(valor)
                if numero_digitos:
                    test_nif_telemovel(valor)
                return int(valor)
            if tipo == "float":
                return float(valor)
            if tipo == "str":
                if max_len and len(valor) > max_len:
                    raise ValueError(f"Valor demasiado longo. Máximo {max_len} caracteres.")
                return valor
        except ValueError as e:
            print(e)
            return atual

        return atual

    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
    except FileNotFoundError:
        print("Ficheiro de funcionários não encontrado.")
        return

    try:
        id_func = int(input("ID do funcionário a editar: "))
    except ValueError:
        print("ID inválido.")
        return

    funcionario = next((f for f in funcionarios if f['_id'] == id_func), None)

    if not funcionario:
        print("Funcionário não encontrado.")
        return

    print("Deixa em branco para manter o valor atual.")

<<<<<<< HEAD
    nome = input_valido("Nome", funcionario['nome'], tipo="str", max_len=100)
    morada = input_valido("Morada", funcionario['morada'], tipo="str", max_len=150)
    telemovel = input_valido("Telemóvel", funcionario['telemovel'], tipo="int", numero_digitos=9)
    nif = input_valido("NIF", funcionario['nif'], tipo="int", numero_digitos=9)
    sexo = input_valido("Sexo (M/F)", funcionario['sexo'], validar_func=validar_sexo)
    iban = input_valido("IBAN", funcionario['iban'], validar_func=test_iban)
    doencas = input_valido("Doenças", funcionario['doencas'], tipo="str", max_len=200)
    ferias = input_valido("Férias (dias)", funcionario['ferias'], tipo="int")
    salario = input_valido("Salário", funcionario['salario'], tipo="float")
    horario = input_valido("Horário (ex: 10,18)", funcionario['horario'], validar_func=validar_horario)
    folgas = input_valido("Folgas", funcionario['folgas'], validar_func=validar_folgas)
=======
    nome = input_valido("Nome", funcionario['_nome'], tipo="str", max_len=100)
    morada = input_valido("Morada", funcionario['_morada'], tipo="str", max_len=150)
    telemovel = input_valido("Telemóvel", funcionario['_telemovel'], tipo="int", numero_digitos=9)
    nif = input_valido("NIF", funcionario['_nif'], tipo="int", numero_digitos=9)
    sexo = input_valido("Sexo (M/F)", funcionario['_sexo'], validar_func=validar_sexo)
    iban = input_valido("IBAN", funcionario['_iban'], validar_func=test_iban)
    doencas = input_valido("Doenças", funcionario['_doencas'], tipo="str", max_len=200)
    ferias = input_valido("Férias (dias)", funcionario['_ferias'], tipo="int")
    salario = input_valido("Salário", funcionario['_salario'], tipo="float")
    horario = input_valido("Horário (ex: 10,18)", funcionario['_horario'], validar_func=validar_horario)
    folgas = input_valido("Folgas", funcionario['_folgas'], validar_func=validar_folgas)
    ferias_status = "Em férias" if ferias > 0 else "Sem férias"
>>>>>>> ferias_teste

    funcionario.update({
        '_nome': nome,
        '_morada': morada,
        '_telemovel': str(telemovel),
        '_nif': str(nif),
        '_sexo': sexo,
        '_iban': iban,
        '_doencas': doencas,
        '_ferias': ferias,
        '_ferias_status': ferias_status,  # Atualizar o ferias_status
        '_salario': salario,
        '_horario': horario,
        '_folgas': folgas
    })

    with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
        json.dump(funcionarios, f, indent=4, ensure_ascii=False)

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
    funcionario = next((f for f in funcionarios if f['_id'] == id_func), None)

    if not funcionario:
        print("Funcionário não encontrado.")
        return

    # Remove o funcionário
    funcionarios = [f for f in funcionarios if f['_id'] != id_func]

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
                departamento = next((dep for dep in departamentos if dep['_id'] == funcionario['_id_departamento']), None)
                sigla_departamento = departamento['_sigla'] if departamento else 'Desconhecido'

                print(f"ID: {funcionario['_id']} | Nome: {funcionario['_nome']} ({sigla_departamento})")
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

    novo_id = max(d['_id'] for d in departamentos) + 1 if departamentos else 1
    novo_departamento = {
        "_id": novo_id,
        "_nome": nome,
        "_sigla": sigla,
        "_gestor": None,  # Inicialmente sem gestor
        "_funcionarios": []  # Inicialmente sem funcionarios
    }

    departamentos.append(novo_departamento)

    with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
        json.dump(departamentos, f, indent=4)

    print(f"Departamento '{nome}' criado com sucesso.")
    
    atribuir_gestor_departamento(novo_id)  # Chama a função para ser atribuído um gestor ao departamento criado

def remover_departamento():
    sigla = input("Sigla do departamento a remover: ").upper()

    with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
        departamentos = json.load(f)

    novo_lista = [d for d in departamentos if d['_sigla'] != sigla]

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
        if d['_sigla'] == sigla:
            print("Deixa em branco para manter o valor atual.")
            novo_nome = input(f"Novo nome ({d['_nome']}): ") or d['_nome']
            nova_sigla = input(f"Nova sigla ({d['_sigla']}): ").upper() or d['_sigla']
            d.update({
                "_nome": novo_nome,
                "_sigla": nova_sigla
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
                print(f"{i+1} - {departamento['_nome']} ({departamento['_sigla']})")
                i += 1
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
        funcionarios_departamento = [f for f in funcionarios if f['_id_departamento'] == id_departamento]

        if funcionarios_departamento:
            print("\n == Funcionários do Departamento == ")
            for funcionario in funcionarios_departamento:
                print(f"ID: {funcionario['_id']} | Nome: {funcionario['_nome']}")
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
        funcionario = next((f for f in funcionarios if f['_id'] == id_funcionario), None)

        if funcionario:
            print(f"Funcionário encontrado: {funcionario['_nome']}")
            novo_id_departamento = int(input("Insira o novo ID do departamento: "))
            funcionario['_id_departamento'] = novo_id_departamento

            # Atualiza o arquivo com as mudanças
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios, f, indent=4)
            print(f"Funcionário {funcionario['_nome']} foi atribuído ao departamento com ID {novo_id_departamento}.")
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
        funcionario = next((f for f in funcionarios if f['_id'] == id_funcionario), None)

        if funcionario:
            print(f"Funcionário encontrado: {funcionario['_nome']}")
            funcionario['_id_departamento'] = None  # Remove o funcionário do departamento

            # Atualiza o arquivo com as mudanças
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios, f, indent=4)
            print(f"Funcionário {funcionario['_nome']} removido do departamento.")
        else:
            print("Funcionário não encontrado.")
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")
        
def atribuir_gestor_departamento(id_departamento):
    id_gestor = int(input("Insira o ID do gestor: "))
    
    encontrado = False  # Inicializa a variável 'encontrado'
    nome_funcionario = ""  # Variável para armazenar o nome do funcionário

    try:
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
            
            for funcionario in funcionarios:
                if funcionario['_id'] == id_gestor:
                    if funcionario['_funcao'] != "Gestor":
                        funcionario['_funcao'] = "Gestor"
                        nome_funcionario = funcionario['_nome']  # Guarda o nome do funcionário para uso futuro
                        encontrado = True
                    else:
                        print("O funcionário já é um gestor.")
                        encontrado = True  # Definir como encontrado, mas não fazer alterações.
                
            if not encontrado:
                print("Funcionário não encontrado.")
            
            if encontrado:
                with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                    json.dump(funcionarios, f, indent=4)  # Guarda as alterações no funcionário
                
                with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
                    departamentos = json.load(f)

                    for departamento in departamentos:
                        if departamento['_id'] == id_departamento:
                            departamento['_gestor'] = id_gestor  # Atribui o id do gestor ao departamento
                            departamento_nome = departamento['_nome']  # Guarda o nome do departamento
                            break
                        
                with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
                    json.dump(departamentos, f, indent=4)  # Guarda as alterações no departamento
                    
                print(f"Funcionário {nome_funcionario} promovido a Gestor do departamento {departamento_nome}")
                
    except FileNotFoundError:
        print("O arquivo de funcionários não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo de funcionários.")

def lista_func_semana(id_departamento):
    dias_da_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    disponiveis = {dia: [] for dia in dias_da_semana}

    try:
        # Carregar os funcionários
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)

        # Carregar os departamentos
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        # Encontrar o departamento correspondente
        departamento = next((d for d in departamentos if d['_id'] == id_departamento), None)
        if not departamento:
            print("Departamento não encontrado.")
            return

        # Filtrar os funcionários do departamento
        funcionarios_do_departamento = [
            f for f in funcionarios if f.get('_id_departamento') == id_departamento
        ]

        # Verificar folgas e preencher dias disponíveis
        for funcionario in funcionarios_do_departamento:
            for dia in dias_da_semana:
                # Se o dia não estiver nas folgas do funcionário, ele está disponível
                if dia not in funcionario.get('_folgas', []):
                    disponiveis[dia].append(funcionario['_nome'])

        # Imprimir resultados
        print(f"\n== Disponibilidade dos Funcionários do Departamento {departamento['_nome']} ({departamento['_sigla']} - {departamento['_id']}) ==\n")
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


# ============ Aprovação Ferias ========================

def carregar_funcionarios():
    # Carregar o arquivo de funcionários
    with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
        funcionarios_data = json.load(f)

    # Instanciar objetos Funcionario a partir dos dados carregados
    funcionarios = [Funcionario(func) for func in funcionarios_data]
    return funcionarios

def ferias_func():
    funcionarios = carregar_funcionarios()  # Carregar os funcionários
    print("== Férias de Funcionários por Aprovar ==")

    # Filtra os funcionários com pedidos de férias pendentes
    pendentes = [f for f in funcionarios if f._ferias_status is not None]

    if not pendentes:
        print("Não há pedidos de férias pendentes.")
        return

    for funcionario in pendentes:
        print(f"{funcionario._nome} (ID: {funcionario._id}) pediu {funcionario._ferias_status} dias de férias.")

    aprovacao = input("Para aprovar digite 'aprovar,<id>', para recusar digite 'recusar,<id>': ").strip()

    if aprovacao.startswith("aprovar"):
        _, id_funcionario = aprovacao.split(",")
        id_funcionario = int(id_funcionario)

        funcionario = next((f for f in funcionarios if f._id == id_funcionario), None)

        if funcionario and funcionario._ferias_status is not None:
            # Aprovar férias
            funcionario._ferias -= funcionario._ferias_status
            funcionario._ferias_status = None  # Resetar o status
            print(f"Férias de {funcionario._nome} aprovadas!")

            # Salvar as alterações no arquivo
            funcionarios_data = [f.__dict__ for f in funcionarios]  # Converter objetos de volta para dicionários
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios_data, f, indent=4)

        else:
            print("Funcionário não encontrado ou não tem férias pendentes.")

    elif aprovacao.startswith("recusar"):
        _, id_funcionario = aprovacao.split(",")
        id_funcionario = int(id_funcionario)

        funcionario = next((f for f in funcionarios if f._id == id_funcionario), None)

        if funcionario and funcionario._ferias_status is not None:
            # Recusar férias
            funcionario._ferias_status = None  # Resetar o status
            print(f"Férias de {funcionario._nome} recusadas.")

            # Salvar as alterações no arquivo
            funcionarios_data = [f.__dict__ for f in funcionarios]  # Converter objetos de volta para dicionários
            with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                json.dump(funcionarios_data, f, indent=4)
        else:
            print("Funcionário não encontrado ou não tem férias pendentes.")
    else:
        print("Comando inválido!")


