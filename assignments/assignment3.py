from data_stream.lossy_counting_algorithm import LossyCountingAlgorithm
import numpy as np

from webdb.page_rank import PageRank


def q3():
    events = ["i3", "i2", "i4", "i3", "i5", "i4", "i2", "i4", "i2", "i4", "i1", "i6", "i2", "i7", "i1", "i7"]
    ls = LossyCountingAlgorithm(s=0.4, e=0.2, events=events)
    # print(ls.width_of_the_bucket)
    output = ls.run(prev_s=[], max_b_current=3)
    print(output)


def q5():
    m = np.array([[0, 1, 0, 0], [0.5, 0, 0, 0], [0.5, 0, 0, 1], [0, 0, 1, 0]])
    page_rank = PageRank(matrix=m, d=0.8, c=np.array([0.2, 0.2, 0.2, 0.2]))
    page_rank.run(10)


if __name__ == '__main__':
    q5()
