from typing import List, Tuple, Callable

import numpy as np


class LossyCountingAlgorithm:
    def __init__(self, s: float, e: float, events: List[str]):
        """

        Args:
            s: s
            e: ε
            delta: δ
        """
        self.s = s
        self.e = e
        self.events = events

    def run(self,
            prev_s: List[Tuple[str, int, int]],
            fail_on_insertion: Callable[[int, int, str, int], bool] = None,
            fail_on_update: Callable[[int, int, str, int], bool] = None,
            fail_on_deletion: Callable[[str, int], bool] = None,
            fail_decreasing: Callable[[str, int], bool] = None,
            start_index_before_rate_change=0,
            end_index_before_rate_change: int = 0,
            max_b_current=None):

        """

        Args:
            max_b_current:
            prev_s:
            fail_on_insertion: Callback function. Parameter is current bucket id, number of insertion, item_name, count
            fail_on_update:
            fail_on_deletion:
            fail_decreasing:
            start_index_before_rate_change:
            end_index_before_rate_change:

        Returns:

        """
        b_current = 1
        storages: List[Tuple[str, int, int]] = prev_s
        number_of_insertion = 0
        number_of_update = 0
        n = 0

        while (b_current - 1) * self.width_of_the_bucket < len(self.events):
            start = (b_current - 1) * self.width_of_the_bucket
            end = b_current * self.width_of_the_bucket

            content_in_bucket = self.events[start:end]
            for content in content_in_bucket:
                found = False
                for i, storage in enumerate(storages):
                    item_name, item_count, bucket = storage
                    if item_name == content:
                        number_of_insertion += 1
                        found = True

                        if fail_on_insertion is not None:
                            if fail_on_insertion(b_current, number_of_insertion, item_name, item_count):
                                break

                        storages[i] = (item_name, item_count + 1, bucket)
                if not found:
                    number_of_update += 1
                    if fail_on_update is not None:
                        if fail_on_update(b_current, number_of_insertion, content, 1):
                            continue
                    storages.append((content, 1, b_current - 1))

            print(f"B_Current: {b_current}")
            print("Before Cleaning Stage")
            print(storages)

            new_storages = []
            for i, storage in enumerate(storages):
                item_name, item_count, bucket = storage
                if item_count + bucket <= b_current:
                    pass
                else:
                    new_storages.append(storage)

            storages = new_storages
            b_current += 1
            n += self.width_of_the_bucket

            print("After Cleaning Stage")
            print(storages)

            if max_b_current is not None and b_current > max_b_current:
                break

        output = self.get_result_list(storages, n)
        return output

    def get_result_list(self, list_of_results: List[Tuple[str, int, int]], n: float) -> List[Tuple[str, int]]:
        final_results = []
        print(f"εN = {self.e * n}, sN = {self.s * n}")

        for item_name, count, b_current in list_of_results:
            if count + self.e * n >= self.s * n:
                final_results.append((item_name, count))

        return final_results

    @property
    def width_of_the_bucket(self):
        return int(np.ceil(1 / self.e))


if __name__ == '__main__':
    events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
    coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
    ls = LossyCountingAlgorithm(s=0.5, e=0.25, events=events)
    output = ls.run(prev_s=[], max_b_current=3)
    print(output)
