

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

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def validateParam(self, value):
        if type(value) != int and type(value) !=float :
            raise TypeError("The value should be a number")
        if value <=0 :
            raise ValueError("The value should be higher than 0")