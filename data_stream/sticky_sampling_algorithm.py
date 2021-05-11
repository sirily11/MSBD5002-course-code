from copy import deepcopy
from typing import List, Tuple, Callable

import numpy as np


class StickySampling:

    def __init__(self, s: float, e: float, delta: float, events: List[str]):
        """

        Args:
            s: s
            e: ε
            delta: δ
        """
        self.s = s
        self.e = e
        self.delta = delta
        self.events = events

    def run(self, coin_tosses: List[str],
            prev_s: List[Tuple[str, int]],
            fail_on_insertion: Callable[[int, int, str, int], bool] = None,
            fail_on_update: Callable[[int, int, str, int], bool] = None,
            fail_on_deletion: Callable[[str, int], bool] = None,
            fail_decreasing: Callable[[str, int], bool] = None,
            start_index_before_rate_change=0,
            end_index_before_rate_change: int = 0,
            ):
        """
        Run the algorithm

        Args:
            fail_decreasing: Callback function handling whether the resampling decreasing will fail
            fail_on_deletion: Callback function handling whether the resampling deletion will fail
            fail_on_update: Callback function handling initial update will fail
                            Parameter for this function is current index, number of updates, item name, count
            fail_on_insertion: Callback function handling initial insertion will fail.
                                Parameter for this function is current index, number of insertion, item name, count
            prev_s:
            start_index_before_rate_change:
            coin_tosses:
            end_index_before_rate_change:

        Returns:

        """
        num_increasing = 0
        num_update = 0

        s: List[Tuple[str, int]] = prev_s
        before_resample = []
        after_resample = []
        samples_before_rate_change = self.events[start_index_before_rate_change:end_index_before_rate_change]

        for index, sample in enumerate(samples_before_rate_change):
            found = False
            for i, item in enumerate(s):
                item_name, count = item
                if item_name == sample:
                    found = True
                    num_update += 1
                    if fail_on_update is not None:
                        if fail_on_update(index, num_update, item_name, count):
                            break
                    s[i] = (item_name, count + 1)

            if not found:
                num_increasing += 1
                if fail_on_insertion is not None:
                    if fail_on_insertion(index, num_increasing, sample[0], 1):
                        continue
                s.append((sample, 1))

        s.sort(key=lambda e: e[0], reverse=False)
        print("Before sample rate changes")
        print(s)
        before_resample = deepcopy(s)

        current_coin_toss_index = 0
        item_index = 0
        while item_index < len(s):
            item_name, count = s[item_index]
            toss_result = coin_tosses[current_coin_toss_index]

            current_coin_toss_index += 1

            if toss_result.upper() == "T":
                if count - 1 == 0:
                    if fail_on_deletion is not None:
                        if fail_on_deletion(item_name, count):
                            continue
                    s.remove(s[item_index])
                else:
                    if fail_decreasing is not None:
                        if fail_decreasing(item_name, count):
                            continue
                    s[item_index] = (item_name, count - 1)
            else:
                item_index += 1

        print("After sample rate changes")
        print(s)

        after_resample = deepcopy(s)
        s = self.get_result_list(s, len(self.events))

        print("Final Results")
        print(s)

        return before_resample, after_resample, s

    def data_no(self, sampling_rate: int):
        """
        Get the data no using the sampling rate

        Args:
            sampling_rate:

        Returns:

        """
        print(f"{self.t * sampling_rate + 1} ~ {self.t * 2 * sampling_rate}")
        return self.t * sampling_rate + 1, self.t * 2 * sampling_rate

    def get_result_list(self, list_of_results: List[Tuple[str, int]], n: float) -> List[Tuple[str, int]]:
        final_results = []
        print(f"εN = {self.e * n}, sN = {self.s * n}")

        for item_name, count in list_of_results:
            if count + self.e * n >= self.s * n:
                final_results.append((item_name, count))

        return final_results

    @property
    def t(self):
        return np.ceil((1 / self.e) * np.log(1 / self.s * 1 / self.delta))


if __name__ == '__main__':
    events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
    coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
    ss = StickySampling(s=0.5, e=0.35, delta=0.5, events=events)
    ss.run(end_index_before_rate_change=8, coin_tosses=coin_tosses, prev_s=[])

    # events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
    # coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
    # ss = StickySampling(s=0.5, e=0.35, delta=0.5, events=events)
    # ss.run(start_index_before_rate_change=8,
    #        end_index_before_rate_change=11,
    #        coin_tosses=coin_tosses,
    #        prev_s=[("i1", 2), ("i2", 2)],
    #        fail_on_insertion=lambda index, number_of_insertion, item_name, count: number_of_insertion == 1
    #        )
    # print(ss.get_result_list([("i1", 5), ("i2", 4), ("i3", 2)], 16))
