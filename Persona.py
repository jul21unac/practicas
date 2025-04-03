

class Persona :

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

    def __init__(self,edad, nombre):
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f"Persona : {self.nombre } ({self.edad})"
