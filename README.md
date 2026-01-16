# Projeto C – Controle de Finanças Pessoais

## Descrição
Este sistema é uma aplicação de linha de comando desenvolvida em Python para gerenciar finanças pessoais. Ele permite o registro de receitas e despesas com armazenamento persistente em arquivos CSV.

## Principais Funcionalidades
* **Registro de Transações**: Cadastro de ID, tipo (receita/despesa), valor, data, categoria e descrição.
* **Persistência de Dados**: Leitura e escrita automática no arquivo `transacoes.csv`.
* **Cálculo de Saldo**: O sistema calcula o saldo líquido atual baseado nas entradas e saídas.
* **Validação OO**: Uso de Programação Orientada a Objetos com Getters e Setters para validar dados.

## Estrutura de Diretórios
* `src/`: Códigos fonte (.py).
* `data/`: Arquivos de dados (.csv).

## Como Executar
1. Navegue até a pasta `src/`.
2. Execute o comando: `python main.py`
