"""
An algorithm maintains an ε-deficient synopsis if it satisfy the following:

Condition 1: There is no false negative.
Condition 2: The difference between the estimated frequency and the true frequency is at most εN.
Condition 3: All items whose true frequencies less than (s-ε)N
             are classified as infrequent items in the algorithm output
"""
from typing import List, Dict

from data_stream.false_positive import ItemSet, FalsePosNeg


class AlgorithmFrequency:
    def __init__(self, frequency: Dict[str, int]):
        """

        Args:
            frequency: I1: 4, I2: 3
        """
        self.frequency = frequency


class DeficientSynopsis:
    def __init__(self, item_sets: List[ItemSet], algorithm_frequencies: List[AlgorithmFrequency],
                 expected_algorithm: ItemSet, expected_frequency: AlgorithmFrequency, n: int, s: float, e: float):
        """
        Compute ε Deficient Synopsis

        Args:
            item_sets:
                Algorithm: Frequent Items, Infrequent Items

            algorithm_frequencies:
                Algorithm: I1: Frequency, I2: Frequency...
        """

        assert len(item_sets) == len(algorithm_frequencies)
        for af in algorithm_frequencies:
            assert len(af.frequency) == len(algorithm_frequencies[0].frequency)

        self.item_sets = item_sets
        self.algorithm_frequencies = algorithm_frequencies
        self.expected_algorithm = expected_algorithm
        self.expected_frequency = expected_frequency
        self.n = n
        self.s = s
        self.e = e

    def check(self):
        """
        Check if the algorithm is ε-deficient synopsis

        Returns: ε-deficient synopsis, no ε-deficient synopsis
        """
        have_deficient = []
        not_have_deficient = []

        for i in range(len(self.item_sets)):
            item_set = self.item_sets[i]
            frequency = self.algorithm_frequencies[i]
            algorithm_number = f"Algorithm {i + 1}"
            if not self.__check_condition_one__(item_set=item_set, frequency=frequency):
                print(f"{algorithm_number} has failed condition 1")
                not_have_deficient.append(algorithm_number)
                continue
            if not self.__check_condition_two__(item_set=item_set, frequency=frequency):
                print(f"{algorithm_number} has failed condition 2")
                not_have_deficient.append(algorithm_number)
                continue
            if not self.__check_condition_three__(item_set=item_set, frequency=frequency):
                print(f"{algorithm_number} has failed condition 3")
                not_have_deficient.append(algorithm_number)
                continue
            have_deficient.append(algorithm_number)

        print()
        print(f"Have deficient: {have_deficient}")
        print(f"Don't have deficient: {not_have_deficient}")
        return have_deficient, not_have_deficient

    def __check_condition_one__(self, item_set: ItemSet, frequency: AlgorithmFrequency) -> bool:
        fp, fn = FalsePosNeg(expected_output=self.expected_algorithm, algorithm_output=item_set).run(print_out=False)
        return len(fn) == 0

    def __check_condition_two__(self, item_set: ItemSet, frequency: AlgorithmFrequency) -> bool:
        expected_diff = self.e * self.n
        for item, freq in frequency.frequency.items():
            expected_freq = self.expected_frequency.frequency[item]
            if abs(expected_freq - freq) > expected_diff:
                return False

        return True

    def __check_condition_three__(self, item_set: ItemSet, frequency: AlgorithmFrequency) -> bool:
        less_than_value = (self.s - self.e) * self.n
        less_than_frequencies = [i for i, f in self.expected_frequency.frequency.items() if f < less_than_value]
        for item in less_than_frequencies:
            if item not in item_set.in_freq_items:
                return False
        return True


if __name__ == '__main__':
    item_sets = [
        ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"]),
        ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"]),
        ItemSet(freq_items=["i1", "i2", "i3", "i4"], in_freq_items=[]),
    ]

    algorithm_frequencies = [
        AlgorithmFrequency(frequency={"i1": 7, "i2": 3, "i3": 2, "i4": 1}),
        AlgorithmFrequency(frequency={"i1": 2, "i2": 2, "i3": 1, "i4": 1}),
        AlgorithmFrequency(frequency={"i1": 3, "i2": 2, "i3": 2, "i4": 1})
    ]

    expected_frequency = AlgorithmFrequency(frequency={"i1": 4, "i2": 3, "i3": 2, "i4": 1})

    expected_algorithm = ItemSet(freq_items=["i1"], in_freq_items=["i2", "i3", "i4"])

    ds = DeficientSynopsis(item_sets=item_sets,
                           algorithm_frequencies=algorithm_frequencies,
                           expected_algorithm=expected_algorithm,
                           expected_frequency=expected_frequency,
                           s=0.4,
                           n=10,
                           e=0.2)

    ds.check()
