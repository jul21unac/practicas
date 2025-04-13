import unittest

from Coche import Coche


class TestCoche(unittest.TestCase):
    def test_marca(self):
        with self.assertRaises(TypeError):
            c = Coche(111,"m",2005,1252,15611)

    def test_modelo(self):
        with self.assertRaises(TypeError):
            c = Coche("volvo",1221,2005,1252,15611)

    def test_anio(self):
        with self.assertRaises(TypeError):
            c = Coche("volvo", "2", "aaaaa", 1252, 15611)

    def test_anio_positive(self):
        with self.assertRaises(ValueError):
            c = Coche("volvo", "2", 0, 1252, 15611)


    def test_precio(self):
        with self.assertRaises(TypeError):
            c = Coche("volvo", "2", 1982, "sdsaas", 15611)

    def test_precio_positive(self):
        with self.assertRaises(ValueError):
            c = Coche("volvo", "2", 1982, 0, 15611)


    def test_kilometre(self):
        with self.assertRaises(TypeError):
            c = Coche("volvo", "2", 1982, 200000, "dasdas")

    def test_kilometre_positive(self):
        with self.assertRaises(ValueError):
            c = Coche("volvo", "2", 1982, 200000, 0)


if __name__ == '__main__':
    unittest.main()
