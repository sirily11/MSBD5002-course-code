from typing import List


def gini(probabilities_arr: List[float]) -> float:
    """
    Calculate entropy based on the probabilities array
    """
    s = 1
    for p in probabilities_arr:
        s -= p ** 2

    return s
