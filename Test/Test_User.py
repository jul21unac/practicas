import unittest

from src.users.User import User


class MyTestCase(unittest.TestCase):
    def test_something(self):
        with self.assertRaises(ValueError):
            u = User("adds","20250101")
            #self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
