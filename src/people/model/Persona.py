from dataclasses import dataclass


@dataclass
class Persona :

    _nombre :str
    _edad : int
    _ciudad : str

    def saludo(self):
        print("Hola "+ self.nombre + " " + str(self.edad))

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self,value):
        self._ciudad = value


