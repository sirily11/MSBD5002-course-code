from typing import List, Optional


class View:
    children: List["View"]

    def __init__(self, name: str, cost: float, is_materialized=False):
        self.name = name
        self._cost = cost
        self.parents: List["View"] = []
        self.children: List["View"] = []
        self.is_materialized = is_materialized

    def __str__(self):
        return self.name

    def add_child(self, child: "View"):
        child.parents.append(self)
        self.children.append(child)

    def add_children(self, children: List["View"]):
        for c in children:
            if c == self:
                raise RuntimeError("Cannot add self")

            if c in self.children or self in c.parents:
                raise RuntimeError("Cannot add twice")

            c.parents.append(self)

        self.children += children

    @property
    def cost(self):
        """
        Get the cost of the current view.
        Returns: the cost

        """
        if self.is_materialized:
            return self._cost
        else:
            costs = [p.cost for p in self.parents]
            return min(costs)
