import unittest

from Rectangulo import Rectangulo


class TestRectangulo(unittest.TestCase):
    def test_altura(self):
        with self.assertRaises(TypeError):
            c = Rectangulo(1,'a')

    def test_base(self):
        with self.assertRaises(TypeError):
            c = Rectangulo('a',1)

    def test_altura_value(self):
        with self.assertRaises(ValueError):
            c = Rectangulo(1,0)

    def test_base_value(self):
        with self.assertRaises(ValueError):
            c = Rectangulo(-1,0)

if __name__ == '__main__':
    unittest.main()
