from typing import List

from dataware_house.view import View


class ViewGain:
    def __init__(self, root: "View"):
        """
        Calculate the Gain
        Args:
            root: Root view.
        """
        self.root = root

    def calculate_gain(self, first_materialization_condition: List[View], second_materialization_condition: List[View]):
        """
        Calculate the gain based on the first and second conditions.
        We will return the gain by using the second's total cost - first total costs
        Args:
            first_materialization_condition:
            second_materialization_condition:

        Returns:

        """
        cost_one = 0
        cost_two = 0
        for v in first_materialization_condition:
            v.is_materialized = True
        cost_one = self.calculate_total_cost()
        for v in first_materialization_condition:
            v.is_materialized = False

        for v in second_materialization_condition:
            v.is_materialized = True
        cost_two = self.calculate_total_cost()
        for v in second_materialization_condition:
            v.is_materialized = False
        return cost_two - cost_one

    def calculate_total_cost(self):
        """
        Calculate the total costs of the view based on the root
        Returns: the total cost

        """
        return ViewGain.calculate_total_cost_util(self.root, [])

    @staticmethod
    def calculate_total_cost_util(view: "View", calculated_view: List["View"]) -> float:
        total_cost = 0
        for c in view.children:
            if c not in calculated_view:
                total_cost += ViewGain.calculate_total_cost_util(c, calculated_view)
                calculated_view.append(c)

        total_cost += view.cost
        return total_cost


if __name__ == '__main__':
    psc = View("psc", 6)
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
    print(gain)