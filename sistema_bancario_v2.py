from datetime import datetime, date

menu = """

Selecione uma das opções abaixo para continuar.

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3
data_transacao = []

while True:

    opcao = int(input(menu))

    if opcao == 1:
        if data_transacao.count(date.today()) > 9:
            print("Quantidade de trasações diárias excedidads")
        else:
            data_hora_deposito = datetime.now()
            formatacao_data = "%d/%m/%Y %H:%M"
            data_deposito = data_hora_deposito.date()
            data_transacao.append(data_deposito)
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo += valor_deposito
            extrato.append(f'{data_hora_deposito.strftime(formatacao_data)}    Depósito: R${valor_deposito:.2f}')
            print(f"Depósito de R${valor_deposito:.2f} realizado. Seu saldo é de R${saldo:.2f}")

    elif opcao == 2:
        if data_transacao.count(date.today()) > 9:
            print("Quantidade de trasações diárias excedidads")
        else:
            valor_saque = int(input("Informe o valor que deseja sacar: "))
            if valor_saque > 0 and valor_saque <= saldo:
                if numero_saques < 3:  
                    if valor_saque <= limite:
                        print("Saque realizado com sucesso! Retire seu dinheiro!")
                        data_hora_saque = datetime.now()
                        formatacao_data = "%d/%m/%Y %H:%M"
                        data_saque = data_hora_saque.date()
                        data_transacao.append(data_saque)
                        numero_saques += 1
                        saldo -= valor_saque
                        extrato.append(f'{data_hora_saque}    Saque: R${valor_saque:.2f}')
                    else:
                        print("O valor solicitado excede o limite permitido, verifique com seu gerente a possibilidade de aumento do limite")
                else:
                    print("Você excedeu a quantidade diária de saques")
            else:
                print("Saldo insuficiente")
    elif opcao == 3:

        print("Extrato".center(len("extrato") + 12, "/"))
        print("\n")
        if len(extrato) == 0:
            print("Não foram realizadas movimentações")
        else:
            for lancamento in extrato:
                print(lancamento)
        print("-----------------")
        print(f"\nSaldo: {saldo}")

    elif opcao == 4:
        print("Obrigado por usar o nosso sistema!")
        break

    else:
        print("Digite uma opção válida!")