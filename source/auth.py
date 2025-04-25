def login(funcionarios):
    # Pedir ID de utilizador e função
    print("Login")
    print("Utilizadores disponíveis:")
    print("1 - Funcionário")
    print("2 - Gestor")
    print("3 - Administrador")
    
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
        
    # Procurar o utilizador com o ID
    for funcionario in funcionarios:
        if funcionario["id"] == user_id and funcionario["funcao"] == role:
            return user_id, role
    else:
        print("Utilizador não encontrado!")
        return None, None
