from functools import reduce


class Inventory:

    _productos = []

    @classmethod
    def agregar_producto(cls,producto):
        if not cls.buscar_producto(producto.name):
            cls._productos.append(producto)


    @classmethod
    def buscar_producto(cls,value):
        return any(x.name == value for x in cls._productos)

    @classmethod
    def summar_precios(cls):
        return reduce(lambda x , y : x + y.price, cls._productos, 0)

    @classmethod
    def productos_alerta(cls):
        return filter(lambda x:x.verifica_alerta() == True ,cls._productos)

    @classmethod
    def vender(cls,name,cantidad):
        if  cls.buscar_producto(name):
            prod = filter(lambda x:x.name == name ,cls._productos)
            for x in prod:
                x.quantity = x.quantity -cantidad
                x.verifica_alerta()
                cls._productos[cls._productos.index(x)] = x
    @classmethod
    def restock(cls,name, cantidad):
        if  cls.buscar_producto(name):
            prod = filter(lambda x:x.name == name ,cls._productos)
            for x in prod:
                x.quantity = x.quantity + cantidad
                x.verifica_alerta()
                cls._productos[cls._productos.index(x)] = x





