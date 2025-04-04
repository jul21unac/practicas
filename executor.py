import sys

from BankAccount import BankAccount
from Coche import Coche
from Persona import Persona

if __name__ == '__main__':
    julio = Persona(18 , "Julio")
    julio.saludo()
    print(julio)

    volvo = Coche("Volvo","station vagon",1983)
    volvo.descripcion()
    print(volvo)

    cuenta = BankAccount("Julio")

    cuenta.depositar(1000000)

    cuenta.retirar("aaa")

    print(cuenta.mostrar_saldo())