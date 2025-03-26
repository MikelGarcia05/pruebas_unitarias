import unittest
import math_utils


class TestUtils(unittest.TestCase):

    def test_es_primo(self):
        self.assertFalse(math_utils.es_primo(1))
        self.assertTrue(math_utils.es_primo(2))
        self.assertTrue(math_utils.es_primo(3))
        self.assertFalse(math_utils.es_primo(4))
        self.assertTrue(math_utils.es_primo(5))
        self.assertEqual(math_utils.es_primo(-5), "No es posible devolver números primos.")

if __name__ == '__main__':
    unittest.main()