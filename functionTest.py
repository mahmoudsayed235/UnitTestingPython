from unittest import TestCase
from functions import divide

class testFunctionClass(TestCase):
    def testDivideFunction(self):
        x = 15
        y = 5
        z = 3
        #  self.assertEqual(divide(x,y),z)
        self.assertAlmostEqual(divide(x, y), z, delta=0.0001)
    def testDivideNegativeFunction(self):
        x=15
        y=-5
        z=-3
        self.assertAlmostEqual(divide(x,y),z,delta=0.0001)
    def testDivideZeroFunction(self):
        x=0
        y=5
        z=0
        self.assertEqual(divide(x,y),z)
    def testDivideByZero(self):
        with self.assertRaises(ValueError):
            divide(15,0)