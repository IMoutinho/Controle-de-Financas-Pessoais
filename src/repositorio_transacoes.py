'''leitura/escrita de transações em arquivo CSV'''
from models import Transacao
from datetime import datetime

def salvar_transacoes(lista_transacoes, nome_arquivo='dados/transacoes.csv'):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        for transacao in lista_transacoes:
            data_formatada = transacao.data.strftime('%d/%m/%Y')
            linha = f"{transacao.id},{transacao.tipo},{transacao.valor},{data_formatada},{transacao.categoria},{transacao.descricao}\n"
            arquivo.write(linha)


def carregar_transacoes(nome_arquivo='dados/transacoes.csv'):
    transacoes = []

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                if len(dados) != 6:
                    continue
                nova_transacao = Transacao(id=int(dados[0]),
                                       tipo=dados[1],
                                       valor=float(dados[2]),
                                       data=datetime.strptime(dados[3], '%d/%m/%Y'),
                                       categoria=dados[4],
                                       descricao=dados[5])
                transacoes.append(nova_transacao)
    except FileNotFoundError:
        return []
    
    return transacoes
