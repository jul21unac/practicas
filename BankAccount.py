from logging import raiseExceptions


class BankAccount:

    def __init__(self, value):
        self._titular = value
        self._saldo = 0

    def depositar(self, value):
        if type(value) != int  and type(value) != float:
            raise TypeError("The value should be a number")
        if value <=0:
            raise ValueError("The number should be higher than 0")
        self._saldo = self._saldo + value

    def retirar(self, value):
        if type(value) != int and type(value) != float:
            raise TypeError("The value should be a number")
        if value <=0:
            raise ValueError("The number should be higher than 0")
        self._saldo = self._saldo - value

    def mostrar_saldo(self):
        return self._saldo