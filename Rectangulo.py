from dataclasses import dataclass


class Rectangulo:

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self,value):
        self.validateParam(value)
        self._base = value

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self,value):
        self.validateParam(value)
        self._altura = value

    def area(self):
        return (self.base * self.altura)

    def perimetro(self):
        return 2 * (self.base + self.altura)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,value):
        self._color = value

    def __init__(self, base, altura, color):
        self.base = base
        self.altura = altura
        self.color = color

    def validateParam(self, value):
        if type(value) != int and type(value) !=float :
            raise TypeError("The value should be a number")
        if value <=0 :
            raise ValueError("The value should be higher than 0")

    def __str__(self):
       return f'[Rectangulo{self.base}_{self.altura}]'