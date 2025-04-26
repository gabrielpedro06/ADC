# Recursos Humanos — Projeto ADC

## Descrição do Projeto

Aplicação de gestão de Recursos Humanos desenvolvida no âmbito da unidade curricular de Ambientes de Desenvolvimento Colaborativo (ADC).  
O sistema organiza e facilita a gestão de funcionários, departamentos e administradores, com diferentes níveis de acesso e funcionalidades.

## Estrutura de Utilizadores

### Funcionários

- **Dados Pessoais**: Nome, Morada, Telemóvel, NIF, Sexo, IBAN, Doenças
- **Férias**: Número de dias disponíveis
- **Faltas**: Registo de faltas justificadas e injustificadas
- **Salário**: Cálculo baseado no número de faltas e função
- **Horário de Trabalho**
- **Folgas**

### Gestores de Departamento

- **Gestão de Funcionários Disponíveis**: Consulta do número de funcionários disponíveis num determinado dia (considerando horários e folgas)
- **Gestão de Horários e Folgas**: Atribuição e ajuste dos horários de trabalho e dias de folga dos funcionários

### Administradores

- **Gestão Completa**: Criação, edição e remoção de funcionários e departamentos
- **Acesso Total**: Permissões para consultar e modificar todos os dados do sistema
- **Conta Pré-Criada**: Conta de administrador criada diretamente no código para garantir o acesso inicial seguro

## Funcionalidades por Perfil

### Funcionário

- Atualizar dados pessoais
- Consultar e solicitar dias de férias
- Consultar faltas justificadas e injustificadas
- Consultar salário atual
- Consultar horário de trabalho
- Consultar dias de folga

### Gestor de Departamento

- Consultar funcionários disponíveis por dia
- Gerir horários de trabalho e folgas dos funcionários

### Administrador (RH)

- Criar, editar e remover funcionários
- Criar, editar e remover departamentos
- Acesso completo a todos os dados de funcionários e departamentos
- Conta de administrador previamente criada para gestão inicial do sistema

## Observações

- A aplicação utiliza ficheiros JSON para armazenamento de dados.
- A segurança das credenciais do administrador é assegurada por criação direta no código-fonte.
- A gestão de salários considera fatores como o número de faltas e a função exercida.
