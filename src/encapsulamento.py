class Conta:
    def __init__(self, agencia, saldo=0):
        self._saldo = saldo

    def get_saldo(self):
        return f'Saldo atual: {self._saldo}'

    def depositar(self, valor):
        self._saldo += valor
        print(f'Realizado um deposito de {valor}, seu saldo atual é {self._saldo}') 

    def sacar(self, valor):
        self._saldo -= valor
        print(f'Realizado um saque de {valor}, seu saldo atual é {self._saldo}')


# ----------------

conta = Conta('001')
print(conta)
