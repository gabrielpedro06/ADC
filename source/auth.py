import json
import getpass

def login(funcionarios):
    """
    Função de autenticação do utilizador.
    Permite o login de utilizadores de acordo com a sua função.
    Se a sua função e o id forem válidos, é pedida a palavra-passe ao utilziador.
    Se a palavra-passe estiver correta o utilizador é autenticado e devolve o id e a função do utilizador para serem mostradas nos menus.
    """
    # Pedir ID de utilizador e função
    print("======== BEM-VINDO AOS RECURSOS-HUMANOS! ========")
    print("LOGIN: ")
    
    # Pedir e validar função
    role = input("Função (admin/gestor/funcionario) ou 'sair' para encerrar: ").lower()
    if role == 'sair':
        print("Programa encerrado.")
        exit()  # Encerra o programa

    if role not in ['admin', 'gestor', 'funcionario']:
        print("Função inválida! Tente novamente.")
        return None, None
    
    try:
        user_id = int(input("ID de Utilizador: "))
    except ValueError:
        print("ID inválido! Tente novamente.")
        return None, None
    
    # Corrigir os nomes das funções para corresponder aos dados no JSON
    role_map = {
        'funcionario': 'Funcionário',
        'gestor': 'Gestor',
        'admin': 'Admin'
    }
    role = role_map.get(role, role)
    
    try:
        # Verificar os utilizadores no arquivo JSON
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios = json.load(f)
        
        for funcionario in funcionarios:
            # Alterar "id" para "_id"
            if funcionario.get("_id") == user_id and funcionario.get("_funcao") == role:
                # Usar getpass para capturar a palavra-passe de forma segura
                password_input = getpass.getpass("Insira a sua palavra-passe: ")
                if funcionario.get('_password') == password_input:
                    print(f"Login bem-sucedido! Bem-vindo(a), {funcionario['_nome']}.\n")
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
