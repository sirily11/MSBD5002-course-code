from typing import Tuple, List

import numpy as np


def lrd(arr: np.ndarray, k: float) -> Tuple[float, List[int]]:
    new_arr = arr.copy()
    new_arr = list(new_arr)
    new_arr = [a for a in new_arr if a != 0]
    new_arr.sort()
    reachable_arr = new_arr[:k]
    max_val = max(reachable_arr)

    reachable_index = []
    for i, a in enumerate(arr):
        if a in reachable_arr:
            reachable_index.append(i)

    return 1 / max_val, reachable_index


def lof(distances: np.ndarray, k=2, display_names=None):
    if display_names is None:
        display_names = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

    distance_dict = {}
    for i, distance in enumerate(distances):
        display_name = display_names[i]
        lrd_val, neb = lrd(distance, k)
        print(f"lrd2{display_name} = {round(lrd_val, 2)}")
        distance_dict[display_name] = (lrd_val, neb)

    print("")
    for display_name, values in distance_dict.items():
        lrd_p, neb = values
        sum_value = 0
        print(f"LOF({display_name}) = (", end="")
        for i, n in enumerate(neb):
            nei = distances[n]
            lrd_o, _ = lrd(nei, k=k)
            sum_value += lrd_o / lrd_p
            print(f"{round(lrd_o, 2)} / {round(lrd_p, 2)}", end="")
            if i < len(neb) - 1:
                print(" + ", end="")

        lof_val = sum_value / k
        print(f") / {k} = {round(lof_val, 3)}", end="")
        print()


if __name__ == '__main__':
    distances = np.array([
        [0, 1, 2, 11, 12],
        [1, 0, 1, 11, 11],
        [2, 1, 0, 9, 10],
        [11, 11, 9, 0, 9],
        [12, 11, 10, 9, 0]
    ])

    k = 2

    lof(distances=distances, k=k)
