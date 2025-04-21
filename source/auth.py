def login(funcionarios):
    # Pedir ID de utilizador e função
    print("Login")
    try:
        user_id = int(input("ID de Utilizador: "))
    except ValueError:
        print("ID inválido!")
        return None, None
    
    # Procurar o utilizador com o ID
    user = next((f for f in funcionarios if f["id"] == user_id), None)
    
    if not user:
        print("Utilizador não encontrado.")
        return None, None
    
    # Pedir e validar função
    role = input("Função (admin/gestor/funcionario): ").lower()
    if role not in ['admin', 'gestor', 'funcionario']:
        print("Função inválida!")
        return None, None

    return user, role
