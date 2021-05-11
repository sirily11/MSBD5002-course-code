from dataware_house.GreedySelect import GreedySelect
from dataware_house.view import View


def q2():
    a = View("a", 100)
    b = View("b", 50)
    c = View("c", 75)
    d = View("d", 20)
    e = View("e", 30)
    f = View("f", 40)
    g = View("g", 1)
    h = View("h", 10)

    a.add_children([b, c])
    b.add_children([d, e])
    c.add_children([e, f])
    d.add_children([g])
    e.add_children([g, h])
    f.add_children([h])

    greedy = GreedySelect(root=a, views=[a, b, c, d, e, f, g, h])

    views = greedy.run(3)


if __name__ == '__main__':
    q2()