import unittest

from ..false_positive import ItemSet, FalsePosNeg


class TestFalsePosNeg(unittest.TestCase):
    def test_false_positives(self):
        expected = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3"])
        algorithm = ItemSet(freq_items=["i1", "i3"], in_freq_items=["i2"])
        fal = FalsePosNeg(expected_output=expected, algorithm_output=algorithm)
        pos, neg = fal.run()
        self.assertEqual(pos, ["i3"])
        self.assertEqual(neg, [])

    def test_false_negatives(self):
        expected = ItemSet(freq_items=["i1", "i3"], in_freq_items=["i2"])
        algorithm = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3"])
        fal = FalsePosNeg(expected_output=expected, algorithm_output=algorithm)
        pos, neg = fal.run()
        self.assertEqual(pos, [])
        self.assertEqual(neg, ["i3"])
