'''Menu principal da aplicação.'''

from models import Transacao
from repositorio_transacoes import carregar_transacoes, salvar_transacoes

def exibir_menu():
    print("\n--- Controle de Finanças Pessoais ---")
    print("1. Registrar Transação (Receita/Despesa)")
    print("2. Listar todas as transações")
    print("3. Mostrar Saldo Atual")
    print("4. Relatórios")
    print("0. Sair")

def main():
    lista_transacoes = carregar_transacoes()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("Digite os detalhes da transação:")
            tipo = input("Digite o tipo da transação (receita/despesa): ")
            valor = float(input("Digite o valor da transação: "))
            data = input("Digite a data da transação (DD/MM/AAAA):")
            categoria = input("Digite a categoria da transação: ")
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
        elif opcao == '2':
            for transacao in lista_transacoes:
                print(transacao)
        elif opcao == '3':
            saldo = 0
            for transacao in lista_transacoes:
                if transacao.tipo == 'receita':
                    saldo += transacao.valor
                else:
                    saldo -= transacao.valor
            print(f"Saldo atual: R$ {saldo:.2f}")           
        elif opcao == '0':
            salvar_transacoes(lista_transacoes)
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida!")

