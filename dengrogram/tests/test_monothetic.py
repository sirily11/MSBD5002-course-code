import unittest
import numpy as np

from dengrogram.monothetic_approach import monithetic_approach


class TestMonothetic(unittest.TestCase):
    def test_one(self):
        m = {
            "a": np.array([0, 1, 1, 1, 0]),
            "b": np.array([1, 1, 1, 1, 0]),
            "c": np.array([1, 0, 1, 0, 1])
        }

        a, b = monithetic_approach(m)
        self.assertEqual(a, [2, 3, 4])
        self.assertEqual(b, [1, 5])
