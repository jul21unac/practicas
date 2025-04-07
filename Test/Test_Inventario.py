import unittest

from Inventory import Inventory
from Product import Product


class MyTestCase(unittest.TestCase):

    def setUp(self):
        prod = [("jabon", 2.2, 1), ("cafe", 3.3, 3),
                ("azucar", 4.4, 1), ("chocolate", 3.4, 3)]

        Inventory._productos =[]
        for n,p,q in prod:
            Inventory.agregar_producto(Product(n, p, q))

        self.busqueda =Inventory.buscar_producto("Azucar")
        self.suma = Inventory.summar_precios()

    def test_busca_producto(self):

        self.assertEqual(self.busqueda, False)  # add assertion here

    def test_suma_precios(self):
        self.assertEqual(self.suma,13.3, "iguales")

    def test_precio(self):
        with self.assertRaises (ValueError):
            Product("Bolivar jabon", -10,5)

    def test_precio_type(self):
        with self.assertRaises (TypeError):
            Product("marsella jabon", "aaa",5)

if __name__ == '__main__':
    unittest.main()
