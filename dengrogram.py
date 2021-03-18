import numpy as np
from distances import group_average_linkage, complete_linkage, single_linkage
from copy import deepcopy


def find_min_element(distance_matrix):
    min_index = (0, 0)
    min_element = 100000000

    for i, row in enumerate(distance_matrix):
        for j, element in enumerate(row):
            if element != 0 and element < min_element:
                min_index = (i, j)
                min_element = element
    return min_index, min_element


def dendrogram(distance_matrix: np.ndarray, distance_func, rows):
    new_matrix = deepcopy(distance_matrix)
    n_rows = deepcopy(rows)
    while True:
        try:
            min_index, min_element = find_min_element(new_matrix)
            x, y = new_matrix[min_index[0]], new_matrix[min_index[1]]

            new_distances = [distance_func(d) for index, d in enumerate(zip(x, y)) if index != min_index[1]]
            new_distances[min_index[0]] = 0
            new_distances = np.array(new_distances)

            new_matrix = np.delete(new_matrix, min_index[0], 1)
            new_matrix = np.delete(new_matrix, min_index[1], 0)

            new_matrix[min_index[0]] = new_distances
            new_matrix[:, min_index[1] - 1] = new_distances
            n_rows[min_index[0]] = n_rows[min_index[0]] + n_rows[min_index[1]]
            del n_rows[min_index[1]]

            print("================")
            print(f"Merge: {min_index}")
            print(f"New Row: {n_rows}")
            print(f"New distance: {new_distances}")
            print("New matrix")
            print(new_matrix)
        except IndexError:
            break


if __name__ == '__main__':
    distances = np.array([
        [0, 2, 6, 10, 9],
        [2, 0, 5, 9, 8],
        [6, 5, 0, 4, 5],
        [10, 9, 4, 0, 3],
        [9, 8, 5, 3, 0]
    ])

    dendrogram(distance_matrix=distances, distance_func=single_linkage,
               rows=[f"{i + 1}" for i, _ in enumerate(distances)])
