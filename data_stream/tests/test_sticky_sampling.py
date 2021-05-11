import unittest

from data_stream.sticky_sampling_algorithm import StickySampling


class TestStickySampling(unittest.TestCase):
    def test_t(self):
        ss = StickySampling(s=0.02, e=0.01, delta=0.1)
        self.assertEqual(ss.t, 622)

    def test_t2(self):
        ss = StickySampling(s=0.5, e=0.35, delta=0.5)
        self.assertEqual(ss.t, 4)

    def test_sample_results(self):
        events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
        coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
        ss = StickySampling(s=0.5, e=0.35, delta=0.5, events=events)
        before, after, final = ss.run(end_index_before_rate_change=8, coin_tosses=coin_tosses, prev_s=[])
        self.assertEqual(after, [('i1', 2), ('i2', 2)])
        self.assertEqual(final, [])
