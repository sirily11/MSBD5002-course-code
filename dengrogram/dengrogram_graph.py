import numpy as np
from copy import deepcopy
from dengrogram import single_linkage, median_linkage, group_average_linkage, euclidean_distance_list, \
    distance_matrix_generator


def find_min_element(distance_matrix):
    min_index = (0, 0)
    min_element = 100000000

    for i, row in enumerate(distance_matrix):
        for j, element in enumerate(row):
            if element != 0 and element < min_element:
                if i < j:
                    min_index = (i, j)
                else:
                    min_index = (j, i)
                min_element = element
    return min_index, min_element


def dendrogram(distance_matrix: np.ndarray, distance_func, rows):
    new_matrix = deepcopy(distance_matrix)
    n_rows = deepcopy(rows)
    print("Use min distance when you are drawing dendrogram")
    i = 1
    while True:
        try:
            min_index, min_element = find_min_element(new_matrix)
            x, y = new_matrix[min_index[0]], new_matrix[min_index[1]]

            new_distances = [distance_func(d) for index, d in enumerate(zip(x, y)) if index != min_index[1]]
            new_distances[min_index[0]] = 0
            new_distances = np.array(new_distances)

            new_matrix = np.delete(new_matrix, min_index[1], 1)
            new_matrix = np.delete(new_matrix, min_index[1], 0)

            # replace with new distances
            new_matrix[min_index[0]] = new_distances
            new_matrix[:, min_index[0]] = new_distances
            n_rows[min_index[0]] = n_rows[min_index[0]] + n_rows[min_index[1]]
            del n_rows[min_index[1]]

            print("================")
            print(f"Step: {i}")
            print(f"Merge (start from 0): {min_index}")
            print(f"Min distance: {min_element}")
            print(f"New Row: {n_rows}")
            print(f"New distance: {np.round(new_distances, 1)}")
            print("New matrix")
            print(np.round(new_matrix, 1))
            i += 1
        except IndexError:
            break


if __name__ == '__main__':
    """
    Draw the dengrogram using agglomerative approach
    """

    distance_func = median_linkage

    # distances = np.array([
    #     [0, 2, 6, 10, 9],
    #     [2, 0, 5, 9, 8],
    #     [6, 5, 0, 4, 5],
    #     [10, 9, 4, 0, 3],
    #     [9, 8, 5, 3, 0]
    # ])

    distances = distance_matrix_generator([(1, 2), (2, 0), (-10, -5), (-5, -2), (10, 12), (8, 6), (-8, -6), (2, 1)],
                                          distance_func=euclidean_distance_list)
    print(np.round(distances, 1))
    dendrogram(distance_matrix=distances, distance_func=distance_func,
               rows=[f"{i + 1}" for i, _ in enumerate(distances)])
