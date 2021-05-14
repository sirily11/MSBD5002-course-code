import numpy as np
from typing import List, Dict, Tuple
from pprint import pprint


def print_points(points):
    if type(points) == list:
        return [p + 1 for p in points]
    elif type(points) == dict:
        t = {}
        for k, v, in points.items():
            t[k + 1] = [p + 1 for p in v]
        return t


def find_group_by_pt(groups: Dict[int, set], pt: int) -> Tuple[bool, int]:
    index = -1
    for k, v in groups.items():
        index = k
        if pt in v:
            return True, k

    return False, index + 1


def dbscan(distance_matrix: np.ndarray, distance=2, min_pts=6):
    core_pts = []
    border = []
    outlier = []
    others = []
    # A dict contains pts index and all its neighborhoods
    neighborhoods_dict: Dict[int, List[int]] = {

    }

    groups: Dict[int: set] = {}

    for index, row in enumerate(distance_matrix):
        # get distance except itself
        distances = [e for i, e in enumerate(row) if i != index]
        pts = [i for i, _ in enumerate(row) if i != index]
        within_the_range: List[bool] = [True if d <= distance else False for d in distances]
        neighborhoods = [e for i, e in enumerate(pts) if within_the_range[i]]
        neighborhoods_dict[index] = neighborhoods

        if len(neighborhoods) >= min_pts:
            core_pts.append(index)
        else:
            others.append(index)

    for pt in core_pts:
        neighborhoods = neighborhoods_dict[pt]
        exist, index = find_group_by_pt(groups, pt)
        if exist:
            groups[index].add(pt)
        else:
            groups[index] = {pt}

        for neighbor in neighborhoods:
            if neighbor in core_pts:
                groups[index].add(neighbor)

    for pt, neighborhoods in neighborhoods_dict.items():
        if pt not in core_pts:
            is_outlier = True
            for neighborhood in neighborhoods:
                if neighborhood in core_pts:
                    exist, index = find_group_by_pt(groups, neighborhood)
                    border.append(pt)
                    groups[index].add(pt)
                    is_outlier = False
                    break
            if is_outlier:
                outlier.append(pt)

    print("Groups: ")
    pprint(print_points(groups))
    print(f"Core points: {print_points(core_pts)}")
    print(f"Border points: {print_points(border)}")
    print(f"Outliers: {print_points(outlier)}")
    print("Neighborhoods")
    pprint(print_points(neighborhoods_dict))


if __name__ == '__main__':
    distance = np.array([
        [0, 1, 2, 11, 12],
        [1, 0, 1, 11, 11],
        [2, 1, 0, 9, 10],
        [11, 11, 9, 0, 9],
        [12, 11, 10, 9, 0]
    ])

    new_group = dbscan(distance_matrix=distance, distance=10, min_pts=2)
