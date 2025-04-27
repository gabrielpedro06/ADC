import json

class Funcionario:
    def __init__(self, dados):
        self._id = dados["_id"]
        self._id_departamento = dados["_id_departamento"]
        self._funcao = dados["_funcao"]
        self._nome = dados["_nome"]
        self._morada = dados["_morada"]
        self._telemovel = dados["_telemovel"]
        self._nif = dados["_nif"]
        self._sexo = dados["_sexo"]
        self._iban = dados["_iban"]
        self._doencas = dados["_doencas"]
        self._ferias = dados["_ferias"]
        self._ferias_status = dados.get("_ferias_status", None)
        self._faltas = dados["_faltas"]
        self._salario = dados["_salario"]
        self._horario = dados["_horario"]
        self._folgas = dados["_folgas"]
        self._password = dados["_password"]

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
    def ferias_status(self): return self._ferias_status
    @ferias_status.setter
    def ferias_status(self, value): self._ferias_status = value
        
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
            "_id": self._id,
            "_id_departamento": self._id_departamento,
            "_funcao": self._funcao,
            "_nome": self._nome,
            "_morada": self._morada,
            "_telemovel": self._telemovel,
            "_nif": self._nif,
            "_sexo": self._sexo, 
            "_iban": self._iban,
            "_doencas": self._doencas,
            "_ferias": self._ferias,
            "_ferias_status": self._ferias_status,  # Adiciona o atributo ferias_status
            "_faltas": self._faltas,
            "_salario": self._salario,
            "_horario": self._horario,
            "_folgas": self._folgas,
            "_password": self._password  # Adiciona a password ao objeto
        }
        funcionarios.append(funcionario)

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print("Funcionário adicionado com sucesso!")

    def editar_dados(self):
        print("Editar Dados Pessoais")
        
        self._nome = input(f"Nome (atual: {self._nome}): ") or self._nome
        self._morada = input(f"Morada (atual: {self._morada}): ") or self._morada
        self._telemovel = input(f"Telemóvel (atual: {self._telemovel}): ") or self._telemovel
        self._nif = input(f"NIF (atual: {self._nif}): ") or self._nif
        self._sexo = input(f"Sexo (atual: {self._sexo}): ") or self._sexo
        self._iban = input(f"IBAN (atual: {self._iban}): ") or self._iban
        self._doencas = input(f"Doenças (atual: {self._doencas}): ") or self._doencas
        
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
            if f["_id"] == self._id:
                funcionarios[i] = {
                    "_id": self._id,
                    "_id_departamento": self._id_departamento,
                    "_funcao": self._funcao,
                    "_nome": self._nome,
                    "_morada": self._morada,
                    "_telemovel": self._telemovel,
                    "_nif": self._nif,
                    "_sexo": self._sexo,
                    "_iban": self._iban,
                    "_doencas": self._doencas,
                    "_ferias": self._ferias,
                    "_ferias_status": self._ferias_status,  # Atualiza o status das férias
                    "_faltas": self._faltas,
                    "_salario": self._salario,
                    "_horario": self._horario,
                    "_folgas": self._folgas,
                    "_password": self._password
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
        Férias em Aprovação: {self._ferias_status} dias
        Faltas: Justificadas: {self._faltas['justificadas']} Injustificadas: {self._faltas['injustificadas']}
        Salário: {self._salario}€
        Horário: {self._horario}
        Folgas: {', '.join(self._folgas)}
        """
        print(perfil)

    def consultar_ferias(self):
        status_ferias = self._ferias_status if self._ferias_status else "Não solicitado"
        print(f"Férias disponíveis: {self._ferias} dias. Por Aprovação: {status_ferias}")

    def consultar_faltas(self):
        print(f"Faltas justificadas: {self._faltas['justificadas']}, Injustificadas: {self._faltas['injustificadas']}")
    
    def consultar_salario(self):
        print(f"Salário: {self._salario}€")
    
    def consultar_folgas(self):
        print(f"Folgas: {', '.join(self._folgas)}")

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

        funcionarios = [f for f in funcionarios if f["_id"] != self._id]

        with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
            json.dump(funcionarios, f, indent=4)

        print(f"Funcionário {self._id} removido com sucesso.")

    def carregar_funcionarios(self):
        # Carregar o arquivo de funcionários
        with open('ADC/data/funcionarios.json', 'r', encoding="utf-8") as f:
            funcionarios_data = json.load(f)
        
        # Criar uma lista de instâncias de Funcionario a partir dos dados
        funcionarios = [Funcionario(func) for func in funcionarios_data]
        
        return funcionarios


    def pedir_ferias(self):
        if self.ferias == 0:
            print("Você não tem dias de férias disponíveis.")
            return

        print(f"Tem {self.ferias} dias de férias por gozar.")
        dias_pedido = input("Deseja gozar quantos dias? ")

        try:
            dias_pedido = int(dias_pedido)
            if dias_pedido > self.ferias:
                print("Você não tem férias suficientes para esse pedido.")
            else:
                self.ferias_status = dias_pedido
                print(f"Aguardando aprovação para {dias_pedido} dias de férias.")

                # Atualizar o estado de férias do funcionário no arquivo JSON
                funcionarios = self.carregar_funcionarios()
                for func in funcionarios:
                    if func.id == self.id:  # Aqui 'func' agora é uma instância de Funcionario
                        func.ferias_status = dias_pedido  # Atualizar ferias_status com os dias pedidos

                # Salvar as alterações no arquivo
                funcionarios_data = [f.__dict__ for f in funcionarios]  # Convertendo objetos de volta para dicionários
                with open('ADC/data/funcionarios.json', 'w', encoding="utf-8") as f:
                    json.dump(funcionarios_data, f, indent=4)
        except ValueError:
            print("Insira um número válido de dias.")

