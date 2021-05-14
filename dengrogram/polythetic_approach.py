import numpy as np
from typing import List
from copy import deepcopy
from dengrogram.distance.distances import complete_linkage, group_average_linkage


def get_print_group(groups):
    return [[e + 1 for e in group] for group in groups]


def polythetic_approach(distance_matrix: np.ndarray, distance_func, groups: List[List]):
    """
    divide the data based on the values by all attributes

    Args:
        distance_matrix:
        distance_func:
        groups:

    Returns:

    """
    print(groups)
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
        print(f"Distance A: {np.round(distances_a, 2)}")
        print(f"Distance B: {np.round(distances_b, 2)}")
        print(f"Delta: {np.round(delta, 2)}")
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
        [0, 10, 7, 30, 29, 38, 42],
        [10, 0, 7, 23, 25, 34, 36],
        [7, 7, 0, 21, 22, 31, 36],
        [30, 23, 21, 0, 7, 10, 13],
        [29, 25, 22, 7, 0, 11, 7],
        [38, 34, 31, 10, 11, 0, 9],
        [42, 36, 36, 13, 17, 9, 0]
    ])

    new_group = polythetic_approach(distance_matrix=distance, distance_func=group_average_linkage,
                                    groups=[[], [i for i, _ in enumerate(distance)]])
