import numpy as np


def count_unique_values(array):
    unique_values, counts = np.unique(array, return_counts=True)
    return dict(zip(unique_values, counts))


if __name__ == "__main__":
    array = np.random.randint(0, 101, size=100)
    print("Array:\n", array)
    unique_values_counts = count_unique_values(array)
    print("Unique Values and Their Counts:\n", unique_values_counts)
