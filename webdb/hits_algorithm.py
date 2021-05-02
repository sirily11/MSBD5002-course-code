import numpy as np


class Hits:
    """
    A class implements hits algorithm.
    In the algorithm we need the initial matrix m.
    Matrix m is the matrix of each node with out going edges
    For example: a -> b, a -> c, then h(a) = a(b), a(c)
    """

    def __init__(self, matrix: np.ndarray, num_class: int):
        """
        Create a hits algorithm
        Args:
            matrix: initial matrix m
            num_class: number of class.
        """

        self.matrix = matrix
        self.hops = np.ones(num_class)
        self.num_class = num_class

    def calculate_hub(self, print_out=True, max_iter=10):
        """
        Calculate the hits

        Returns:
            Normalized hits
        """
        prev_hop = self.hops
        next_hop = self.hops
        i = 2
        next_hops = []

        while (prev_hop != next_hop).any() or i == 2:
            prev_hop = next_hop
            next_hop = self.matrix.dot(self.matrix.T).dot(next_hop)
            if print_out:
                print(f"Iteration {i}")
                print(np.round(next_hop, 3))
            next_hop = self.normalize(next_hop)
            if print_out:
                print("Normalized")
                print(np.round(next_hop, 3))
                print()
            next_hops.append(next_hop)
            i += 1

            if i > max_iter:
                break
        return next_hops

    def calculate_authority(self, print_out=True, max_iter=10):
        """
        Calculate the hits

        Returns:
            Normalized hits
        """
        prev_authority = self.hops
        next_authority = self.hops
        i = 2
        next_hops = []

        while (prev_authority != next_authority).any() or i == 2:
            prev_authority = next_authority
            next_authority = self.matrix.T.dot(self.matrix).dot(next_authority)
            if print_out:
                print(f"Iteration {i}")
                print(np.round(next_authority, 3))
            next_authority = self.normalize(next_authority)
            if print_out:
                print("Normalized")
                print(np.round(next_authority, 3))
                print()
            next_hops.append(next_authority)
            i += 1

            if i > max_iter:
                break
        return next_hops

    def normalize(self, matrix: np.ndarray):
        return (matrix / matrix.sum(axis=0, keepdims=1)) * self.num_class


if __name__ == '__main__':
    m = np.array([[1, 1, 1], [0, 0, 1], [1, 1, 0]])
    hits = Hits(matrix=m, num_class=3)
    hits.calculate_authority()
