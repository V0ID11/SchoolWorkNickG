import unittest
from calc_func import calc

class TestCalcOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc('Add',1,3),4)

    def test_sub(self):
        self.assertEqual(calc('Sub',4,2),2)

    def test_mul(self):
        self.assertEqual(calc('Mul',2,3),6)
    
    def test_blargh(self):
        self.assertIsNone(calc('Bluh',1,3))
        with self.assertRaises(TypeError):
            calc("No operands")

if __name__ == '__main__':
    unittest.main()