import json

class Funcionario:
    def __init__(self, dados):
        self.id = dados["id"]
        self.id_departamento = dados["id_departamento"]
        self.funcao = dados["funcao"]
        self.nome = dados["nome"]
        self.morada = dados["morada"]
        self.telemovel = dados["telemovel"]
        self.nif = dados["nif"]
        self.sexo = dados["sexo"]
        self.iban = dados["iban"]
        self.doencas = dados["doencas"]
        self.ferias = dados["ferias"]
        self.faltas = dados["faltas"]
        self.salario = dados["salario"]
        self.horario = dados["horario"]
        self.folgas = dados["folgas"]
        self.password = dados["password"]  # Novo campo para a password

    def __str__(self):
        return f"""Funcionário {self.nome} (ID: {self.id}) - Departamento: {self.id_departamento} - Função {self.funcao}\nMorada: {self.morada} - Telemóvel: {self.telemovel}
NIF: {self.nif} - IBAN: {self.iban} - Salário: {self.salario}€
Sexo: {self.sexo} - Doenças: {self.doencas}
Férias: {self.ferias} dias - Faltas: {self.faltas} - Horário: {self.horario} - Folgas: {self.folgas}
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
    
    @property
    def password(self): return self._password
    @password.setter
    def password(self, value): self._password = value

    # ----------- FUNÇÕES -----------    
    def colocar_funcionario(self):
        try:
            with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
                funcionarios = json.load(f)
        except FileNotFoundError:
            funcionarios = []

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
            "folgas": self._folgas,
            "password": self._password  # Adiciona a password ao objeto
        }
        funcionarios.append(funcionario)

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print("Funcionário adicionado com sucesso!")

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
        
        password_input = input("Alterar palavra-passe (deixe em branco para manter a atual): ")
        if password_input:
            self._password = password_input

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
                    "folgas": self._folgas,
                    "password": self._password  # Atualiza a password
                }
                break

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print("Alterações guardadas com sucesso.")

    def consultar_perfil(self):
        perfil = f"""
        ID: {self._id}
        Departamento: {self._id_departamento}
        Função: {self._funcao}
        Nome: {self._nome}
        Morada: {self._morada}
        Telemóvel: {self._telemovel}
        NIF: {self._nif}
        Sexo: {self._sexo}
        IBAN: {self._iban}
        Doenças: {self._doencas}
        Férias: {self._ferias} dias
        Faltas: Justificadas: {self._faltas['justificadas']} Injustificadas: {self._faltas['injustificadas']}
        Salário: {self._salario}€
        Horário: {self._horario}
        Folgas: {', '.join(self._folgas)}
        """
        print(perfil)

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
