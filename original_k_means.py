from typing import Tuple, List
from scipy.spatial import distance
import numpy as np
import matplotlib.pyplot as plt
from distances import calculate_distance


def calculate_new_center(points: List[Tuple[int, int]]):
    x = sum([p[0] for p in points]) / len(points)
    y = sum([p[1] for p in points]) / len(points)
    return x, y


def k_means(points: List[Tuple[int, int]], initial_centers: List[Tuple[int, int]]):
    distances = [[calculate_distance(p, center) for center in initial_centers] for p in points]
    clusters = [np.argmin(d) for d in distances]
    groups: List[Tuple[int, int]] = [[] for c in initial_centers]
    for i, cluster in enumerate(clusters):
        group = groups[cluster]
        group.append(points[i])
        groups[cluster] = group

    new_centers = [calculate_new_center(g) for g in groups]
    print("Cluster index")
    print(clusters)
    print("New group")
    print(groups)
    print("New centers")
    print(new_centers)

    return groups, new_centers


def sequential_k_means(point: Tuple[int, int], initial_centers: List[Tuple[int, int]], initial_numbers: List[int]):
    distances = [calculate_distance(center, point) for center in initial_centers]
    cluster = np.argmin(distances)
    groups: List[Tuple[int, int]] = [[] for c in initial_centers]
    groups[cluster].append(point)

    new_centers = [c for c in initial_centers]
    initial_x = initial_centers[cluster][0]
    initial_y = initial_centers[cluster][1]
    x = point[0]
    y = point[1]
    new_numbers = [n for n in initial_numbers]
    new_numbers[cluster] = new_numbers[cluster] + 1

    new_x = initial_x + (x - initial_x) / new_numbers[cluster]
    new_y = initial_y + (y - initial_y) / new_numbers[cluster]

    new_centers[cluster] = (new_x, new_y)
    print(f"Point: {point}")
    print("group")
    print(cluster)
    print("New centers")
    print(new_centers)

    return groups, new_centers, new_numbers


def draw_scatter(groups: List[Tuple[int, int]]):
    for i, points in enumerate(groups):
        x = [p[0] for p in points]
        y = [p[1] for p in points]
        plt.scatter(x, y, label=f"group {i}")

    plt.legend()
    plt.show()


if __name__ == '__main__':
    # ps = [(65, 60), (53, 60), (65, 62), (53, 64), (68, 63), (51, 57), (60, 51), (60, 80)]
    # ic = [(60, 51), (60, 80), (53, 60), (65, 60)]

    ps = [(0, 0), (1, 1), (0.75, 0), (0.25, 0)]
    ic = [(0, 0.5), (1, 0.5)]
    init_numbers = [0, 0]
    groups, new_centers, init_numbers = sequential_k_means(ps[0], ic, init_numbers)
    print("======")
    groups, new_centers, init_numbers = sequential_k_means(ps[1], new_centers, init_numbers)
    print("======")
    groups, new_centers, init_numbers = sequential_k_means(ps[2], new_centers, init_numbers)
    print("======")
    groups, new_centers, init_numbers = sequential_k_means(ps[3], new_centers, init_numbers)
    draw_scatter(groups)
