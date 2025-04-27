import json
from auth import login
from menu import menu_admin, menu_funcionario, menu_gestor

def carregar_dados():
    """
    Carrega os dados dos arquivos JSOn de funcionarios e departamentos.
    Caso o ficheiro seja encontrado, devolve os dados e caso não seja encontrado, devolve duas listas vazias.
    """
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

def main():
    """
    Função principal que inicia o programa e gerencia o fluxo dos logins e dos menus.
    O utilizador pode fazer login como admin, gestor ou funcionario e dependedo do seu papel é chamado o menu correspondente.
    O utilizador pode sair do programa ou voltar ao menu de login.
    Se o login não for bem-sucedido, o programa irá tentar novamente até que o utilizador faça login corretamente ou saia do programa.
    """
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
