class Funcionario:
    def __init__(self, dados):
        self.id = dados["id"]
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
    
    def editar_dados(self):
        # Permitir ao funcionário editar seus dados
        print("Editar Dados Pessoais")
        self.nome = input(f"Nome (atual: {self.nome}): ") or self.nome
        self.morada = input(f"Morada (atual: {self.morada}): ") or self.morada
        self.telemovel = input(f"Telemóvel (atual: {self.telemovel}): ") or self.telemovel
        self.nif = input(f"NIF (atual: {self.nif}): ") or self.nif
        self.sexo = input(f"Sexo (atual: {self.sexo}): ") or self.sexo
        self.iban = input(f"IBAN (atual: {self.iban}): ") or self.iban
        # Adicionar outras alterações conforme necessário

    def consultar_ferias(self):
        # Exibir as férias do funcionário
        print(f"Férias disponíveis: {self.ferias} dias")

    def consultar_faltas(self):
        # Exibir as faltas do funcionário
        print(f"Faltas justificadas: {self.faltas['justificadas']}, Injustificadas: {self.faltas['injustificadas']}")
    
    def consultar_salario(self):
        # Exibir o salário do funcionário
        print(f"Salário: {self.salario}€")
    
    def consultar_folgas(self):
        # Exibir as folgas do funcionário
        print(f"Folgas: {', '.join(self.folgas)}")
