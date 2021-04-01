import numpy as np
from typing import Tuple

def group_average_linkage(points: np.ndarray) -> float:
    """
    Calculate distances from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.mean(normalized_points)


def complete_linkage(points: np.ndarray) -> float:
    """
    Calculate distances from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.max(normalized_points)


def single_linkage(points: np.ndarray) -> float:
    """
    Calculate distances from the points array
    """
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.min(normalized_points)


def calculate_distance_from_array(distance_array: np.ndarray, index: int) -> float:
    return distance_array[index]


def calculate_distance(point1: Tuple[int, int], point2: Tuple[int, int]):
    """
    Calculate distance between two points with x and y coordinate
    """
    return distance.euclidean(point1, point2)
