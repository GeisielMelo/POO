from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.permissao = False

    @abstractmethod
    def sacar(self, value): ...

    def depositar(self, value):
        if value < 0:
            return print('VALOR INVALIDO')
        self.saldo += value
        return print(f'Novo Saldo: R$ {self.saldo}')

    def to_list(self):
        return [self.agencia, self.conta, self.saldo]


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, value):
        limite = -self.limite

        if self.permissao is False:
            return print('Você não tem permissao para sacar.')

        if self.saldo - value < limite:
            return print('Saldo Insuficiente.')
        self.saldo -= value
        return print(f'Saque: R$ {value}, Novo Saldo: R$ {self.saldo}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
        super().__init__(agencia, conta, saldo)

    def sacar(self, value):

        if self.permissao is False:
            return print('Você não tem permissao para sacar.')

        if self.saldo - value < 0:
            return print('Saldo Insuficiente')
        self.saldo -= value
        return print(f'Saque: R$ {value}, Novo Saldo: R$ {self.saldo}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'


class Banco:
    def __init__(self):
        self.agencias = [111, 222, 333, 444]
        self.contas = [4444, 5555, 1111, 3333]
        self.clientes = ['Ana', 'Marcus', 'Maria', 'Pedro']

    def autenticar(self, cliente, dados: list):
        if dados[2][0] not in self.agencias:
            return print('Sua agencia não pertence a este Banco.')

        if dados[2][1] not in self.contas:
            return print('Conta não pertence a este Banco.')

        if dados[0] not in self.clientes:
            return print('Usuario não pertence a este Banco.')

        cliente.conta.permissao = True
