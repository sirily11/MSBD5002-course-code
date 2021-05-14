from typing import List, Optional
import numpy as np
from webdb.hits_algorithm import Hits
from webdb.page_rank import PageRank

class Node:
    def __init__(self, name: str):
        """
        Construct a graph node
        """
        self.name = name
        self.children: List["Node"] = []
        self.parent = None

    def add_children(self, nodes: List["Node"]):
        for node in nodes:
            node.parent = self
            if node in self.children:
                raise RuntimeError("Child already exists")

        self.children += nodes

    def get_order(self, node, order_nodes: List["Node"]):
        name = self.name
        for i, n in enumerate(order_nodes):
            if node == n:
                return i

    def get_out_going_edges(self, order_nodes: List["Node"], print_output=True) -> List[int]:
        """
        Generate a matrix.
        Args:
            print_output:
            order_nodes: The output result will follow this order

        Returns:

        """
        results = [0 for i in range(len(order_nodes))]
        if print_output:
            print(f"h({self.name}) =", end=" ")

        for i, node in enumerate(self.children):
            order = self.get_order(node, order_nodes)
            results[order] = 1
            if print_output:
                print(f"a({node.name})", end=" ")
                if i < len(self.children) - 1:
                    print("+", end=" ")

        if print_output:
            print()
        return results

    def get_num_out_going_edges(self):
        return len(self.children)


class GraphConverter:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def convert(self, to_which_algo="pagerank"):
        if to_which_algo == "pagerank":
            return self.__convert_pagerank__()
        elif to_which_algo == "hits":
            return self.__convert_hit__()
        else:
            raise RuntimeError("Please choose either pagerank or hits")

    def __convert_hit__(self):
        h_list = []
        for node in self.nodes:
            results = node.get_out_going_edges(self.nodes)
            h_list.append(results)

        return np.array(h_list)

    def __convert_pagerank__(self):
        h_list: Optional[np.ndarray] = None
        for node in self.nodes:
            results = node.get_out_going_edges(self.nodes, print_output=False)
            results = np.array(results)
            results = results / node.get_num_out_going_edges()
            results = results.reshape(-1, 1)
            if h_list is None:
                h_list = results
            else:
                h_list = np.hstack((h_list, results))

        return np.array(h_list)


if __name__ == '__main__':
    x = Node("x")
    y = Node("y")
    z = Node("z")

    x.add_children([y, z])
    y.add_children([y, x])
    z.add_children([x, y])

    converter = GraphConverter(nodes=[x, y, z])
    m = converter.convert(to_which_algo="pagerank")
    print(m)

    page_rank = PageRank(matrix=m, d=0.8, c=np.array([0.2, 0.2, 0.2]))
    page_rank.run(10)
