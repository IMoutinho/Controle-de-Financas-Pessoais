'''modulo criado para guardar algumas funções uteis para a aplicação, como calculo de periodo (utilizado em alguns relatorios e que pode ser reaproveitada), leitura de tipo para 
facilitar a logica e evitar erros, leitura de valor e de data. '''

from datetime import datetime

def calcula_periodo(lista_transacoes, categoria_escolhida):
    '''função para calculo de periodo, que verifica as transações por categoria selecionada, verifica a data da primeira transação e da ultima e salva a data inicio e data fim'''

    data_inicio = None
    data_fim = None

    for transacao in lista_transacoes:
        if transacao.categoria == categoria_escolhida:
            if data_inicio is None:
                data_inicio = transacao.data
                data_fim = transacao.data
            else:
                data_inicio = min(data_inicio, transacao.data)
                data_fim = max(data_fim, transacao.data)

    return data_inicio, data_fim


def ler_tipo():
    '''função que faz a leitura do tpo digitado, se foi receita ou despesa. Só sai do loop quando for digitado uma opção valida'''
    while True:
        tipo = input("Digite o tipo da transação (receita/despesa): ").strip().lower()
        if tipo in ['receita', 'despesa']:
            return tipo
        print("Erro: Digite apenas 'receita' ou 'despesa'.")

def ler_valor():
    '''função que faz a leitura do valor digitado, que deve ser um NUMERO. não aceita que seja digitado outro tipo de valor'''
    while True:
        try:
            return float(input("Digite o valor da transação: "))
        except ValueError:
            print("Erro: Digite um número válido.")

def ler_data():
    '''função que faz a leitura da data da transação e aceita somente datas no formato dia/mes/ano'''
    while True:
        data = input("Digite a data da transação (DD/MM/AAAA): ").strip()
        try:
            tipo_data = datetime.strptime(data, "%d/%m/%Y")
            return tipo_data
        except ValueError:
            print("Erro: Formato inválido. Use DD/MM/AAAA.")