import json
import getpass

def login(funcionarios):
    # Pedir ID de utilizador e função
    print("======== BEM-VINDO AOS RECURSOS-HUMANOS! ========")
    print("LOGIN: ")
    
    # Pedir e validar função
    role = input("Função (admin/gestor/funcionario) ou 'sair' para encerrar: ").lower()
    if role == 'sair':
        print("Programa encerrado.")
        exit()  # Encerra o programa

    if role not in ['admin', 'gestor', 'funcionario']:
        print("Função inválida!")
        return None, None
    
    try:
        user_id = int(input("ID de Utilizador: "))
    except ValueError:
        print("ID inválido!")
        return None, None
    
    # Coloca a role igual ao guardado no arquivo JSON
    if role == 'funcionario': 
        role = "Funcionário"
    elif role == 'gestor':
        role = "Gestor"
    elif role == 'admin':
        role = "Admin"
    
    try:
        # Verificar os utilizadores no arquivo
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
        
        for funcionario in funcionarios:
            if funcionario["id"] == user_id and funcionario["funcao"] == role:
                # Usar getpass para capturar a palavra-passe de forma segura
                password_input = getpass.getpass("Insira a sua palavra-passe: ")
                if funcionario.get('password') == password_input:
                    print(f"Login bem-sucedido! Bem-vindo(a), {funcionario['nome']}.\n")
                    return user_id, role
                else:
                    print("Senha inválida!")
                    return None, None
        else:
            print("Utilizador não encontrado!")
            return None, None  
    except FileNotFoundError:
        print("Ficheiro de utilizadores não encontrado.")
    except json.JSONDecodeError:
        print("Erro ao ler o ficheiro.")
