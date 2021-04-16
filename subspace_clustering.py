from math import sqrt
from typing import List, Tuple, Optional
from scipy.special import xlogy
import numpy as np
from pprint import pprint
from sympy import Symbol, Matrix, MatrixSymbol, summation
from sympy.stats import Covariance


def kl_transform(points: List[Tuple], k=1):
    """
    Compute kl transform based on list of points
    Args:
        points: list of points
        k: target number

    Returns:

    """
    print("================================")
    print("Step 1, calculate the mean vector")
    mean_vector = tuple([float(sum(li)) / len(li) for li in zip(*points)])
    differences = [tuple([element - mean_vector[i] for i, element in enumerate(point)]) for point in points]
    print(f"Mean vector: {mean_vector}")
    print(f"Difference from mean vector: {differences}")
    print("================================")
    print("Step 2, obtain the covariance matrix")
    y: Optional[np.ndarray] = None
    for difference in differences:
        da = np.array(difference).reshape(-1, 1)
        if y is None:
            y = da
        else:
            y = np.hstack((y, da))
    cov_matrix = 1 / len(points) * y.dot(y.T)
    print(f"y matrix:\n{y}")
    print(f"Covariance matrix:\n{cov_matrix}")

    print("================================")
    print("Step 3, find the eigenvalues and eigenvectors of covariance matrix")
    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    # a list where first element is eigenvalues and second element is eigenvectors
    value_vectors = list(zip(eigenvalues, eigenvectors))
    print("Eigenvalue: Eigenvector")
    pprint(value_vectors)
    print("================================")
    print("Step 4, rearrange the eigenvectors in descending order of the eigenvalues")
    value_vectors.sort(key=lambda e: e[0], reverse=True)
    phi: Optional[np.ndarray] = None
    for value_vector in value_vectors:
        vec = value_vector[1].reshape(-1, 1)
        if phi is None:
            phi = vec
        else:
            phi = np.hstack((vec, phi))
    print(f"Phi:\n{phi}")
    print("================================")
    print("Step 5, transform the given L-dimensional vectors by eigenvector matrix")
    result = []
    for p in points:
        x = np.array(p).reshape(-1, 1)
        a = phi.T.dot(x)
        result.append(a)
        print(f"{p} -> {a}")

    print("================================")
    print("Step 6, keep only the k values corresponding to the smallest k eigenvalues")
    eigenvalues_with_index = [(i, e) for i, e in enumerate(value_vectors)]
    eigenvalues_with_index = sorted(eigenvalues_with_index, key=lambda e: e[1])
    target_idx = [i for i, e in eigenvalues_with_index][:k]
    # noinspection PyUnresolvedReferences
    final_results = [np.around(r[target_idx[0]:target_idx[-1] + 1], 3) for r in result]
    print("Final Result")
    pprint(final_results)

    return final_results


def kl_transform_with_symbol(points: List[Tuple], symbol, k=1, to_value=2):
    """
    Compute kl transform with sympy
    Args:
        to_value: Replace sympy symbol to what value
        symbol: sympy symbol
        points: list of points. Can contain symbol like x
        k: target number

    Returns:

    """
    print("================================")
    print("Step 1, calculate the mean vector")
    mean_vector = tuple([sum(li) / len(li) for li in zip(*points)])
    differences = [tuple([element - mean_vector[i] for i, element in enumerate(point)]) for point in points]
    print(f"Mean vector: {mean_vector}")
    print(f"Difference from mean vector: {differences}")
    print("================================")
    print("Step 2, obtain the covariance matrix")
    y: Optional[Matrix] = None
    for difference in differences:
        da = Matrix(difference)
        if y is None:
            y = da
        else:
            y = Matrix.hstack(y, da)
    cov_matrix = (1 / len(points)) * (y * y.T)
    print(f"y matrix:\n{y}")
    print(f"Covariance matrix:\n{cov_matrix}")

    print("================================")
    print("Step 3, find the eigenvalues and eigenvectors of covariance matrix")
    eigenvectors = cov_matrix.eigenvects()
    # a list where first element is eigenvalues and second element is eigenvectors
    value_vectors = [(e[0], e[2]) for e in eigenvectors]
    print("================================")
    print("Step 4, rearrange the eigenvectors in descending order of the eigenvalues")
    phi: Optional[Matrix] = None
    try:
        value_vectors.sort(key=lambda e: e[0], reverse=True)
    except:
        value_vectors.sort(key=lambda e: e[0].subs(symbol, to_value), reverse=True)

    print("Eigenvalue: Eigenvector")
    print(value_vectors)
    for value_vector in value_vectors:
        vec = value_vector[1]
        for v in vec:
            if phi is None:
                phi = -v
            else:
                phi = Matrix.hstack(phi, -v)
    print(f"Phi:\n{phi}")
    print("================================")
    print("Step 5, transform the given L-dimensional vectors by eigenvector matrix")
    result = []
    for p in points:
        x = Matrix(p)
        a = phi.T * x
        print(f"{p} -> {a}")
        result.append(a)

    print("================================")
    print("Step 6, keep only the k values corresponding to the smallest k eigenvalues")
    eigenvalues_with_index = [(i, e[0]) for i, e in enumerate(value_vectors)]
    try:
        eigenvalues_with_index.sort(key=lambda e: e[1])
    except Exception:
        eigenvalues_with_index.sort(key=lambda e: e[1].subs(symbol, to_value))
    target_idx = [i for i, e in eigenvalues_with_index][:k]
    # noinspection PyUnresolvedReferences
    final_results = [r[target_idx[0]:target_idx[-1] + 1] for r in result]
    print("Final Result")
    pprint(final_results)

    return final_results


if __name__ == '__main__':
    # pts = [(3, 3), (0, 2), (-1, -1), (2, 0)]
    c = Symbol("c")
    d = c + 5
    pts1 = [(7 + c, 7 + c), (9 + c, 9 + c), (6 + c, 10 + c), (10 + c, 6 + c)]
    pts2 = [(7 - d, 7 - d), (9 - d, 9 - d), (6 - d, 10 - d), (10 - d, 6 - d)]
    pts3 = [(7 * c, 7 * c), (9 * c, 9 * c), (6 * c, 10 * c), (10 * c, 6 * c)]
    # r1 = kl_transform_with_symbol(pts1)
    # r2 = kl_transform_with_symbol(pts2)

    r3 = kl_transform_with_symbol(pts2, symbol=c, to_value=1)
    print()
    # print(r1[0][0] / r2[0][0])
