import unittest
from calc import suma,resta,multiplicacion,division

class test_calc(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(suma(2,3),5)
        self.assertAlmostEqual(suma("2","2.5"),4.5) 
    
    def test_resta(self):
        self.assertEqual(resta(10,5),5)
        self.assertAlmostEqual(resta("10.5","5"),5.5)
    
    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(2, 3), 6)
        self.assertEqual(multiplicacion(5, 4), 20)
        self.assertAlmostEqual(multiplicacion("2.5", "4"), 10.0)
        self.assertEqual(multiplicacion(-3, 2), -6)
        self.assertEqual(multiplicacion(0, 5), 0)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertAlmostEqual(division(15, 3), 5.0)
        self.assertAlmostEqual(division("10", "2"), 5.0)
        self.assertEqual(division(-10, 2), -5)
        self.assertAlmostEqual(division(7, 2), 3.5)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            division(5, 0)
        with self.assertRaises(ValueError):
            division(10, "0")


    def test_error(self):
        with self.assertRaises(ValueError):
            suma("a",3)
            resta("a",3)
            multiplicacion("a",3)
            division("a",3)

if __name__ == '__main__':
    unittest.main()