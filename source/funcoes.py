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
    
    salario = input("Insira o salário: ")
    test_numbers(salario)
    
    horario = input("Insira o horário (inicioH - fimH): ")
    folgas = input("Insira os dias de folgas (separados por vírgula): ")
    
    with open('data/funcionarios.json', 'r') as arquivo_funcionarios:
        funcionarios = json.load(arquivo_funcionarios)
        id = max(funcionario['id'] for funcionario in funcionarios) + 1
    
    with open('data/departamentos.json', 'r') as arquivo_departamentos:
        departamentos = json.load(arquivo_departamentos)
        input_sigla = input("Insira a sigla do departamento: ")
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