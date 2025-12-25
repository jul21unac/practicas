from logging import raiseExceptions


class BankAccount:

    def __init__(self, titular, tc):
        self._titular = titular
        self._saldo = 0
        self.tipo_cuenta =tc

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

    @property
    def tipo_cuenta(self):
        return self._tipo_cuenta

    @tipo_cuenta.setter
    def tipo_cuenta(self,value):
        self._tipo_cuenta = value

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, value):
        self._titular = value

    def __str__(self):
        return f'Cuenta : {self._titular} + " " + {self._tipo_cuenta}'
