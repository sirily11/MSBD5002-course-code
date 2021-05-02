import unittest

from data_stream.deficient_synopsis import AlgorithmFrequency, DeficientSynopsis
from data_stream.false_positive import ItemSet


class TestDeficientSynopsis(unittest.TestCase):
    def test_deficient_synopsis(self):
        item_sets = [
            ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"]),
            ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"]),
            ItemSet(freq_items=["i1", "i2", "i3", "i4"], in_freq_items=[]),
        ]

        algorithm_frequencies = [
            AlgorithmFrequency(frequency={"i1": 7, "i2": 3, "i3": 2, "i4": 1}),
            AlgorithmFrequency(frequency={"i1": 2, "i2": 2, "i3": 1, "i4": 1}),
            AlgorithmFrequency(frequency={"i1": 3, "i2": 2, "i3": 2, "i4": 1})
        ]

        expected_frequency = AlgorithmFrequency(frequency={"i1": 4, "i2": 3, "i3": 2, "i4": 1})

        expected_algorithm = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"])

        ds = DeficientSynopsis(item_sets=item_sets,
                               algorithm_frequencies=algorithm_frequencies,
                               expected_algorithm=expected_algorithm,
                               expected_frequency=expected_frequency,
                               s=0.4,
                               n=10,
                               e=0.2)

        h, dh = ds.check()
        self.assertEqual(h, ["Algorithm 2"])
        self.assertEqual(dh, ["Algorithm 1", "Algorithm 3"])
