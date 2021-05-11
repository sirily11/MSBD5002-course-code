import unittest

from data_stream.lossy_counting_algorithm import LossyCountingAlgorithm
from data_stream.space_saving_algorithm import SpaceSavingSampling


class TestSpaceSavingSampling(unittest.TestCase):
    def test_one(self):
        events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
        coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
        ls = SpaceSavingSampling(s=0.5, events=events, m=4)
        output, d = ls.run(prev_s=[], max_number_th=12)

        self.assertEqual(d, [('i4', 3, 0), ('i1', 4, 0), ('i7', 1, 2)])


if __name__ == '__main__':
    unittest.main()
