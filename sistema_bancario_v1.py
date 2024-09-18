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


while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor_deposito = float(input("Informe o valor do depósito: "))
        saldo += valor_deposito
        extrato.append(f'Depósito: R${valor_deposito:.2f}')
        print(f"Depósito de R${valor_deposito:.2f} realizado. Seu saldo é de R${saldo:.2f}")

    elif opcao == 2:
        valor_saque = int(input("Informe o valor que deseja sacar: "))
        if valor_saque > 0 and valor_saque <= saldo:
            if numero_saques < 3:  
                if valor_saque <= limite:
                    print("Saque realizado com sucesso! Retire seu dinheiro!")
                    numero_saques += 1
                    saldo -= valor_saque
                    extrato.append(f'Saque: R${valor_saque:.2f}')
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