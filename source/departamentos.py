class Departamento:
    """
    Classe que representa um departamento dentro de uma empresa.
    A classe tem atributos como id, nome, gestor e uma lista de funcionários.
    Contem 3 métodos, um para atribuir um funcionário ao departamento, outro para remover e outro para listar os funcionários do departamento.
    """
    def __init__(self, dados):
        self.id = dados["id"]
        self.nome = dados["nome"]
        self.gestor = dados["gestor"]
        self.funcionarios = dados.get("funcionarios", [])
        
    def __str__(self):
        return f"Departamento {self.nome} (ID: {self.id})\nGestor: {self.gestor}"
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value
        
    @property
    def gestor(self):
        return self._gestor
    
    @gestor.setter
    def gestor(self, value):
        self._gestor = value
    
    def atribuir_funcionario(self, funcionario_id):
        """
        Atribui um funcionário ao departamento, se ele ainda não estiver atribuido.
        """
        if funcionario_id not in self.funcionarios:
            self.funcionarios.append(funcionario_id)
    
    def remover_funcionario(self, funcionario_id):
        """
        Procura se o funcionário existe no departamento e remove-o se existir.
        """
        if funcionario_id in self.funcionarios:
            self.funcionarios.remove(funcionario_id)
    
    def listar_funcionarios(self, lista_funcionarios=None):
        """
        Lista os funcionários do departamento.
        Se a lista de funcionários for encontrada, imprime os detalhes dos funcionários.
        Caso contrário, imprime apenas os IDs dos funcionários.
        """
        print(f"Funcionários do Departamento {self.nome}:")
        if lista_funcionarios:
            for f_id in self.funcionarios:
                f = next((x for x in lista_funcionarios if x["id"] == f_id), None)
                if f:
                    print(f"ID: {f['id']}, Nome: {f['nome']}")
        else:
            for f_id in self.funcionarios:
                print(f"ID: {f_id}")
