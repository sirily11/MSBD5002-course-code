from typing import List, Tuple, Callable

import numpy as np


class SpaceSavingSampling:
    def __init__(self, s: float, m: float, events: List[str]):
        """

        Args:
            s:
            m: Maximum space available
            events:
        """

        self.s = s
        self.m = m
        self.events = events

    def run(self, prev_s: List[Tuple[str, int, int]],
            fail_on_insertion: Callable[[int, int, str, int], bool] = None,
            fail_on_update: Callable[[int, int, str, int], bool] = None,
            fail_on_deletion: Callable[[str, int], bool] = None,
            fail_decreasing: Callable[[str, int], bool] = None,
            start_index_before_rate_change=0,
            end_index_before_rate_change: int = 0,
            max_number_th=None):
        """

        Args:
            prev_s:
            fail_on_insertion: Parameter: i, pe, item_name, count
            fail_on_update:
            fail_on_deletion:
            fail_decreasing:
            start_index_before_rate_change:
            end_index_before_rate_change:

        Returns:

        """

        d: List[Tuple[str, int, int]] = []
        pe = 0
        num_insertion = 0
        num_update = 0
        n = 0

        for i, e in enumerate(self.events):
            found = False
            for index, content in enumerate(d):
                item_name, count, max_error = content
                if e == item_name:
                    num_update += 1
                    found = True
                    if fail_on_update is not None:
                        if fail_on_update(num_update, pe, item_name, count):
                            break
                    d[index] = (item_name, count + 1, pe)
            if not found:
                num_insertion += 1
                if len(d) == self.m:
                    pe = min([count + max_error for item_name, count, max_error in d])
                    new_list = []
                    for content in d:
                        item_name, count, max_error = content
                        if count + max_error > pe:
                            new_list.append(content)

                    d = new_list
                if fail_on_insertion is not None:
                    if fail_on_update(num_insertion, pe, e, 1):
                        continue
                d.append((e, 1, pe))

            n += 1
            print(f"{i + 1}th, {e}, pe = {pe}")
            print(d)
            if max_number_th is not None and i + 1 >= max_number_th:
                break

        output = self.get_result_list(d, n)
        return output, d

    def get_result_list(self, list_of_results: List[Tuple[str, int, int]], n: float) -> List[Tuple[str, int]]:
        final_results = []
        print(f"sN = {self.s * n}")

        for item_name, count, max_error in list_of_results:
            if count + max_error >= self.s * n:
                final_results.append((item_name, count))

        return final_results


if __name__ == '__main__':
    events = ["i4", "i1", "i3", "i2", "i2", "i1", "i4", "i1", "i1", "i4", "i5", "i7", "i4", "i9"]
    coin_tosses = ["t", "h", "h", "t", "t", "t", "h", "t", "h", "t", "h", "h"]
    ls = SpaceSavingSampling(s=0.5, events=events, m=4)
    output, d = ls.run(prev_s=[], max_number_th=12)
    print(output, d)
