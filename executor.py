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

from Rectangulo import Rectangulo

if __name__ == '__main__':
    julio = Persona("Julio",43,"MAdrid" )
    julio.saludo()
    print(julio)

    volvo = Coche("Fiat","station vagon",1983,15616,46545646)
    volvo.descripcion()
    print(volvo)

    cuenta = BankAccount("Julio", "Ahorro")

    cuenta.depositar(1000000)

    cuenta.retirar(100)

    print(cuenta.mostrar_saldo())
    print(cuenta)

    fido = Perro("Fido",23,'chihuahu')
    garfield = Gato("garfield", 12,"raza1")
    print(fido.sonido())
    print(garfield.sonido())

    books = [("libro 1","vallejo",1982),("libro 2","chocano",1983),
             ("libro 3","valdelomar",1952),("libro 4","alegria",1972)]

    for t,a,an in books:
        Libro(t,a,an,"accion")

    Libro.mostrar_libros()

    prod = [("jabon",2.2,1,10),("cafe",3.3,12,10),
            ("azucar",4.4,1,10),("chocolate",3.4,20,10)]


    for n,p,q,u  in prod:
        Inventory.agregar_producto(Product(n,p,q,u))

    print(Inventory.buscar_producto("azucar"))
    print(Inventory.summar_precios())

    print("alerta de productos")
    for x in Inventory.productos_alerta():
        print(x.name)

    Inventory.vender("chocolate",4)
    Inventory.restock("jabon",20)
    print("alerta de productos 2")
    for x in Inventory.productos_alerta():
        print(x.name)

    c = Cuadrado(1)
    c.lado = 2

    game = Juego()
    game.jugar()




    mylist = ["apple", "banana", "cherry"]

    print(random.choice(mylist))

    c = Rectangulo(1,1, "Azul")

    print(c)
