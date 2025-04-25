import json

class Departamento:
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
        if funcionario_id not in self.funcionarios:
            self.funcionarios.append(funcionario_id)
    
    def remover_funcionario(self, funcionario_id):
        if funcionario_id in self.funcionarios:
            self.funcionarios.remove(funcionario_id)
    
    def listar_funcionarios(self, lista_funcionarios=None):
        print(f"Funcionários do Departamento {self.nome}:")
        if lista_funcionarios:
            for f_id in self.funcionarios:
                f = next((x for x in lista_funcionarios if x["id"] == f_id), None)
                if f:
                    print(f"ID: {f['id']}, Nome: {f['nome']}")
        else:
            for f_id in self.funcionarios:
                print(f"ID: {f_id}")
    
    @staticmethod
    def criar_departamento():
        nome = input("Nome do novo departamento: ")
        sigla = input("Sigla (ex: INF): ").upper()

        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        novo_id = max(d['id'] for d in departamentos) + 1 if departamentos else 1
        novo_departamento = {
            "id": novo_id,
            "nome": nome,
            "sigla": sigla
        }

        departamentos.append(novo_departamento)

        with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
            json.dump(departamentos, f, indent=4)

        print(f"Departamento '{nome}' criado com sucesso.")

    @staticmethod
    def remover_departamento():
        sigla = input("Sigla do departamento a remover: ").upper()

        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        novo_lista = [d for d in departamentos if d['sigla'] != sigla]

        if len(novo_lista) == len(departamentos):
            print("Departamento não encontrado.")
        else:
            with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
                json.dump(novo_lista, f, indent=4)
            print(f"Departamento com sigla '{sigla}' removido.")

    @staticmethod
    def editar_departamento():
        sigla = input("Sigla do departamento a editar: ").upper()

        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
            departamentos = json.load(f)

        for d in departamentos:
            if d['sigla'] == sigla:
                print("Deixa em branco para manter o valor atual.")
                novo_nome = input(f"Novo nome ({d['nome']}): ") or d['nome']
                nova_sigla = input(f"Nova sigla ({d['sigla']}): ").upper() or d['sigla']
                d.update({
                    "nome": novo_nome,
                    "sigla": nova_sigla
                })

                with open('ADC/data/departamentos.json', 'w', encoding="utf-8") as f:
                    json.dump(departamentos, f, indent=4)
                print("Departamento atualizado com sucesso.")
                return

        print("Departamento não encontrado.")

    @staticmethod
    def listar_departamentos():
        try:
            with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as f:
                departamentos = json.load(f)

            # Verifica se há departamentos para listar
            if departamentos:
                i = 0
                print("\n == Lista de Departamentos == ")
                for departamento in departamentos:
                    print(f"{i+1} - {departamento['nome']} ({departamento['sigla']})")
                    i+=1
            else:
                print("Não há departamentos registrados.")
        except FileNotFoundError:
            print("O arquivo de departamentos não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de departamentos.")
