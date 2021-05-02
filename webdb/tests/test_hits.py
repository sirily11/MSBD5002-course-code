import unittest
from ..hits_algorithm import Hits
import numpy as np


class TestHits(unittest.TestCase):
    def test_example1(self):
        m = np.array([[1, 1, 1], [0, 0, 1], [1, 1, 0]])
        hits = Hits(matrix=m, num_class=3)
        results = hits.calculate_hub(print_out=False)
        results_2 = hits.calculate_authority(print_out=False)

        self.assertEqual(list(np.round(results[0], 3)), [1.5, 0.5, 1])
        self.assertEqual(list(np.round(results[5], 3)), [1.5, 0.402, 1.098])

        self.assertEqual(list(np.round(results_2[0], 3)), [1.071, 1.071, 0.857])
        self.assertEqual(list(np.round(results_2[5], 3)), [1.098, 1.098, 0.804])
