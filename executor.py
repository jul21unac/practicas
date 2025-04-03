import sys

from Coche import Coche
from Persona import Persona

if __name__ == '__main__':
    julio = Persona(18 , "Julio")
    julio.saludo()

    volvo = Coche("Volvo","station vagon",1983)
    volvo.descripcion()