import json
class Funcionario:
    def __init__(self, dados):
        self._id = dados[0]
        self._id_departamento = dados[1]
        self._funcao = dados[2]
        self._nome = dados[3]
        self._morada = dados[4]
        self._telemovel = dados[5]
        self._nif = dados[6]
        self._sexo = dados[7]
        self._iban = dados[8]
        self._doencas = dados[9]
        self._ferias = dados[10]
        self._faltas = dados[11]
        self._salario = dados[12]
        self._horario = dados[13]
        self._folgas = dados[14]
    
    def __str__(self):
        return f"""Funcionário {self._nome} (ID: {self._id}) - Departamento: {self._id_departamento} - Função {self._funcao}\nMorada: {self._morada} - Telemóvel: {self._telemovel}
NIF: {self._nif} - IBAN: {self._iban} - Salário: {self._salario}€
Sexo: {self._sexo} - Doenças: {self._doencas}
Férias: {self._ferias} dias - Faltas: {self._faltas} - Horário: {self._horario} - Folgas: {self._folgas}
"""

# ----------- GETTERS E SETTERS -----------    
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

# ----------- FUNÇÕES -----------    
    def test_nif_telemovel(self, input):
        if len(input) != 9 or not input.isdigit():
            raise ValueError("Número inválido!")

    def test_iban(self, input):
        if len(input) == 21 and input.isdigit():
            return "PT50" + input
        else:
            raise ValueError("IBAN inválido!")

    def test_numbers(self, input):
        if not input.isdigit():
            raise ValueError("Insira um número!")

    def criar_funcionario(self):
        print("Criar funcionário")
        # Criar novo funcionário
        
        nome = input("Insira o nome: ")
        funcao = input("Insira a função (Funcionário/Gestor/Admin): ")
        morada = input("Insira a morada: ")
        telemovel = input("Insira o telemóvel: ")
        self.test_nif_telemovel(telemovel)
            
        nif = input("Insira o NIF: ")
        self.test_nif_telemovel(nif)
            
        sexo = input("Insira o sexo: ")
        iban = input("Insira o IBAN (sem PT50): ")
        iban_completo = self.test_iban(iban)
            
        doencas = input("Insira a(s) doença(s) separadas por vírgulas: ")
        
        ferias = input("Insira o número de dias de férias: ")
        self.test_numbers(ferias)
        ferias = int(ferias)
        
        salario = input("Insira o salário: ")
        self.test_numbers(salario)
        salario = salario + "€"
        
        horario = input("Insira o horário (inicioH - fimH): ")
        folgas = input("Insira os dias de folgas (separados por vírgula): ")
        
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as arquivo_funcionarios:
            funcionarios = json.load(arquivo_funcionarios)
            id = max(funcionario['id'] for funcionario in funcionarios) + 1
        
        with open('ADC/data/departamentos.json', 'r', encoding="utf-8") as arquivo_departamentos:
            departamentos = json.load(arquivo_departamentos)
            input_sigla = input("Insira a sigla do departamento: ").upper()
            id_departamento = 0
            found = False
            for departamento in departamentos:
                if input_sigla.upper() == departamento['sigla']:
                    id_departamento = departamento['id']
                    found = True
                    
            if not found:
                print("Departamento não encontrado!")
                
        faltas = {"justificadas": 0, "injustificadas": 0}
        dados = [id, id_departamento, funcao, nome, morada, telemovel, nif, sexo, iban_completo, doencas, ferias, faltas, salario, horario, folgas]
        funcionario = Funcionario(dados)
        funcionario.colocar_funcionario()
        print(funcionario)
        
    def editar_funcionario(self):
        # Determine qual ficheiro usar de acordo com a função
        if self._funcao == "Funcionario":
            file_path = 'ADC/data/funcionarios.json'
        elif self._funcao == "Gestor":
            file_path = 'ADC/data/gestor.json'
        elif self._funcao == "Admin":
            file_path = 'ADC/data/admin.json'

        try:
            with open(file_path, 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)
        except FileNotFoundError:
            print(f"O arquivo de {self._funcao}s não foi encontrado.")
            return

        id_func = int(input("ID do funcionário a editar: "))
        funcionario = next((f for f in funcionarios if f['id'] == id_func), None)

        if not funcionario:
            print("Funcionário não encontrado.")
            return

        print("Deixa em branco para manter o valor atual.")
        nome = input(f"Nome ({funcionario['nome']}): ") or funcionario['nome']
        morada = input(f"Morada ({funcionario['morada']}): ") or funcionario['morada']
        telemovel = input(f"Telemóvel ({funcionario['telemovel']}): ") or funcionario['telemovel']
        nif = input(f"NIF ({funcionario['nif']}): ") or funcionario['nif']
        sexo = input(f"Sexo ({funcionario['sexo']}): ") or funcionario['sexo']
        iban = input(f"IBAN ({funcionario['iban']}): ") or funcionario['iban']
        doencas = input(f"Doenças ({funcionario['doencas']}): ") or funcionario['doencas']
        ferias = input(f"Férias ({funcionario['ferias']}): ") or funcionario['ferias']
        salario = input(f"Salário ({funcionario['salario']}): ") or funcionario['salario']
        horario = input(f"Horário ({funcionario['horario']}): ") or funcionario['horario']
        folgas = input(f"Folgas ({funcionario['folgas']}): ") or funcionario['folgas']

        funcionario.update({
            'nome': nome,
            'morada': morada,
            'telemovel': telemovel,
            'nif': nif,
            'sexo': sexo,
            'iban': iban,
            'doencas': doencas,
            'ferias': ferias,
            'salario': salario,
            'horario': horario,
            'folgas': folgas
        })

        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)
        print(f"{self._funcao} atualizado com sucesso.")

        
    def remover_funcionario(self):
        # Lê o arquivo de funcionários
        try:
            with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)
        except FileNotFoundError:
            print("O arquivo de funcionários não foi encontrado.")
            return
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de funcionários.")
            return

        # Solicita o ID do funcionário a ser removido
        id_func = int(input("ID do funcionário a remover: "))

        # Encontra o funcionário com o ID fornecido
        funcionario = next((f for f in funcionarios if f['id'] == id_func), None)

        if not funcionario:
            print("Funcionário não encontrado.")
            return

        # Remove o funcionário
        funcionarios = [f for f in funcionarios if f['id'] != id_func]

        # Atualiza o arquivo de funcionários
        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)
        
        print(f"Funcionário com ID {id_func} removido com sucesso.")

    def listar_funcionarios():
        try:
            with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)

            # Verifica se há funcionários para listar
            if funcionarios:
                print("\n == Lista de Funcionários == ")
                for funcionario in funcionarios:
                    print(f"ID: {funcionario['id']} | Nome: {funcionario['nome']}")
            else:
                print("Não há funcionários registrados.")
        except FileNotFoundError:
            print("O arquivo de funcionários não foi encontrado.")
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de funcionários.")
    
    def colocar_funcionario(self):
        try:
            # Abrir o ficheiro de funcionários para garantir que se inicia com dados válidos
            if self._funcao == "Funcionario":
                with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                    funcionarios = json.load(f)
            elif self._funcao == "Gestor":
                with open('ADC/data/gestor.json', 'r', encoding="utf-8") as f:
                    funcionarios = json.load(f)
            elif self._funcao == "Admin":
                with open('ADC/data/admin.json', 'r', encoding="utf-8") as f:
                    funcionarios = json.load(f)
        except FileNotFoundError:
            funcionarios = []  # Se o ficheiro não for encontrado, começa com uma lista vazia

        # Criar um dicionário com os dados do funcionário
        funcionario = {
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

        funcionarios.append(funcionario)

        # Definir o ficheiro correto de acordo com a função
        if self._funcao == "Funcionario":
            file_path = 'ADC/data/funcionarios.json'
        elif self._funcao == "Gestor":
            file_path = 'ADC/data/gestor.json'
        elif self._funcao == "Admin":
            file_path = 'ADC/data/admin.json'

        # Gravar o novo funcionário no ficheiro correspondente
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print(f"{self._funcao} adicionado com sucesso!")


    def editar_dados(self):
        print("Editar Dados Pessoais")
        
        self._funcao = input(f"Função (atual: {self._funcao}): ") or self._funcao
        self._nome = input(f"Nome (atual: {self._nome}): ") or self._nome
        self._morada = input(f"Morada (atual: {self._morada}): ") or self._morada
        self._telemovel = input(f"Telemóvel (atual: {self._telemovel}): ") or self._telemovel
        self._nif = input(f"NIF (atual: {self._nif}): ") or self._nif
        self._sexo = input(f"Sexo (atual: {self._sexo}): ") or self._sexo
        self._iban = input(f"IBAN (atual: {self._iban}): ") or self._iban
        self._doencas = input(f"Doenças (atual: {self._doencas}): ") or self._doencas

        try:
            ferias_input = input(f"Férias (atual: {self._ferias}): ")
            self._ferias = int(ferias_input) if ferias_input else self._ferias
        except ValueError:
            print("Valor inválido para férias. Mantido valor anterior.")
        
        try:
            justificadas = input(f"Faltas justificadas (atual: {self._faltas['justificadas']}): ")
            injustificadas = input(f"Faltas injustificadas (atual: {self._faltas['injustificadas']}): ")
            self._faltas = {
                "justificadas": int(justificadas) if justificadas else self._faltas['justificadas'],
                "injustificadas": int(injustificadas) if injustificadas else self._faltas['injustificadas']
            }
        except ValueError:
            print("Valor inválido para faltas. Mantido valor anterior.")

        try:
            salario_input = input(f"Salário (atual: {self._salario}): ")
            self._salario = int(salario_input) if salario_input else self._salario
        except ValueError:
            print("Valor inválido para salário. Mantido valor anterior.")
        
        self._horario = input(f"Horário (atual: {self._horario}): ") or self._horario

        folgas_input = input(f"Folgas (atual: {', '.join(self._folgas)} - separa por vírgulas): ")
        if folgas_input:
            self._folgas = [f.strip().capitalize() for f in folgas_input.split(",") if f.strip()]
        
        self.guardar_alteracoes()


    def guardar_alteracoes(self):
        try:
            with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)
        except FileNotFoundError:
            print("Ficheiro de funcionários não encontrado.")
            return

        for i, f in enumerate(funcionarios):
            if f["id"] == self._id:
                funcionarios[i] = {
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
                break

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print("Alterações guardadas com sucesso.")


    def consultar_ferias(self):
        print(f"Férias disponíveis: {self._ferias} dias")

    def consultar_faltas(self):
        print(f"Faltas justificadas: {self._faltas['justificadas']}, Injustificadas: {self._faltas['injustificadas']}")
    
    def consultar_salario(self):
        print(f"Salário: {self._salario}€")
    
    def consultar_folgas(self):
        print(f"Folgas: {', '.join(self._folgas)}")

    def pedir_ferias(self, dias):
        if dias <= self._ferias:
            self._ferias -= dias
            print(f"{dias} dias de férias aprovados. Férias restantes: {self._ferias}")
        else:
            print("Não tem dias suficientes de férias.")

    def registar_falta(self, justificada=True):
        tipo = "justificadas" if justificada else "injustificadas"
        self._faltas[tipo] += 1
        print(f"Falta {tipo[:-1]} registada com sucesso.")

    def atualizar_horario(self, novo_horario):
        self._horario = novo_horario
        print(f"Horário atualizado para: {self._horario}")

    def aumentar_salario(self, valor):
        self._salario += valor
        print(f"Novo salário: {self._salario}€")

    def atribuir_folga(self, dia):
        self._folgas.append(dia)
        print(f"Folga atribuída: {dia}")

    def remover_funcionario(self):
        try:
            with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)
        except FileNotFoundError:
            print("Ficheiro não encontrado.")
            return

        funcionarios = [f for f in funcionarios if f["id"] != self._id]

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print(f"Funcionário {self._id} removido com sucesso.")
