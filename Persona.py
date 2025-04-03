

class Persona :


    def saludo(self):
        print("Hola "+ self.nombre + " " + str(self.edad))

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad


    def __init__(self,edad, nombre):
        self.nombre = nombre
        self.edad = edad

