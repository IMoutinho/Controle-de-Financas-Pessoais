'''Modulo que terá todas as funções utilizadas no main'''

from relatorios import exibir_relatorio_categoria, exibir_relatorio_mes_ano, exibir_relatorio_categoriaEscolhida, exibir_relatorio_mes_escolhido
from models import Transacao
import constantes
from utils import ler_tipo, ler_valor, ler_data


def registrar_transacao(lista_transacoes):
    print("Digite os detalhes da transação:")
    tipo = ler_tipo()
    valor = ler_valor()
    data = ler_data()
    categoria = selecionar_categoria(tipo)
    descricao = input("Digite uma descrição para a transação: ")
    nova_transacao = Transacao(
        id=len(lista_transacoes) + 1,
        tipo=tipo,
        valor=valor,
        data=data,
        categoria=categoria,
        descricao=descricao
    )
    lista_transacoes.append(nova_transacao)
    print("Transação registrada com sucesso!")


def calcular_saldo(lista_transacoes):
    saldo = 0
    for transacao in lista_transacoes:
        if transacao.tipo == 'receita':
            saldo += transacao.valor
        else:
            saldo -= transacao.valor
    print("\n-------------------------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("\n-------------------------------------------")


def exibir_relatorios(lista_transacoes):
    relatorio_opcao = -1
    while relatorio_opcao != 0:
        print("\n--- Relatórios ---")
        print("1. Relatório por Categoria")
        print("2. Relatório por Mês/Ano")
        print("3. Relatório Personalizado por Categoria")
        print("4. Relatório Personalizado por Mês/Ano")
        print("0 - Voltar ao Menu Principal")
        relatorio_opcao = input("Escolha uma opção de relatório: ")
        if relatorio_opcao == '1':
            exibir_relatorio_categoria(lista_transacoes)
        elif relatorio_opcao == '2':
            exibir_relatorio_mes_ano(lista_transacoes)
        elif relatorio_opcao == '3':
            tipo = ler_tipo()
            categoria_escolhida = selecionar_categoria(tipo)
            exibir_relatorio_categoriaEscolhida(
                lista_transacoes, categoria_escolhida)
        elif relatorio_opcao == '4':
            mes_ano_escolhido = input("Digite o mês/ano desejado (MM/AAAA): ")
            exibir_relatorio_mes_escolhido(lista_transacoes, mes_ano_escolhido)
        elif relatorio_opcao == '0':
            return
        else:
            print("Opção de relatório inválida!")


def selecionar_categoria(tipo):
    if tipo == 'receita':
        categorias = constantes.categorias_definidas['receita']
    else:
        categorias = constantes.categorias_definidas['despesa']
    
    print("Categorias disponíveis:\n")
    i = 1
    for categoria in categorias:
        print(f"{i}. {categoria}")
        i += 1
    while True:
        try:
            escolha = int(input("Selecione o número da categoria: "))
            if 1 <= escolha <= len(categorias):
                return categorias[escolha - 1]

            else:
                print("Escolha inválida. Tente novamente.")

        except ValueError:
                print("Entrada inválida. O valor deve ser um número.")
        




