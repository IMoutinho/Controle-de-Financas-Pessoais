'''funcões para resumo de categoria/mês/ano'''


def relatorio_categoria(lista_transacoes):
    r_categoria = {}
    for transacao in lista_transacoes:
        if transacao.categoria not in r_categoria:
            r_categoria[transacao.categoria] = 0

        if transacao.tipo == 'receita':
            r_categoria[transacao.categoria] += transacao.valor
        else:
            r_categoria[transacao.categoria] -= transacao.valor

    return r_categoria


def relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida):
    total = 0.0
    for transacao in lista_transacoes:
        if transacao.categoria == categoria_escolhida:
            if transacao.tipo == 'receita':
                total += transacao.valor
            else:
                total -= transacao.valor
    return total


def relatorio_meses(lista_transacoes):
    r_mes_ano = {}
    for transacao in lista_transacoes:
        mes_ano = transacao.data.strftime('%m/%Y')
        if mes_ano not in r_mes_ano:
            r_mes_ano[mes_ano] = 0.0

        if transacao.tipo == 'receita':
            r_mes_ano[mes_ano] += transacao.valor
        else:
            r_mes_ano[mes_ano] -= transacao.valor

    return r_mes_ano


def relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido):
    total = 0.0
    for transacao in lista_transacoes:
        mes_ano = transacao.data.strftime('%m/%Y')
        if mes_ano == mes_ano_escolhido:
           if transacao.tipo == 'receita':
                total += transacao.valor
           else:
                total -= transacao.valor
    return total


def exibir_relatorio_categoria(lista_transacoes):
    r_categoria = relatorio_categoria(lista_transacoes)
    print("\n--- Relatório por Categoria ---")
    for categoria, total in r_categoria.items():
        print(f"Categoria: {categoria} | Total: R$ {total:.2f}")


def exibir_relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida):
    total = relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida)
    print(f"\n--- Relatório para Categoria: {categoria_escolhida} ---")
    print(f"Total: R$ {total:.2f}")

def exibir_relatorio_mes_ano(lista_transacoes):
    r_mes_ano = relatorio_meses(lista_transacoes)
    print("\n--- Relatório por Mês/Ano ---")
    for mes_ano, total in r_mes_ano.items():
        print(f"Mês/Ano: {mes_ano} | Total: R$ {total:.2f}")

def exibir_relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido):
    total = relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido)
    print(f"\n--- Relatório para Mês/Ano: {mes_ano_escolhido} ---")
    print(f"Total: R$ {total:.2f}")
