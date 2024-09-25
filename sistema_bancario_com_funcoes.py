def criar_usuario(nome, data_nascimento, cpf, endereco):

    #Somente numero do CPF dever ser armazenados
    #Não são permitidos cpf duplicados
    return nome, data_nascimento, cpf, endereco

def criar_conta_corrente(cpf):

    global contas_correntes
    AGENCIA = "0001"

    if len(contas_correntes) == 0:
        contas_correntes.append(1)
        conta_corrente = 1
    else:
        contas_correntes.append(max(contas_correntes) + 1) 
        conta_corrente = max(contas_correntes) + 1

    return AGENCIA, conta_corrente


def deposito(saldo, valor, extrato):
    saldo += valor_deposito
    extrato.append(f'Depósito: R${valor_deposito:.2f}')
    print(f"Depósito de R${valor_deposito:.2f} realizado. Seu saldo é de R${saldo:.2f}")

    return saldo, extrato

def saque(*, saldo=None, valor=None, extrato=None, limite=None, numero_saques=None, limite_saques=None):

    if valor > 0 and valor <= saldo:
        if numero_saques < 3:  
            if valor <= limite:
                print("Saque realizado com sucesso! Retire seu dinheiro!")
                numero_saques += 1
                saldo -= valor
                extrato.append(f'Saque: R${valor:.2f}')
            else:
                print("O valor solicitado excede o limite permitido, verifique com seu gerente a possibilidade de aumento do limite")
        else:
            print("Você excedeu a quantidade diária de saques")
    else:
        print("Saldo insuficiente")

    return saldo, extrato

def extrato(saldo, *, extrato: list =None):
    print("Extrato".center(len("extrato") + 12, "/"))
    print("\n")
    if len(extrato) == 0:
        print("Não foram realizadas movimentações")
    else:
        for lancamento in extrato:
            print(lancamento)
    print("-----------------")
    print(f"\nSaldo: {saldo}")


menu_inicial = '''

Olá, seja bem vindo!

[1] Já é correntista? Tecle Para Continuar.
[2] Ainda não é correntista? Faça seu cadastro.

=>'''

menu = """

Selecione uma das opções abaixo para continuar.

[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

=> """

contas_correntes = []
clientes = {}
lista_cpf = []

#Validação do cliente, caso o cpf não esteja cadastrado, não é possível prosseguir.
while True:

    entrada = int(input(menu_inicial))

    if entrada == 1:
            break
    
    elif entrada == 2:
        validador_cpf = input("Digite seu CPF: ")
        if validador_cpf in lista_cpf:
            print("CPF já consta na base")
        else:
            nome = input("\nNome: ")
            data_nascimento = input("Data de Nascimento: ")
            endereco = input("Endereço: ")
            nome, data_nascimento, cpf, endereco = criar_usuario(nome, data_nascimento, validador_cpf, endereco)
            AGENCIA, conta_corrente = criar_conta_corrente(validador_cpf)
            clientes[nome] = {"Data de Nascimento": data_nascimento, "CPF":cpf, "Endereço":endereco, "Agência":AGENCIA, "Número da Conta": conta_corrente}
            lista_cpf.append(cpf)

    else:
        print("Digite uma opção válida")

saldo = 0
limite = 500
movimentacao = []
numero_saques = 0
LIMITE_SAQUES = 3
contador = 0

while True:
    contador += 1
    if contador < 2:
        validacao_cpf = input("Digite seu CPF para prosseguir: ")
        if validacao_cpf in lista_cpf:
                
            while True:

                opcao = int(input(menu))

                if opcao == 1:
                    valor_deposito = float(input("Informe o valor do depósito: "))
                    saldo, movimentacao = deposito(saldo, valor_deposito, movimentacao)
                    
                    
                elif opcao == 2:
                    valor = int(input("Digite o valor que deseja sacar: "))
                    saque(saldo=saldo, valor=valor, extrato=movimentacao, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

                elif opcao == 3:
                    extrato(saldo, extrato= movimentacao)
                    
                elif opcao == 4:
                    print("Obrigado por usar o nosso sistema!")
                    break

                else:
                    print("Digite uma opção válida!")
        
        else:
            print("CPF inválido! Reinicie o programa e cadastre um CPF")
            break
    else:
        break




