import sys

from BankAccount import BankAccount
from Coche import Coche
from Gato import Gato
from Libro import Libro
from Perro import Perro
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

    cuenta.retirar(100)

    print(cuenta.mostrar_saldo())

    fido = Perro("Fido")
    garfield = Gato("garfield")

    print(fido.sonido())
    print(garfield.sonido())

    books = [("libro 1","vallejo",1982),("libro 2","chocano",1983),
             ("libro 3","valdelomar",1952),("libro 4","alegria",1972)]

    for t,a,an in books:
        Libro(t,a,an)



    Libro.mostrar_libros()

