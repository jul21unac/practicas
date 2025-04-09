from Jugador import Jugador


class Juego:

    def __init__(self):
        self._jugador = Jugador(100,20,"player")
        self._enemigo = Jugador(60,30,"enemy")

    def jugar(self):

        while self._jugador.vida >0 and self._enemigo.vida >0 :
            self._jugador.atacar(self._enemigo,self._jugador.ataque)
            if self._enemigo.vida<=0: break
            self._enemigo.atacar(self._jugador, self._enemigo.ataque )



