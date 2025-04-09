import unittest

from User import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(ValueError):
            u = User("adds")
            #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
