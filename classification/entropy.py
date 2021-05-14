from typing import List

import numpy as np


def entropy(probabilities_arr: List[float]) -> float:
    """
    Calculate entropy based on the probabilities array.
    Smaller entropy, more information we get
    """
    s = 0
    for p in probabilities_arr:
        a = -np.log2(p) * p if p != 0 else 0
        s += a

    return s


def conditional_entropy_part(probabilities_arr: List[float]):
    """
    Compute part of conditional entropy. For example will compute H(x|y=1). Will return the value as
    well as a array contains H(x=1|y=1), H(x=2|y=1)

    Args:
        probabilities_arr: list of probabilities. p(x, y). If we are computing only the x|y=1

    Returns: conditional entropy part, array of value
    """
    s = []
    for p in probabilities_arr:
        s.append(p / sum(probabilities_arr))

    return entropy(s), s


def conditional_entropy(probabilities_arr: List[float], conditional_array: List[float]) -> float:
    """
    Compute conditional entropy based on the probabilities array and conditional probabilities
    The algorithm is based on $H(Y|X) = -\sum\sum p(x,y)logp(y|x) $

    Args:
        probabilities_arr: p(x, y)
        conditional_array: this is the result from conditional_entropy_part's array

    Returns:

    """
    s = 0
    for i, p in enumerate(probabilities_arr):
        cp = conditional_array[i]
        s += -p * np.log2(cp) if cp > 0 else 0

    return s


if __name__ == '__main__':
    # Entropy
    # Suppose we have a table
    # x1/x2  1   2
    # 1      1/4 1/2
    # 2      0   1/4
    # then the probability array = [1/4, 1/2, 0, 1/4]
    # then the conditional array H(Y|X=2) = [1/8, 1/8]
    # result, s_0 = conditional_entropy_part(probabilities_arr=[1/4, 1/4])
    # result, s_1 = conditional_entropy_part(probabilities_arr=[0, 1/2])
    # result = conditional_entropy([1/4, 0, 1/4, 1/2], [0.5, 0.0, 0.5, 1.0])
    # print(result)
    result = entropy([0.2, 0.1, 0.1, 0.2, 0.2, 0.1, 0.1])
    print(result)