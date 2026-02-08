'''Menu principal da aplicação.'''

from repositorio_transacoes import carregar_carteira, salvar_transacoes
from operacoes import registrar_transacao, exibir_relatorios
from relatorios import exibir_transacoes


def exibir_menu():
    print(" ______________________________________________________")
    print("|*********** CONTROLE DE FINANÇAS PESSOAIS *********** |")
    print(f"{'|1. Registrar Transação (Receita/Despesa)':<50} {'|':>5}")
    print(f"{'|2. Listar todas as transações':<50}{'|':>6}")
    print(f"{'|3. Mostrar Saldo Atual':<50}{'|':>6}")
    print(f"{'|4. Relatórios':<50}{'|':>6}")
    print(f"{'|0. Sair':<50}{'|':>6}")
    print(" ******************************************************")


def main():

    minha_carteira = carregar_carteira()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            registrar_transacao(minha_carteira)
            salvar_transacoes(minha_carteira.transacoes)

        elif opcao == '2':
            exibir_transacoes(minha_carteira.transacoes)

        elif opcao == '3':
            saldo = minha_carteira.calcular_saldo()
            print(f"\nSaldo Atual: R$ {saldo:.2f}")

        elif opcao == '4':
            exibir_relatorios(minha_carteira.transacoes)

        elif opcao == '0':
            salvar_transacoes(minha_carteira.transacoes)
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida!")


main()
