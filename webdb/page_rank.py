import numpy as np


class PageRank:
    def __init__(self, matrix: np.ndarray, c: np.ndarray = None, d: float = 1, ):
        self.matrix = matrix
        self.d = d
        self.c = c

    def run(self, num_iterations: int):
        r = np.ones(self.matrix.shape[0])

        for i in range(num_iterations):
            if self.c is not None:
                r = self.matrix.dot(r) * self.d + self.c
            else:
                r = self.matrix.dot(r) * self.d
            print(f"Iteration {i + 2}")
            print(r)
        return r


if __name__ == '__main__':
    m = np.array([[0.5, 0, 0.5], [0, 0, 0.5], [0.5, 1, 0]])
    page_rank = PageRank(matrix=m)
    page_rank.run(10)
