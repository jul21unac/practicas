
class Coche:

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, value):
        self._marca = value

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, value):
        self._anio = value

    def descripcion(self):
        print("Coche " +self.marca + " del año " + str(self.anio)+ " Modelo " + self.modelo)


    def __init__(self,marca,modelo,anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio

    def __str__(self):
        return f"Coche : {self.marca} {self.modelo } ({self.anio})"
