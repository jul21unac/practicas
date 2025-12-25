import unittest

from src.rectangle.model.Rectangulo import Rectangulo


class TestRectangulo(unittest.TestCase):
    def test_altura(self):
        with self.assertRaises(TypeError):
            c = Rectangulo(1,'a',"Rojo")

    def test_base(self):
        with self.assertRaises(TypeError):
            c = Rectangulo('a',1,"Azul")

    def test_altura_value(self):
        with self.assertRaises(ValueError):
            c = Rectangulo(1,0,"Gris")

    def test_base_value(self):
        with self.assertRaises(ValueError):
            c = Rectangulo(-1,0,"Verde")

if __name__ == '__main__':
    unittest.main()
