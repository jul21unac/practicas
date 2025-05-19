class Animal:

    def __init__(self, value, peso, raza):
        self.nombre = value
        self.peso = peso
        self.raza = raza
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,value):
        self._nombre = value

    def sonido(self):
        pass

    @property
    def raza(self):
        return self._raza

    @raza.setter
    def raza(self,value):
        self._raza = value

    @property
    def peso(self):
        return self._peso

    @peso.setter
    def peso(self,value):
            self._peso = value



