import json
class Funcionario:
    def __init__(self, dados):
        self.id = dados[0]
        self.id_departamento = dados[1]
        self.nome = dados[2]
        self.morada = dados[3]
        self.telemovel = dados[4]
        self.nif = dados[5]
        self.sexo = dados[6]
        self.iban = dados[7]
        self.doencas = dados[8]
        self.ferias = dados[9]
        self.faltas = dados[10]
        self.salario = dados[11]
        self.horario = dados[12]
        self.folgas = dados[13]
    
    def __str__(self):
        return f"""Funcionário {self.nome} (ID: {self.id}) - Departamento: {self.id_departamento})\n Morada: {self.morada} - Telemóvel: {self.telemovel}\n
    NIF: {self.nif} - IBAN: {self.iban} - Salário: {self.salario}€\nSexo: {self.sexo} - Doenças: {self.doencas}\n
    Férias: {self.ferias} dias - Faltas: {self.faltas} - Horário: {self.horario} - Folgas: {self.folgas}\n
    """
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def id_departamento(self):
        return self._id_departamento
    
    @id_departamento.setter
    def id_departamento(self, value):
        self._id_departamento = value
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, value):
        self._nome = value
    
    @property
    def morada(self):
        return self._morada
    
    @morada.setter
    def morada(self, value):
        self._morada = value
    
    @property
    def telemovel(self):
        return self._telemovel
    
    @telemovel.setter
    def telemovel(self, value):
        self._telemovel = value

    @property
    def nif(self):
        return self._nif
    
    @nif.setter
    def nif(self, value):
        self._nif = value
        
    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, value):
        self._sexo = value
    
    @property
    def iban(self):
        return self._iban
    
    @iban.setter
    def iban(self, value):
        self._iban = value
    
    @property
    def doencas(self):
        return self._doencas
    
    @doencas.setter
    def doencas(self, value):
        self._doencas = value
        
    @property
    def ferias(self):
        return self._ferias

    @ferias.setter
    def ferias(self, value):
        self._ferias = value
        
    @property
    def faltas(self):
        return self._faltas
    
    @faltas.setter
    def faltas(self, value):
        self._faltas = value
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, value):
        self._salario = value
    
    @property
    def horario(self):
        return self._horario
    
    @horario.setter
    def horario(self, value):
        self._horario = value
        
    @property
    def folgas(self):
        return self._folgas
    
    @folgas.setter
    def folgas(self, value):
        self._folgas = value
        
    def colocar_funcionario(self):
        with open('data/funcionarios.json', 'a') as arquivo_funcionarios:
            # Adicionar novo funcionário ao arquivo JSON
            funcionario = {
                "id": self._id,
                "id_departamento": self._id_departamento,
                "nome": self._nome,
                "morada": self._morada,
                "telemovel": self._telemovel,
                "nif": self._nif,
                "sexo": self._sexo, 
                "iban": self._iban,
                "doencas": self._doencas,
                "ferias": int(self._ferias),
                "faltas": self._faltas,
                "salario": int(self._salario),
                "horario": self._horario,
                "folgas": self._folgas
            }
            json.dump(funcionario, arquivo_funcionarios, indent=4)
            print("Funcionário adicionado com sucesso!")
            arquivo_funcionarios.close()
            
    def editar_dados(self):
        # Permitir ao funcionário editar seus dados
        print("Editar Dados Pessoais")
        self.nome = input(f"Nome (atual: {self._nome}): ") or self._nome
        self.morada = input(f"Morada (atual: {self._morada}): ") or self._morada
        self.telemovel = input(f"Telemóvel (atual: {self._telemovel}): ") or self._telemovel
        self.nif = input(f"NIF (atual: {self._nif}): ") or self._nif
        self.sexo = input(f"Sexo (atual: {self._sexo}): ") or self._sexo
        self.iban = input(f"IBAN (atual: {self._iban}): ") or self._iban
        # Adicionar outras alterações conforme necessário

    def consultar_ferias(self):
        # Exibir as férias do funcionário
        print(f"Férias disponíveis: {self._ferias} dias")

    def consultar_faltas(self):
        # Exibir as faltas do funcionário
        print(f"Faltas justificadas: {self._faltas['justificadas']}, Injustificadas: {self._faltas['injustificadas']}")
    
    def consultar_salario(self):
        # Exibir o salário do funcionário
        print(f"Salário: {self._salario}€")
    
    def consultar_folgas(self):
        # Exibir as folgas do funcionário
        print(f"Folgas: {', '.join(self._folgas)}")
