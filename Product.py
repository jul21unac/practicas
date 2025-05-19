from lib.Validatos import validateNumber


class Product:

    @property
    def name(self):
        return  self._name

    @name.setter
    def name(self,value):
        self._name = value


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self.valida_precio(value)
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def umbral_minimo(self):
        return self._umbral_minimo

    @umbral_minimo.setter
    def umbral_minimo(self, value):
        validateNumber("Umbral Minimo", value)
        self._umbral_minimo = value

    def __init__(self, name, price, quantity, umbral_minimo):
        self._name = name
        self.valida_precio(price)
        self._price = price
        self._quantity = quantity
        self._umbral_minimo = umbral_minimo

    @staticmethod
    def valida_precio(value):
        if type(value) != int  and type(value) != float:
            raise TypeError("The value should be a number")
        if value <=0:
            raise ValueError("The number should be higher than 0")


    def verifica_alerta(self):

        return  self._quantity - self._umbral_minimo <=1

    def __str__(self):
        return f'Product {self.name} quantity {self.quantity}'