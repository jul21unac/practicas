

from lib.Validatos import validateString, validateNumber, validatePositive


class Coche:

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        validateString("marca",value)
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        validateString("modelo", value)
        self._modelo = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        validateNumber("anio", value )
        validatePositive("anio", value)
        self._anio = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self,value):
        validateNumber("precio", value)
        validatePositive("Precio", value)
        self._precio = value

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self,valor):
        validateNumber("kilometraje",valor)
        validatePositive("Kilometraje", valor)
        self._kilometraje =valor

    def descripcion(self):
        print("Coche " +self.marca + " del año " + str(self.anio)+ " Modelo " + self.modelo)


    def __init__(self,marca,modelo,anio,precio,kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio
        self.kilometraje = kilometraje

    def __str__(self):
        return f"Coche : {self.marca} {self.modelo } ({self.anio})"
