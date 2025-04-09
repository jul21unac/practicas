import unittest

from Figura import Circulo, Cuadrado, Triangulo


class MytestFigura(unittest.TestCase):

    def setUp(self):
        self.t = Triangulo(2, 3)

    def test_validaCirculo(self):
        with self.assertRaises(TypeError):
           a= Circulo("sasad")

    def test_validaCirculoValueEr(self):
        with self.assertRaises(ValueError):
            Circulo(-1)

    def test_validaCuadrado(self):

        with self.assertRaises(ValueError):
            c= Cuadrado(1)
            c.lado = -1

    def test_validaTriangulo(self):

        with self.assertRaises(TypeError):
            self.t.altura = "dasd"





if __name__ == '__main__':
    unittest.main()
