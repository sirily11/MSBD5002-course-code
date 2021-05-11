import unittest

from dataware_house.ViewGain import ViewGain
from dataware_house.view import View


class SimpleCostTest(unittest.TestCase):
    def test_one(self):
        psc = View("psc", 6, is_materialized=True)
        pc = View("pc", 4)
        ps = View("ps", 0.8)
        sc = View("sc", 2)
        p = View("p", 0.2)
        s = View("s", 0.01)
        c = View("c", 0.1)

        psc.add_children([pc, ps, sc])
        pc.add_children([p, c])
        ps.add_children([p, s])
        sc.add_children([s, c])

        self.assertEqual(psc.cost, 6)
        self.assertEqual(pc.cost, 6)
        self.assertEqual(ps.cost, 6)
        self.assertEqual(sc.cost, 6)
        self.assertEqual(p.cost, 6)
        self.assertEqual(s.cost, 6)
        self.assertEqual(c.cost, 6)

        sc.is_materialized = True
        self.assertEqual(psc.cost, 6)
        self.assertEqual(pc.cost, 6)
        self.assertEqual(ps.cost, 6)
        self.assertEqual(sc.cost, 2)
        self.assertEqual(p.cost, 6)
        self.assertEqual(s.cost, 2)
        self.assertEqual(c.cost, 2)

    def test_two(self):
        psc = View("psc", 6, is_materialized=True)
        pc = View("pc", 4)
        ps = View("ps", 0.8)
        sc = View("sc", 2)
        p = View("p", 0.2)
        s = View("s", 0.01)
        c = View("c", 0.1)

        psc.add_children([pc, ps, sc])
        pc.add_children([p, c])
        ps.add_children([p, s])
        sc.add_children([s, c])

        self.assertEqual(psc.cost, 6)
        self.assertEqual(pc.cost, 6)
        self.assertEqual(ps.cost, 6)
        self.assertEqual(sc.cost, 6)
        self.assertEqual(p.cost, 6)
        self.assertEqual(s.cost, 6)
        self.assertEqual(c.cost, 6)

        sc.is_materialized = True
        ps.is_materialized = True

        self.assertEqual(psc.cost, 6)
        self.assertEqual(pc.cost, 6)
        self.assertEqual(ps.cost, 0.8)
        self.assertEqual(sc.cost, 2)
        self.assertEqual(p.cost, 0.8)
        self.assertEqual(s.cost, 0.8)
        self.assertEqual(c.cost, 2)

    def test_view_gain(self):
        psc = View("psc", 6, is_materialized=True)
        pc = View("pc", 4)
        ps = View("ps", 0.8)
        sc = View("sc", 2)
        p = View("p", 0.2)
        s = View("s", 0.01)
        c = View("c", 0.1)

        psc.add_children([pc, ps, sc])
        pc.add_children([p, c])
        ps.add_children([p, s])
        sc.add_children([s, c])

        view_gain = ViewGain(root=psc)
        gain = view_gain.calculate_gain([sc, psc], [psc])
        self.assertEqual(gain, 12)

    def test_view_gain2(self):
        psc = View("psc", 6, is_materialized=True)
        pc = View("pc", 4)
        ps = View("ps", 0.8)
        sc = View("sc", 2)
        p = View("p", 0.2)
        s = View("s", 0.01)
        c = View("c", 0.1)

        psc.add_children([pc, ps, sc])
        pc.add_children([p, c])
        ps.add_children([p, s])
        sc.add_children([s, c])

        view_gain = ViewGain(root=psc)
        gain = view_gain.calculate_gain([sc, psc, ps], [psc])
        self.assertEqual(gain, 23.6)
