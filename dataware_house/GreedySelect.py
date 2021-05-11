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
    psc = View("psc", 6)
    pc = View("pc", 4)
    ps = View("ps", 0.8)
    sc = View("sc", 6)
    p = View("p", 0.2)
    s = View("s", 0.01)
    c = View("c", 0.1)

    psc.add_children([pc, ps, sc])
    pc.add_children([p, c])
    ps.add_children([p, s])
    sc.add_children([s, c])

    greedy = GreedySelect(root=psc, views=[psc, pc, ps, sc, p, s, c])

    views = greedy.run(2)
