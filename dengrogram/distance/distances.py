import numpy as np
from typing import Tuple, List
from scipy.spatial import distance
from itertools import permutations


def group_average_linkage(points: np.ndarray) -> float:
    """
    The distance between two clusters is defined as the average of the distances between all pairs of records (one from each cluster).


    Calculate distance from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.mean(normalized_points)


def complete_linkage(points: np.ndarray) -> float:
    """
    The distance between two clusters is given by the distance between their most distant members

    Calculate distance from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.max(normalized_points)


def single_linkage(points: np.ndarray) -> float:
    """
    Nearest neighbor
    Calculate distance from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.min(normalized_points)


def centroid_linkage(points: np.ndarray) -> float:
    """
    The distance between two clusters is defined as
    the distance between the mean vectors of the two clusters.
    Calculate distance from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.mean(normalized_points)


def median_linkage(points: np.ndarray) -> float:
    """
    Disadvantage of the Centroid Clustering:
     When a large cluster is merged with a small one,
     the centroid of the combined cluster would be closed to the large one,
     ie. The characteristic properties of the small one are lost
    After we have combined two groups,
    the mid-point of the original two cluster centres
    is used as the centre of the newly combined group

    Calculate distance from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.median(normalized_points)


def calculate_distance_from_array(distance_array: np.ndarray, index: int) -> float:
    return distance_array[index]


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]):
    """
    Calculate distance between two points with x and y coordinate
    """
    return distance.euclidean(point1, point2)


def euclidean_distance_list(points: List[Tuple[int, int]]) -> float:
    """
    Lists version of euclidean distance. Similar to single linkage's usage
    Args:
        points:

    Returns:

    """
    return distance.euclidean(points[0], points[1])


def distance_matrix_generator(points: List[Tuple[int, int]], distance_func) -> np.ndarray:
    """
    Generate a distance matrix by points
    Args:
        points: [(1, 2), (3, 4)]
        distance_func: Which distance function you want to use. Single linkage for example

    Returns: a distance matrix

    """
    length = len(points)
    arr = np.zeros((length, length))
    for i in range(length):
        for j in range(length):
            pts = [points[i], points[j]]
            dis = distance_func(pts)
            arr[i][j] = dis
    return arr


if __name__ == '__main__':
    distance_matrix = distance_matrix_generator([(1, 2), (2, 2), (5, 2), (6, 1)],
                                                distance_func=euclidean_distance_list)
    print(distance_matrix)
