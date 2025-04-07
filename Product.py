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

    def __init__(self, name, price, quantity):
        self._name = name
        self.valida_precio(price)
        self._price = price
        self._quantity = quantity

    @staticmethod
    def valida_precio(value):
        if type(value) != int  and type(value) != float:
            raise TypeError("The value should be a number")
        if value <=0:
            raise ValueError("The number should be higher than 0")


