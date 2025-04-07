from functools import reduce


class Inventory:

    _productos = []

    @classmethod
    def agregar_producto(cls,producto):
        cls._productos.append(producto)

    @classmethod
    def buscar_producto(cls,value):
        return any(x.name == value for x in cls._productos)

    @classmethod
    def summar_precios(cls):
        return reduce(lambda x , y : x + y.price, cls._productos, 0)



