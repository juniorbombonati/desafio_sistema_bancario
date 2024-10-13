from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco:str):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao():
        pass

    def adicionar_conta():          
        pass

    @property
    def listar_contas(self):
        return self._contas or None
    
class PessoaFisica(Cliente):
    def __init__(self, cpf:str, nome:str, data_nascimento:datetime, *arg):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento 
        super().__init__(*arg)

class Conta:

    def __init__(self, numero:int, cliente):
        self._saldo = 0
        self._numero = numero
        self._cliente = cliente
        self._historico = Historico()

    # Método que retorna uma instância da classe conta
    @classmethod
    def nova_conta (cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def nova_conta(cliente:Cliente, numero:int):
        cliente._contas.append(numero)

    def sacar(self, valor:float):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Operação não realizada! Você não possui saldo suficiente!')
        elif valor > 0:
            saldo -= valor
            print('Operação realizada com sucesso!')
            return True
        else:
            print("Você digitou um valor inválido! Repita a operação!")
        return False

    def depositar(self, valor:float):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else:
            print("Opereração não realizada, o valor informado é inválido!")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite:float=500, limite_saques:int=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len (
            [transacao for transacao in self.historico.transacoes
            if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação não realizada, número de saques excedido!")

        elif excedeu_saques:
            print("Operação não realizada, quantida de saques excedida!")

        else:
            return super(Conta).sacar(valor) 

        return False  
        
    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}

    """

class Transacao:
    def __init__ (self, valor_transacao):
        self.valor = valor_transacao

    def registrar(conta:Conta):
        lancamento = {conta:{'Saque':[].append(Saque.valor), 'Depósito':[].append(Deposito.valor)}}
        
        return lancamento

class Historico:
    def __init__ (self):
        self._historico = []

    def adicionar_transacao(transacao:Transacao):
        pass

class Saque:
    def __init__(self, valor:float):
        self._valor = valor

class Deposito:
    def __init__(self, valor:float):
        self._valor = valor
        
#inputs
cliente = PessoaFisica('418.605.878-44', 'Junior', 16, 'Mauricio Guidugli, 269')
Conta.nova_conta(cliente, 123123)
Conta.nova_conta(cliente, 111222)
print(cliente.listar_contas())

