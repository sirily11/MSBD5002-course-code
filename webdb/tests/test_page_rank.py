import unittest
import numpy as np

from webdb.page_rank import PageRank


class TestPageRank(unittest.TestCase):
    def test_page_rank(self):
        m = np.array([[0.5, 0, 0.5], [0, 0, 0.5], [0.5, 1, 0]])
        page_rank = PageRank(matrix=m)
        result = page_rank.run(5)
        self.assertEqual(list(result), [1.15625, 0.53125, 1.3125])
