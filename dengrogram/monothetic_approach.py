import itertools
from typing import List, Dict

import numpy as np


def dict_to_list(d: Dict, for_which="value") -> List[np.ndarray]:
    li = []
    for k, v in d.items():
        if for_which == "value":
            li.append(v)
        else:
            li.append(k)
    return li


def chisequare(a_arr: np.ndarray, b_arr: np.ndarray):
    a = 0
    b = 0
    c = 0
    d = 0

    for i in range(len(a_arr)):
        if a_arr[i] == b_arr[i] and a_arr[i] == 1:
            a += 1

        elif a_arr[i] == 1 and b_arr[i] == 0:
            c += 1

        elif b_arr[i] == 1 and a_arr[i] == 0:
            b += 1
        else:
            d += 1

    return a, b, c, d


def monithetic_approach(distance_matrix: Dict[str, np.ndarray]):
    """
    divide the data on the basis of the possession of a single specified attribute

    Returns:

    """
    combinations = list(itertools.combinations(range(len(distance_matrix)), 2))
    # Convert dict {"a": [1]} to list [[1]]
    list_of_distance_matrix = dict_to_list(distance_matrix)
    list_of_keys = dict_to_list(distance_matrix, for_which="key")
    chi_values = {}
    for a, b in combinations:
        a_list: np.ndarray = list_of_distance_matrix[a]
        b_list: np.ndarray = list_of_distance_matrix[b]
        a_value, b_value, c_value, d_value = chisequare(a_list, b_list)
        xab = ((a_value * d_value - b_value * c_value) ** 2) * len(list_of_distance_matrix[0]) / (
                (a_value + b_value) * (a_value + c_value) * (b_value + d_value) * (c_value + d_value))
        print(f"X{list_of_keys[a]}{list_of_keys[b]}: {xab}")
        chi_values[f"{list_of_keys[a]}{list_of_keys[b]}"] = xab

    pair_values = {}
    max_key = None
    max_value = 0
    for key, value in distance_matrix.items():
        print(f"For attribute {key}")
        s = 0
        for pair, chi_value in chi_values.items():
            if key in pair:
                s += chi_value

        pair_values[key] = s
        if s > max_value:
            max_value = s
            max_key = key

    print(pair_values)
    print(f"Since {max_key} has the biggest value, we choose {max_key} to seperate the data")

    group_1 = []
    group_2 = []
    for i, v in enumerate(distance_matrix[max_key]):
        if v == 1:
            group_1.append(i + 1)
        else:
            group_2.append(i + 1)
    print(f"Group 1: {group_1}")
    print(f"Group 2: {group_2}")

    return group_1, group_2


if __name__ == '__main__':
    m = {
        "a": np.array([1, 1, 1, 0]),
        "b": np.array([1, 1, 0, 0]),
        "c": np.array([0, 0, 1, 1])
    }

    monithetic_approach(m)
