'''funcões para resumo de categoria/mês/ano'''

# r_categoria inicializa um dicionario. A função recebe lista_transacoes que contem todas as transações. A lista é percorrida em um for. é feita uma checagem
# se não existe categoria pra transacao da lista ou nao há transacao na lista o valor atribuido é zero. Do contrario, se for despesa diminui do saldo, se for receita soma


def relatorio_categoria(lista_transacoes):
    r_categoria = {}
    for transacao in lista_transacoes:

        if transacao.categoria not in r_categoria:
            r_categoria[transacao.categoria] = {
                'total': 0.0,
                'inicio': transacao.data,
                'fim': transacao.data
            }

        dados = r_categoria[transacao.categoria]

        if transacao.tipo == 'receita':
            dados['total'] += transacao.valor
        else:
            dados['total'] -= transacao.valor

        if transacao.data < dados['inicio']:
            dados['inicio'] = transacao.data
        if transacao.data > dados['fim']:
            dados['fim'] = transacao.data

    return r_categoria


# inicializa a variavel total com 0, loop for que percorre todas transacoes na lista de transacoes. Como recebe categoria_escolhida, ele verifica se a transacao é dessa categoria
# caso positivo, se for uma receita soma ao total, do contrario, subtrai.
def relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida):
    total = 0.0
    for transacao in lista_transacoes:
        if transacao.categoria == categoria_escolhida:
            if transacao.tipo == 'receita':
                total += transacao.valor
            else:
                total -= transacao.valor

    return total

# a lógica de todas as funções de relatório é basicamente a mesma, a diferença dessas que utilizam datas é que existe a função strftime que, nesse caso, seleciona somente
# a parte que queremos da data, nos casos, mes e ano.


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


def exibir_transacoes(lista_transacoes):
    print("\n===========================================")
    print('--- Todas Transações ---')

    for transacao in lista_transacoes:
        print("\n-------------------------------------------")
        print('ID: ', transacao.id)
        print('Tipo: ', transacao.tipo)
        print('Valor: R$', transacao.valor)
        print('Data: ', transacao.data)


def exibir_relatorio_categoria(lista_transacoes):
    dados_categoria = relatorio_categoria(lista_transacoes)

    print("\n=======================================================================")
    print(f"{'CATEGORIA':<20}| {'PERÍODO':^30} | {'TOTAL (R$)':>12}")
    print("------------------------------------------------------------------------")

    for categoria, dados in dados_categoria.items():
        d_inicio = dados['inicio'].strftime('%d/%m/%y')
        d_fim = dados['fim'].strftime('%d/%m/%y')

        periodo = f"{d_inicio} até {d_fim}"

        print(f"{categoria:<20} | {periodo:^30} | {dados['total']:>12.2f}")
    print("\n=======================================================================")


def exibir_relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida):
    total = relatorio_categoriaEscolhida(lista_transacoes, categoria_escolhida)
    print(f"\n--- Relatório para Categoria: {categoria_escolhida} ---")
    print(f"Total: R$ {total:.2f}")


def exibir_relatorio_mes_ano(lista_transacoes):
    r_mes_ano = relatorio_meses(lista_transacoes)
    print("\n===========================================")
    print(f"{'RELATÓRIO MÊS/ANO':^40}")
    print("-------------------------------------------")
    print(f"{'MÊS/ANO':<25}|{'TOTAL (R$)':>12}")
    print("\n-------------------------------------------")
    for mes_ano, total in r_mes_ano.items():
        print(f"{mes_ano:<25}|{total:>12.2f}")
    print("\n===========================================")


def exibir_relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido):
    total = relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido)
    print(f"\n--- Relatório para Mês/Ano: {mes_ano_escolhido} ---")
    print(f"Total: R$ {total:.2f}")
