class Departamento:
    def __init__(self, dados):
        self.id = dados["id"]
        self.nome = dados["nome"]
        self.gestor = dados["gestor"]
        self.funcionarios = dados["funcionarios"]
    
    def atribuir_funcionario(self, funcionario):
        # Atribuir um funcionário ao departamento
        self.funcionarios.append(funcionario)
    
    def remover_funcionario(self, funcionario_id):
        # Remover um funcionário do departamento
        self.funcionarios = [f for f in self.funcionarios if f["id"] != funcionario_id]
    
    def listar_funcionarios(self):
        # Listar todos os funcionários do departamento
        print(f"Funcionários do Departamento {self.nome}:")
        for f in self.funcionarios:
            print(f"ID: {f['id']}, Nome: {f['nome']}")
