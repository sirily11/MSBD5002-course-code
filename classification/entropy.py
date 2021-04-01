from typing import List

import numpy as np


def entropy(probabilities_arr: List[float]) -> float:
    """
    Calculate entropy based on the probabilities array
    """
    s = 0
    for p in probabilities_arr:
        a = -np.log2(p) * p if p != 0 else 0
        s += a

    return s


def conditional_entropy(probabilities_arr: List[float], conditional_probabilities: List[float]) -> float:
    """
    Compute conditional entropy based on the probabilities array and conditional probabilities
    The algorithm is based on $H(Y|X) = -\sum\sum p(x,y)logp(y|x) $

    Args:
        probabilities_arr: list of probabilities. p(x, y)
        conditional_probabilities: conditional probabilities p(y|x)

    Returns: conditional entropy
    """
    s = 0
    for i, p in enumerate(probabilities_arr):
        a = - p * np.log2(conditional_probabilities[i]) if conditional_probabilities[i] != 0 else 0
        s += a

    return s
