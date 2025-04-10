import sys

from BankAccount import BankAccount
from Coche import Coche
from Figura import Cuadrado
from Gato import Gato
from Inventory import Inventory
from Juego import Juego
from Libro import Libro
from Perro import Perro
from Persona import Persona
from Product import Product
import random

if __name__ == '__main__':
    julio = Persona("Julio",43,"MAdrid" )
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

    prod = [("jabon",2.2,1),("cafe",3.3,3),
            ("azucar",4.4,1),("chocolate",3.4,3)]


    for n,p,q in prod:
        Inventory.agregar_producto(Product(n,p,q))

    print(Inventory.buscar_producto("Azucar"))
    print(Inventory.summar_precios())


    c = Cuadrado(1)
    c.lado = 2

    game = Juego()
    game.jugar()




    mylist = ["apple", "banana", "cherry"]

    print(random.choice(mylist))