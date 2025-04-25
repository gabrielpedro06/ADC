import json
import os
from funcionarios import Funcionario
from departamentos import Departamento
from gestor import Gestor

class Admin:
    def __init__(self, id, nome, morada, telemovel, nif, sexo, iban, salario, horario, folgas):
        self._id = id
        self._id_departamento = 0  # O administrador não pertence a um departamento específico
        self._funcao = "Admin"
        self._nome = nome
        self._morada = morada
        self._telemovel = telemovel
        self._nif = nif
        self._sexo = sexo
        self._iban = iban
        self._doencas = []
        self._ferias = 12
        self._faltas = {"justificadas": 1, "injustificadas": 0}
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
    def carregar_admins():
        if not os.path.exists("admins.json"):
            return []
        with open("admins.json", "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def guardar_admins(admins):
        with open("admins.json", "w", encoding="utf-8") as f:
            json.dump(admins, f, ensure_ascii=False, indent=4)

    def guardar(self):
        admins = Admin.carregar_admins()
        admins.append(self.to_dict())
        Admin.guardar_admins(admins)

    @staticmethod
    def listar():
        admins = Admin.carregar_admins()
        for a in admins:
            print(f"ID: {a['id']}, Nome: {a['nome']}")

    @staticmethod
    def editar(id, campo, novo_valor):
        admins = Admin.carregar_admins()
        for admin in admins:
            if admin["id"] == id:
                if campo in admin:
                    admin[campo] = novo_valor
                    Admin.guardar_admins(admins)
                    print("Admin atualizado com sucesso.")
                    return
                else:
                    print("Campo inválido.")
                    return
        print("Admin não encontrado.")

    @staticmethod
    def consultar_por_id(id):
        admins = Admin.carregar_admins()
        for admin in admins:
            if admin["id"] == id:
                return admin
        return None

    # Funcionalidade: Criar, editar e remover funcionários
    @staticmethod
    def gerir_funcionarios(acao, funcionario_data=None):
        funcionarios = Funcionario.carregar_funcionarios()  # Supondo que tens uma classe Funcionario já implementada

        if acao == "criar" and funcionario_data:
            funcionario = Funcionario(**funcionario_data)
            funcionario.guardar()
            print("Funcionário criado com sucesso.")
        
        elif acao == "editar" and funcionario_data:
            id = funcionario_data.get("id")
            campo = funcionario_data.get("campo")
            novo_valor = funcionario_data.get("novo_valor")
            Funcionario.editar(id, campo, novo_valor)
        
        elif acao == "remover" and funcionario_data:
            id = funcionario_data.get("id")
            Funcionario.remover(id)
        
        else:
            print("Ação inválida ou dados insuficientes.")

    # Funcionalidade: Criar, editar e remover departamentos
    @staticmethod
    def gerir_departamentos(acao, departamento_data=None):
        departamentos = Departamento.carregar_departamentos()  # Supondo que tens uma classe Departamento já implementada

        if acao == "criar" and departamento_data:
            departamento = Departamento(**departamento_data)
            departamento.guardar()
            print("Departamento criado com sucesso.")
        
        elif acao == "editar" and departamento_data:
            id = departamento_data.get("id")
            campo = departamento_data.get("campo")
            novo_valor = departamento_data.get("novo_valor")
            Departamento.editar(id, campo, novo_valor)
        
        elif acao == "remover" and departamento_data:
            id = departamento_data.get("id")
            Departamento.remover(id)
        
        else:
            print("Ação inválida ou dados insuficientes.")

    # Funcionalidade: Criar, editar e remover gestores
    @staticmethod
    def gerir_gestores(acao, gestor_data=None):
        gestores = Gestor.carregar_gestores()  # Supondo que tens uma classe Gestor já implementada

        if acao == "criar" and gestor_data:
            gestor = Gestor(**gestor_data)
            gestor.guardar()
            print("Gestor criado com sucesso.")
        
        elif acao == "editar" and gestor_data:
            id = gestor_data.get("id")
            campo = gestor_data.get("campo")
            novo_valor = gestor_data.get("novo_valor")
            Gestor.editar(id, campo, novo_valor)
        
        elif acao == "remover" and gestor_data:
            id = gestor_data.get("id")
            Gestor.remover(id)
        
        else:
            print("Ação inválida ou dados insuficientes.")

    @staticmethod
    def permissao_acesso():
        # Como administrador, tem acesso total às informações
        print("Permissões de acesso: Total")

    @staticmethod
    def conta_admin_pre_criada():
        admins = Admin.carregar_admins()
        if not admins:  # Se não houver nenhum admin, cria um admin inicial
            admin = Admin(
                id=1,
                nome="Pedro Almeida",
                morada="Rua W, 789",
                telemovel="914567890",
                nif="123987456",
                sexo="Masculino",
                iban="PT50000201231234567890123",
                salario=2500,
                horario="9h-18h",
                folgas=["Sábado", "Domingo"]
            )
            # Dados adicionais de doenças, férias, faltas
            admin._doencas = ["Dor de cabeça"]
            admin._ferias = 12
            admin._faltas = {"justificadas": 1, "injustificadas": 0}
            
            # Salvar o administrador com todos os dados preenchidos
            admin.guardar()
            print("Conta de administrador pré-criada com sucesso.")

