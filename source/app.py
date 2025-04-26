import json
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
    while True:
        funcionarios, departamentos = carregar_dados()
        
        utilizador, papel = login(funcionarios)
        
        if not utilizador:  # Se login falhou
            print("Tentando novamente...")
            continue
        
        # Converte o papel para minúsculas
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
        
        # Perguntar se o utilizador quer voltar ao menu de login ou sair
        opcao = input("Deseja voltar ao menu de login? (s/n): ").strip().lower()
        if opcao != 's':
            print("Programa terminado.")
            break

if __name__ == '__main__':
    main()
