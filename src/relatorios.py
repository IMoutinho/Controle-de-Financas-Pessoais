'''funcões para resumo de categoria/mês/ano'''


def relatorio_categoria(lista_transacoes):
    r_categoria = {}
    for transacao in lista_transacoes:
        if transacao.categoria not in r_categoria:
            r_categoria[transacao.categoria] = 0
