from typing import List, Dict, Tuple
import numpy as np
from pprint import pprint
from ast import literal_eval as make_tuple
from itertools import combinations


def generate_counts(ranges: Dict[str, List[Tuple[int, int]]],
                    num_dim: int, num_groups: int):
    """
    Generate a large item set
    Args:
        ranges:
        num_dim:
        threshold:
        num_points:

    Returns: results and the large item set. Results will be [[(0, 1)],[],[]].
    the first value is which group and the second one is the count

    """
    d: Dict[str, int] = {}
    for key, values in ranges.items():
        for value in values:
            if str(value) not in d:
                d[str(value)] = 0
            d[str(value)] = d[str(value)] + 1
    results: List[List[Tuple[int, int]]] = [[] for i in range(num_dim)]

    for key, value in d.items():
        axis, group = make_tuple(key)
        results[axis].append((group, value))

    return results


def generate_large_item_set(counts: List[List[Tuple[int, int]]], size: int):
    results = []
    com = list(combinations(range(len(counts)), size))
    print(com)
    for i, item in enumerate(counts):
        if len(item) > 0:
            results.append(i)

    return results


def find_dense_unit_for_subspace(points: List[List[float]], threshold: float, range_list: List[float],
                                 d_names=None):
    """
    Find Dense unit for given subspace and range. Implementation is not finished
    Args:
        points: List of points. For example [[11, 13, 5], [2, 10, 20]]
        threshold: Threshold value. For example, 0.2
        range_list: Range list. For example, [0, 10, 20, 30] will create a range between 0 and 30
        d_names: Dimension's name. For example "x", "y", "z"


    Returns:

    """
    if d_names is None:
        d_names = ["x", "y", "z"]

    num_dims = len(points[0])
    num_ranges = len(range_list) - 1
    num_points = len(points)
    # A dict contains point and its category. For example, [11, 13, 5] with [(0, 2), (1, 2), (2, 1)] means
    # it belongs to x_2, y_2, z_1
    ranges: Dict[str, List[Tuple[int, int]]] = {}

    for i in range(num_dims):
        for index, point in enumerate(points):
            current_value = point[i]
            for j in range(num_ranges):
                start = range_list[j]
                end = range_list[j + 1]
                if start <= current_value < end:
                    if str(point) not in ranges:
                        ranges[str(point)] = []

                    ranges[str(point)].append((i, j + 1))
                    break
    print("Map: [point axis]: [(dimension, group: start from 1)]")
    for key, value in ranges.items():
        vs = [(d_names[axis], group) for axis, group in value]
        print(f"{key}: {vs}")
    size = 1
    counts = generate_counts(ranges, num_dim=num_dims, num_groups=num_ranges)
    print(f"counts, we need to find the count > {threshold * num_points}")
    pprint(counts)
    print("Density map")
    for i, group in enumerate(counts):
        pts = [(g, count / num_points) for g, count in group]
        pts.sort(key=lambda k: k[0])
        print(f"{d_names[i]}: {pts}")
    # # print(counts)
    # while True:
    #     print("=================")
    #     print(f"Large {size} item set")
    #
    #     large_item_set = generate_large_item_set(counts, size)
    #     print([d_names[i] for i in large_item_set])
    #
    #     break


if __name__ == '__main__':
    pts = [[11, 13, 5], [12, 11, 21], [11, 17, 27], [13, 14, 38], [22, 37, 36],
           [24, 31, 27], [25, 35, 21], [29, 34, 4], [35, 5, 4], [36, 6, 5]]

    find_dense_unit_for_subspace(pts, threshold=0.4, range_list=[0, 10, 20, 30, 40])
