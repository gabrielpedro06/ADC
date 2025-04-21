import json
from funcionarios import Funcionario
from departamentos import Departamento
from auth import login
from menu import menu_admin, menu_funcionario, menu_gestor

def carregar_dados():
    try:
        # Carregar dados dos arquivos JSON
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as arquivo_funcionarios:
            funcionarios = json.load(arquivo_funcionarios)
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as arquivo_departamentos:
            departamentos = json.load(arquivo_departamentos)
        return funcionarios, departamentos
    except FileNotFoundError as e:
        print(f"Erro ao abrir arquivo: {e}")
        return [], []

def salvar_dados(funcionarios, departamentos):
    # Salvar dados de volta aos arquivos JSON
    with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as arquivo_funcionarios:
        json.dump(funcionarios, arquivo_funcionarios, indent=4)
    with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as arquivo_departamentos:
        json.dump(departamentos, arquivo_departamentos, indent=4)

def main():
    funcionarios, departamentos = carregar_dados()
    
    # Efetuar login
    utilizador, papel = login(funcionarios)
    
    # Converte de novo para minúsculas
    if papel == 'Funcionário':
        papel = 'funcionario'
    elif papel == 'Gestor':
        papel = 'gestor'
    elif papel == 'Admin':
        papel = 'admin'
        
    # Chamar o menu correspondente de acordo com o papel
    if papel == 'admin':
        menu_admin()
    elif papel == 'funcionario':
        menu_funcionario(funcionarios, utilizador)
    elif papel == 'gestor':
        menu_gestor(departamentos, funcionarios, utilizador)
    else:
        print("Acesso negado!")

if __name__ == '__main__':
    main()
