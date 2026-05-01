# Projetofinalpoo-zoo
Projeto final FGV ADS POO

# Sistema de Gestão de Zoológico e Reabilitação Animal

## Descrição

Aplicação desenvolvida em Python com foco na aplicação prática dos conceitos de Programação Orientada a Objetos (POO). O sistema realiza o gerenciamento de animais, tratadores e tarefas operacionais em um zoológico, incluindo suporte a um fluxo adicional de reabilitação animal.

---

## Objetivo

Implementar um sistema capaz de:

- Gerenciar cadastro de animais e tratadores
- Controlar tarefas operacionais (alimentação, limpeza, tratamento)
- Registrar e rastrear atividades realizadas
- Persistir dados em arquivo
- Simular um fluxo de reabilitação animal

---

## Modelagem

### Entidades principais

- Animal (classe base)
  - Mamifero
  - Ave
  - Reptil

- Tratador (classe base)
  - TratadorMamiferos
  - TratadorAves
  - TratadorReptil

- Tarefa (classe base)
  - Alimentacao
  - LimpezaHabitat
  - ConsultaVeterinaria
  - Reabilitacao

---

## Conceitos de POO aplicados

- Herança: especialização de animais e tratadores
- Polimorfismo: execução de tarefas com comportamentos distintos
- Encapsulamento: organização dos atributos e métodos nas classes
- Abstração: definição de classes base para generalização do domínio

---

## Funcionalidades

- Cadastro de animais com definição de tipo e status (zoológico ou reabilitação)
- Cadastro de tratadores por área de atuação
- Registro de tarefas associando animal e tratador
- Listagem estruturada de entidades
- Execução de tarefas com retorno de resultado
- Persistência automática em arquivo JSON
- Carregamento de dados na inicialização

---

## Reabilitação Animal

O sistema implementa um fluxo de reabilitação como uma tarefa composta.

Durante a execução da reabilitação, são realizadas automaticamente:

- Alimentação controlada
- Consulta veterinária
- Atualização do estado do animal

Essa abordagem permite reutilização de lógica existente e simula um processo gradual de recuperação.

---

## Persistência

Os dados são armazenados no arquivo:

dados_zoo.json

Estrutura:

- animais: lista com nome, espécie, status e tipo
- tratadores: lista com nome, matrícula, setor e tipo
- tarefas: registros de atividades executadas

O sistema realiza:

- Salvamento automático após operações
- Carregamento dos dados ao iniciar

---

## Execução

bash cd zoologico_v1 python main.py 

---

## Estrutura do Projeto

zoologico_v1/ │ ├── models/ ├── exceptions/ ├── utils/ ├── sistema.py ├── main.py └── dados_zoo.json

---

## Considerações

O projeto atende integralmente aos requisitos propostos, incluindo:

- Implementação de POO completa
- Manipulação de arquivos
- Organização modular do código
- Interface de interação via terminal

Adicionalmente, foram implementados elementos não obrigatórios, como:

- Sistema de reabilitação animal
- Persistência com reconstrução de objetos
- Validação de entradas do usuário

Essas extensões ampliam o escopo do projeto e demonstram maior maturidade na modelagem do sistema.

---

## Autor

Mterra64
