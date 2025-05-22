from Jugador import Jugador
from random import randrange

class Juego:

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self,value):
        self._player = value

    @property
    def enemigo(self):
        return self._enemigo

    @enemigo.setter
    def enemigo(self,value):
        self._enemigo = value

    @property
    def ganador(self):
        return self._ganador



    @property
    def damage(self):
        return self._damage

    @property
    def turnos(self):
        return self._turnos


    def __init__(self):
        self._player = Jugador(randrange(80,100,10),randrange(1,30),"player")
        self._enemigo = Jugador(randrange(80,100,10),randrange(1,30),"enemy")

    def jugar(self):
        i=0
        while self._player.vida >0 and self._enemigo.vida >0 :
            i=i+1
            self._player.atacar(self._enemigo,self._player.ataque)
            if self._enemigo.vida<=0: break
            self._enemigo.atacar(self._player, self._enemigo.ataque )

        if self.player.vida <= 0:
            self._ganador= self.enemigo
        elif self.enemigo.vida<=0:
            self._ganador = self.player

        self._damage = self.ganador.vida_inicial - self.ganador.vida
        self._turnos = i
