import json
from funcionarios import Funcionario
import os

class Gestor:
    def __init__(self, id, id_departamento, nome, morada, telemovel, nif, sexo, iban, salario, horario, folgas):
        self._id = id
        self._id_departamento = id_departamento
        self._funcao = "Gestor"
        self._nome = nome
        self._morada = morada
        self._telemovel = telemovel
        self._nif = nif
        self._sexo = sexo
        self._iban = iban
        self._doencas = []
        self._ferias = 15
        self._faltas = {"justificadas": 0, "injustificadas": 0}
        self._salario = salario
        self._horario = horario
        self._folgas = folgas

    # Propriedades
    @property
    def id(self): return self._id
    @id.setter
    def id(self, value): self._id = value
    
    @property
    def id_departamento(self): return self._id_departamento
    @id_departamento.setter
    def id_departamento(self, value): self._id_departamento = value
    
    @property
    def funcao(self): return self._funcao
    @funcao.setter
    def funcao(self, value): self._funcao = value
    
    @property
    def nome(self): return self._nome
    @nome.setter
    def nome(self, value): self._nome = value
    
    @property
    def morada(self): return self._morada
    @morada.setter
    def morada(self, value): self._morada = value
    
    @property
    def telemovel(self): return self._telemovel
    @telemovel.setter
    def telemovel(self, value): self._telemovel = value

    @property
    def nif(self): return self._nif
    @nif.setter
    def nif(self, value): self._nif = value
        
    @property
    def sexo(self): return self._sexo
    @sexo.setter
    def sexo(self, value): self._sexo = value
    
    @property
    def iban(self): return self._iban
    @iban.setter
    def iban(self, value): self._iban = value
    
    @property
    def doencas(self): return self._doencas
    @doencas.setter
    def doencas(self, value): self._doencas = value
        
    @property
    def ferias(self): return self._ferias
    @ferias.setter
    def ferias(self, value): self._ferias = value
        
    @property
    def faltas(self): return self._faltas
    @faltas.setter
    def faltas(self, value): self._faltas = value
    
    @property
    def salario(self): return self._salario
    @salario.setter
    def salario(self, value): self._salario = value
    
    @property
    def horario(self): return self._horario
    @horario.setter
    def horario(self, value): self._horario = value
        
    @property
    def folgas(self): return self._folgas
    @folgas.setter
    def folgas(self, value): self._folgas = value

    def to_dict(self):
        return {
            "id": self._id,
            "id_departamento": self._id_departamento,
            "funcao": self._funcao,
            "nome": self._nome,
            "morada": self._morada,
            "telemovel": self._telemovel,
            "nif": self._nif,
            "sexo": self._sexo,
            "iban": self._iban,
            "doencas": self._doencas,
            "ferias": self._ferias,
            "faltas": self._faltas,
            "salario": self._salario,
            "horario": self._horario,
            "folgas": self._folgas
        }

    @staticmethod
    def carregar_gestores():
        if not os.path.exists("gestores.json"):
            return []
        with open("gestores.json", "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_gestores(gestores):
        with open("gestores.json", "w", encoding="utf-8") as f:
            json.dump(gestores, f, ensure_ascii=False, indent=4)

    def guardar(self):
        gestores = Gestor.carregar_gestores()
        gestores.append(self.to_dict())
        Gestor.guardar_gestores(gestores)

    @staticmethod
    def listar():
        gestores = Gestor.carregar_gestores()
        for g in gestores:
            print(f"ID: {g['id']}, Nome: {g['nome']}, Departamento: {g['id_departamento']}")

    @staticmethod
    def editar(id, campo, novo_valor):
        gestores = Gestor.carregar_gestores()
        for gestor in gestores:
            if gestor["id"] == id:
                if campo in gestor:
                    gestor[campo] = novo_valor
                    Gestor.guardar_gestores(gestores)
                    print("Gestor atualizado com sucesso.")
                    return
                else:
                    print("Campo inválido.")
                    return
        print("Gestor não encontrado.")

    @staticmethod
    def consultar_por_id(id):
        gestores = Gestor.carregar_gestores()
        for gestor in gestores:
            if gestor["id"] == id:
                return gestor
        return None

    @staticmethod
    def consultar_funcionarios_departamento(departamento_id):
        """Consulta todos os funcionários de um determinado departamento."""
        funcionarios = Funcionario.carregar_funcionarios()  # Assumindo que tens uma classe Funcionario
        funcionarios_departamento = []
        for funcionario in funcionarios:
            if funcionario["id_departamento"] == departamento_id:
                funcionarios_departamento.append(funcionario)
        return funcionarios_departamento

    @staticmethod
    def atribuir_funcionario_departamento(funcionario_id, novo_departamento_id):
        """Atribui um funcionário a um novo departamento."""
        funcionarios = Funcionario.carregar_funcionarios()  # Assumindo que tens uma classe Funcionario
        for funcionario in funcionarios:
            if funcionario["id"] == funcionario_id:
                funcionario["id_departamento"] = novo_departamento_id
                Funcionario.guardar_funcionarios(funcionarios)  # Assumindo que tens um método guardar na classe Funcionario
                print(f"Funcionário {funcionario['nome']} atribuído ao departamento {novo_departamento_id}.")
                return
        print("Funcionário não encontrado.")

    @staticmethod
    def remover_funcionario_departamento(funcionario_id):
        """Remove um funcionário de um departamento, deixando o campo 'id_departamento' vazio."""
        funcionarios = Funcionario.carregar_funcionarios()  # Assumindo que tens uma classe Funcionario
        for funcionario in funcionarios:
            if funcionario["id"] == funcionario_id:
                funcionario["id_departamento"] = None
                Funcionario.guardar_funcionarios(funcionarios)  # Assumindo que tens um método guardar na classe Funcionario
                print(f"Funcionário {funcionario['nome']} removido do departamento.")
                return
        print("Funcionário não encontrado.")
