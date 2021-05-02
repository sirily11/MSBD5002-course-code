"""
If we say: The algorithm has no false positives.
All true infrequent items are classified as infrequent items in the algorithm output.

If we say: the algorithm has no false negatives.
All true frequent items are classified as frequent items in the algorithm output.
"""
from typing import List

import pandas as pd
import numpy as np


class ItemSet:
    def __init__(self, freq_items: List[str], in_freq_items: List[str]):
        """
        Create an itemset

        Args:
            freq_items: Frequent items
            in_freq_items: Infrequent items
        """
        self.freq_items = freq_items
        self.in_freq_items = in_freq_items


class FalsePosNeg:
    def __init__(self, expected_output: ItemSet, algorithm_output: ItemSet):
        """
        False Positive / negative classifier

        Args:
            expected_output:
            algorithm_output:
        """
        self.expected_output = expected_output
        self.algorithm_output = algorithm_output

    def run(self, print_out=True):
        """
        Run the algorithm and give the false negative and positive items

        Returns: false positives, false negatives

        """

        false_positives = []
        false_negatives = []

        for item in self.algorithm_output.freq_items:
            if item in self.expected_output.in_freq_items:
                false_positives.append(item)

        for item in self.algorithm_output.in_freq_items:
            if item in self.expected_output.freq_items:
                false_negatives.append(item)

        if print_out:
            print("False Positives")
            print(false_positives)

            print("False Negatives")
            print(false_negatives)

        return false_positives, false_negatives


if __name__ == '__main__':
    expected = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3"])
    algorithm = ItemSet(freq_items=["i1", "i3"], in_freq_items=["i2"])
    fal = FalsePosNeg(expected_output=expected, algorithm_output=algorithm)
    fal.run()
