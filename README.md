# 💰 Projeto C - Controle de Finanças Pessoais

Programa desenvolvido em **Python** para gestão de receitas e despesas pessoais. Este projeto foi desenvolvido como parte da avaliação "Semana 4 e 5" (Projeto 1), consolidando conceitos de **Programação Orientada a Objetos (POO)**, modularização, tratamento de erros e manipulação de arquivos.

## 📝 Descrição do Problema
Muitas pessoas têm dificuldade em acompanhar para onde vai o seu dinheiro. Este sistema resolve esse problema permitindo o registro rápido de transações, a categorização de gastos e a geração automática de relatórios. O objetivo é oferecer uma visão clara do saldo financeiro e do histórico de movimentações, garantindo que os dados sejam salvos para consultas futuras.

## ⚙️ Principais Funcionalidades

* **Registro de Transações:** Cadastro completo com validação de dados (ID automático, valor numérico, data formatada, categoria e descrição).
* **Gestão Orientada a Objetos:** Implementação da classe 'Carteira' para gerenciar listas de objetos `Transacao`, aplicando conceitos de encapsulamento e composição.
* **Persistência de Dados:** Leitura e escrita automática em arquivo CSV (`data/transacoes.csv`), garantindo que as informações sejam salvas ao sair do programa.
* **Relatórios Detalhados:**
    * Extrato completo de transações em formato de tabela.
    * Relatório por Categoria (com período de apuração).
    * Relatório Mensal (Total de Receitas vs Despesas e Saldo Líquido formatado).
* **Validações Robustas:** O sistema impede entradas inválidas (ex: datas inexistentes ou valores não numéricos) através de tratamento de exceções (`try/except`).

# 📂 Estrutura de Diretórios

O código foi organizado em módulos específicos para facilitar a manutenção e a escalabilidade:

```text
projeto-financas/
│
├── data/                      # Diretório para armazenamento de dados
│   └── transacoes.csv         # Banco de dados persistente (gerado automaticamente)
│
├── src/                       # Código fonte da aplicação
│   ├── main.py                # Ponto de entrada (Menu Principal)
│   ├── models.py              # Classes: Transacao e Carteira
│   ├── repositorio_transacoes.py  # Leitura e Escrita do CSV (camada de dados)
│   ├── operacoes.py           # Lógica de registro e orquestração das ações
│   ├── relatorios.py          # Funções de exibição formatada (Tabelas e Cards)
│   ├── utils.py               # Validadores de entrada (ler_data, ler_valor, ler_tipo)
│   └── constantes.py          # Listas de categorias pré-definidas (Receita/Despesa)
│
└── README.md                  # Documentação do projeto
```

# 🚀 Como Executar o Projeto

Siga o passo a passo abaixo para rodar o sistema no seu computador.

### Pré-requisitos

* Ter o **Python 3**.
* Não é necessário instalar bibliotecas externas (o projeto utiliza apenas bibliotecas padrão como 'datetime').

### Passo a Passo

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone https://github.com/IMoutinho/Controle-de-Financas-Pessoais
    ```

2.  **Acesse a pasta do projeto:**
    ```bash
    cd projeto-financas
    ```

3.  **Verifique a pasta de dados:**
    O sistema salva os arquivos na pasta `data/`. Certifique-se de que ela existe:
    * **Linux/Mac:**
      ```bash
      mkdir data
      ```
    * **Windows:**
      Crie uma nova pasta chamada `data` dentro da pasta do projeto (manualmente ou via terminal).

4.  **Execute o programa:**
    ```bash
    python src/main.py
    ```

5.  **Utilização:**
    * Navegue pelo menu digitando o número da opção desejada e pressionando Enter.
    * Ao selecionar a opção **0 (Sair)**, o sistema salva automaticamente todas as alterações no arquivo CSV.
