from abc import ABC, abstractmethod
import math

class Figura(ABC):

    @abstractmethod
    def area(self):
       pass

    @abstractmethod
    def perimetro(self):
        pass

    @staticmethod
    def validaParam(value):
        if type(value) != int and type(value) != float:
            raise TypeError("Debe ser Int o float")
        if value <= 0:
            raise ValueError("debe ser mayor que 0")

class Circulo(Figura):

    @property
    def radio(self):
        return self._radio
    @radio.setter
    def radio(self,value):
        self.validaParam(value)
        self._radio = value

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return  round( (self._radio**2)*math.pi)

    def perimetro(self):
        return round( 2*self._radio*math.pi)



class Cuadrado(Figura):

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, value):
        self.validaParam(value)
        self._lado = value

    def __init__(self, value):
        self.lado = value

    def area(self):
        return round(self._lado**2)

    def perimetro(self):
        return round(4*self._lado)

class Triangulo(Figura):

    def __init__(self,b,a):
        self.base =b
        self.altura = a

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, value):
        self.validaParam(value)
        self._altura = value

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self,value):
        self.validaParam(value)
        self._base = value

    def area(self):
        return round( self._altura*self._base/2)

    def perimetro(self):
        return round(self.base + self.altura + math.sqrt(self.base**2 + self.altura**2))


