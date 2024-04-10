import numpy as np


def sort_matrix_rows(m):
    sorted_matrix = np.sort(m, axis=1)
    return sorted_matrix


if __name__ == "__main__":
    matrix = np.random.randint(0, 101, size=(5, 5))
    print("Original Matrix:\n", matrix)
    sorted = sort_matrix_rows(matrix)
    print("Sorted Matrix Rows:\n", sorted)
