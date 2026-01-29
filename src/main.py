'''Menu principal da aplicação.'''

from repositorio_transacoes import carregar_transacoes, salvar_transacoes
from operacoes import registrar_transacao, calcular_saldo, exibir_relatorios
from relatorios import exibir_transacoes


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
            registrar_transacao(lista_transacoes)

        elif opcao == '2':
            exibir_transacoes(lista_transacoes)

        elif opcao == '3':
            calcular_saldo(lista_transacoes)

        elif opcao == '4':
            exibir_relatorios(lista_transacoes)

        elif opcao == '0':
            salvar_transacoes(lista_transacoes)
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida!")


main()
