class Jugador:

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self,value):
        self._vida = value

    @property
    def ataque(self):
        return self._ataque

    @ataque.setter
    def ataque(self,value):
        self._ataque = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,value):
        self._nombre = value
    @property
    def vida_inicial(self):
        return self._vida_inicial

    def __init__(self, vida, ataque, nombre):
        self._vida = vida
        self._ataque = ataque
        self._nombre = nombre
        self._vida_inicial = vida


    def recibe_ataque(self,value):
        self._vida = self._vida - value

    def atacar(self, jugador, atq):
        jugador.recibe_ataque(atq)


    def __str__(self):
        return f'Jugador({self.vida},{self.nombre})'