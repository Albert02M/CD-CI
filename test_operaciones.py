# test_operaciones.py
import unittest
from operaciones import sumas, resta

class TestOperaciones(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(sumas(2, 3), 5)
        self.assertEqual(sumas(-1, 1), 0)
        self.assertEqual(sumas(0, 0), 0)

    def test_resta(self):
        self.assertEqual(resta(5, 3), 2)
        self.assertEqual(resta(-1, -1), 0)
        self.assertEqual(resta(0, 5), -5)

if __name__ == "__main__":
    unittest.main()
