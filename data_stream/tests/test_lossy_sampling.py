import unittest

from data_stream.lossy_counting_algorithm import LossyCountingAlgorithm


class TestLossySampling(unittest.TestCase):
    def test_one(self):
        events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
        coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
        ls = LossyCountingAlgorithm(s=0.5, e=0.25, events=events)
        output = ls.run(prev_s=[], max_b_current=3)
        self.assertEqual(output, [("i1", 3)])


if __name__ == '__main__':
    unittest.main()
