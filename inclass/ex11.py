from webdb.hits_algorithm import Hits
import numpy as np


def q1():
    m = np.array([[0, 1, 1], [1, 0, 0], [1, 1, 0]])
    hits = Hits(matrix=m, num_class=3)
    print("Hub")
    hits.calculate_hub()
    print("Authority")
    hits.calculate_authority()



if __name__ == '__main__':
    q1()