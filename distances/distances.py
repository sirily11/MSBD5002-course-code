import numpy as np


def group_average_linkage(points: np.ndarray) -> float:
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.mean(normalized_points)


def complete_linkage(points: np.ndarray) -> float:
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.max(normalized_points)


def single_linkage(points: np.ndarray) -> float:
    if len(points) == 0:
        return 0
    normalized_points = [p for p in points if p != 0]
    return np.min(normalized_points)
