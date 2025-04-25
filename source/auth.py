def login(funcionarios, gestores, admins):
    print("Login")
    role = input("Função (admin/gestor/funcionario): ").lower()
    
    if role not in ['admin', 'gestor', 'funcionario']:
        print("Função inválida!")
        return None, None

    try:
        user_id = int(input("ID de Utilizador: "))
    except ValueError:
        print("ID inválido!")
        return None, None

    # Carregar a lista certa com base na função
    if role == 'funcionario':
        lista_utilizadores = funcionarios
        role_nome = "funcionario"  # Alterado para minúsculas
    elif role == 'gestor':
        lista_utilizadores = gestores
        role_nome = "gestor"  # Alterado para minúsculas
    elif role == 'admin':
        lista_utilizadores = admins
        role_nome = "admin"  # Alterado para minúsculas

    for utilizador in lista_utilizadores:
        # Comparar a função e o ID de utilizador de forma consistente
        if utilizador["id"] == user_id and utilizador["funcao"].lower() == role_nome:
            return user_id, role
    else:
        print("Utilizador não encontrado!")
        return None, None
