
class Coche:

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, value):
        self._marca = value

    @property
    def


    def setModelo(self, modelo):
        self.modelo = modelo

    def setAnio(self, anio):
        self.anio = anio

    def descripcion(self):
        print("Coche " +self.marca + " del año " + str(self.anio)+ " Modelo " + self.modelo)


    def __init__(self,marca,modelo,anio):
        self._marca = marca
        self._modelo = modelo
        self._anio = anio


