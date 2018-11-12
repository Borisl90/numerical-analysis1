import unittest
from lib.scant_method import ScantMethod


class ScantMethodTest(unittest.TestCase):
    global scantObj
    scantObj = ScantMethod()

    def test_regular(self):
        self.assertEqual(scantObj.secant(lambda x: x ** 2 - 20, 4.5, 0.1, 20), 4.47213595499958)
        self.assertEqual(scantObj.secant(lambda x: x ** 2 - x - 1, 1, 2, 5), 4.47213595499958)


if __name__ == '__main__':
    unittest.main()