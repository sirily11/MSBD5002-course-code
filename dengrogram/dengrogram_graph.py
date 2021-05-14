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
            print(f"Min distance: {round(min_element, 2)}")
            print(f"New Row: {n_rows}")
            print(f"New distance: {np.round(new_distances, 2)}")
            print("New matrix")
            print(np.round(new_matrix, 2))
            i += 1
        except IndexError:
            break


if __name__ == '__main__':
    """
    Draw the dengrogram using agglomerative approach
    """

    distance_func = group_average_linkage

    distances = np.array([
        [0, 11, 5, 12, 7, 13, 9, 11],
        [11, 0, 13, 2, 17, 4, 15, 20],
        [5, 13, 0, 14, 1, 15, 12, 12],
        [12, 2, 14, 0, 18, 5, 16, 21],
        [7, 17, 1, 18, 0, 20, 15, 17],
        [13, 4, 15, 5, 20, 0, 19, 22],
        [9, 15, 12, 16, 15, 19, 0, 30],
        [11, 20, 12, 21, 17, 22, 30, 0]
    ])

    # distances = distance_matrix_generator([(1, 2), (2, 0), (-10, -5), (-5, -2), (10, 12), (8, 6), (-8, -6), (2, 1)],
    #                                       distance_func=euclidean_distance_list)
    print(np.round(distances, 1))
    dendrogram(distance_matrix=distances, distance_func=distance_func,
               rows=[f"{i + 1}" for i, _ in enumerate(distances)])
