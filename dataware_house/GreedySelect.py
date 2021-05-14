from typing import List

from dataware_house.ViewGain import ViewGain
from dataware_house.view import View


class GreedySelect:
    def __init__(self, root: View, views: List[View]):
        self.root = root
        self.views = views

    def run(self, k=2):
        """
        Run greedy select algorithm
        Args:
            k: number of views need to be materialized

        Returns: set of views

        """
        s = [self.root]
        view_gain = ViewGain(root=self.root)

        for i in range(k):
            gains = []
            print_views = []
            max_gain = -1
            max_view = None
            for v in self.views:
                if v not in s:
                    tmp = s + [v]
                    gain = view_gain.calculate_gain(tmp, s)
                    gains.append(gain)
                    print_views.append(v)
                    if gain > max_gain:
                        max_gain = gain
                        max_view = v
            assert max_view is not None
            s.append(max_view)
            gains = [str(g) for g in gains]
            print(f"Choice {i + 1}")
            print([str(v) for v in print_views])
            print(gains)
            print(f"Select: {max_view.name}")
            print("==========================")

        return s


if __name__ == '__main__':
    a = View("a", 200)
    b = View("b", 100)
    c = View("c", 150)
    d = View("d", 120)
    e = View("e", 80)
    f = View("f", 70)
    g = View("g", 55)
    h = View("h", 90)
    i = View("i", 40)
    j = View("j", 10)
    k = View("k", 15)
    l = View("l", 20)
    m = View("m", 5)

    a.add_children([b, c, d])
    b.add_children([e, f, g])
    c.add_children([e, f, g])
    d.add_children([g, h, i])
    e.add_children([j, k])
    f.add_children([j, k])
    g.add_children([j, k, l])
    h.add_children([l, m])
    i.add_children([m])

    greedy = GreedySelect(root=a, views=[a, b, c, d, e, f, g, h, i, j, k, l, m])

    views = greedy.run(4)
