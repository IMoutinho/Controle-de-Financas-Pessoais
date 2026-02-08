# 💰 Controle de Finanças Pessoais (Projeto C)

Sistema de linha de comando (CLI) desenvolvido em **Python** para gestão de receitas e despesas pessoais. Este projeto consolida conceitos de **Programação Orientada a Objetos (POO)**, modularização e manipulação de arquivos.

## 📝 Descrição
O sistema permite que o usuário registre suas movimentações financeiras, categorizando-as como receitas ou despesas. O objetivo é facilitar o controle financeiro através de relatórios detalhados e persistência de dados, garantindo que as informações não se percam ao fechar o programa.

## ⚙️ Funcionalidades

* **Cadastro de Transações:** Registro completo com ID automático, tipo (receita/despesa), valor, data, categoria e descrição.
* **Gestão via Carteira:** Utilização da classe `Carteira` para gerenciar a lista de objetos `Transacao`.
* **Persistência de Dados:** Carregamento e salvamento automático em arquivo CSV (`data/transacoes.csv`).
* **Relatórios Detalhados:**
    * Extrato completo de transações.
    * Relatório agrupado por Categoria (com período de apuração).
    * Relatório mensal (Receitas vs Despesas e Saldo Líquido).
* **Validações Robustas:** Tratamento de erros para impedir datas inválidas, valores negativos ou tipos incorretos.

## 📂 Estrutura do Projeto

O código foi organizado em módulos para facilitar a manutenção e leitura:

```text
projeto-financas/
│
├── data/                   # Pasta onde o arquivo .csv é salvo
│   └── transacoes.csv      # Banco de dados (criado automaticamente)
│
├── src/                    # Código fonte do projeto
│   ├── main.py             # Ponto de entrada (Menu Principal)
│   ├── models.py           # Classes: Transacao e Carteira
│   ├── repositorio_transacoes.py  # Leitura e Escrita do CSV
│   ├── operacoes.py        # Lógica de registro e orquestração
│   ├── relatorios.py       # Funções de exibição e cálculo de relatórios
│   ├── utils.py            # Validadores (ler_data, ler_valor, etc.)
│   └── constantes.py       # Listas de categorias fixas
│
└── README.md               # Documentação do projeto
