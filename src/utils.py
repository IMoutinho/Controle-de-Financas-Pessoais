from datetime import datetime

def calcula_periodo(lista_transacoes, categoria_escolhida):

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
    while True:
        tipo = input("Digite o tipo da transação (receita/despesa): ").strip().lower()
        if tipo in ['receita', 'despesa']:
            return tipo
        print("Erro: Digite apenas 'receita' ou 'despesa'.")

def ler_valor():
    while True:
        try:
            return float(input("Digite o valor da transação: "))
        except ValueError:
            print("Erro: Digite um número válido.")

def ler_data():
    while True:
        data = input("Digite a data da transação (DD/MM/AAAA): ").strip()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            print("Erro: Formato inválido. Use DD/MM/AAAA.")