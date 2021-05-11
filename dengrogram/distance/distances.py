import numpy as np
from typing import Tuple
from scipy.spatial import distance


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
