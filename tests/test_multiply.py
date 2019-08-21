import unittest
from tdd_demo.functions import multiply

class MyTestCase(unittest.TestCase):
    def test_multiply_proper_result(self):
        x = 7
        y = 7
        ans = multiply(x, y)
        assert ans == 49

    def test_sending_badness_to_function(self):
        x = "cars"
        y = "jokes"
        with self.assertRaises(TypeError) as cm:
            ans = multiply(x, y)
