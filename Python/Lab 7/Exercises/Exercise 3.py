import numpy as np


def second_largest_in_columns(matrix):
    return np.sort(matrix, axis=0)[-2]


if __name__ == "__main__":
    matrix = np.random.randint(0, 101, size=(5, 5))
    print("Original Matrix:\n", matrix)
    second_largest_values = second_largest_in_columns(matrix)
    print("Second-Largest Values in Each Column:\n", second_largest_values)
