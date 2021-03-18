import numpy as np
from typing import List
from copy import deepcopy
from pprint import pprint
from distances import complete_linkage, group_average_linkage


def get_print_group(groups):
    return [[e + 1 for e in group] for group in groups]


def polythetic_approach(distance_matrix: np.ndarray, distance_func, groups: List[List]):
    new_groups = deepcopy(groups)

    while True:
        distances_a = []
        distances_b = []
        for i in new_groups[1]:
            distance_a = distance_func([row[i] for index, row in enumerate(distance_matrix) if
                                        index in new_groups[0]])
            distance_b = distance_func([row[i] for index, row in enumerate(distance_matrix) if
                                        index in new_groups[1]])

            distances_a.append(distance_a)
            distances_b.append(distance_b)

        distances_a = np.array(distances_a)
        distances_b = np.array(distances_b)

        delta = distances_b - distances_a
        less_than_zero = [d for d in delta if d < 0]
        print("===========")
        print(f"Distance A: {distances_a}")
        print(f"Distance B: {distances_b}")
        print(f"Delta: {delta}")
        if len(less_than_zero) == len(delta):
            print(f"Final Group: {get_print_group(new_groups)}")
            break

        max_index = np.nanargmax(delta)
        max_item = new_groups[1][max_index]
        new_groups[0].append(max_item)
        new_groups[1] = [i for i, _ in enumerate(distance_matrix) if i not in new_groups[0]]
        print(f"New Group: {get_print_group(new_groups)}")

    return new_groups


if __name__ == '__main__':
    distance = np.array([
        [0, 11, 5, 12, 7, 13, 9, 11],
        [11, 0, 13, 2, 17, 4, 15, 20],
        [5, 13, 0, 14, 1, 15, 12, 12],
        [12, 2, 14, 0, 18, 5, 16, 21],
        [7, 17, 1, 18, 0, 20, 15, 17],
        [13, 4, 15, 5, 20, 0, 19, 22],
        [9, 15, 12, 16, 15, 19, 0, 30],
        [11, 20, 12, 21, 17, 22, 30, 0]
    ])

    new_group = polythetic_approach(distance_matrix=distance, distance_func=complete_linkage,
                                    groups=[[], [i for i, _ in enumerate(distance)]])
