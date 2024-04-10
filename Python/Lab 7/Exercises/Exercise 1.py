import numpy as np


def create_matrix():
    matrix = np.random.randint(0, 101, size=(5, 5))
    print(matrix)


if __name__ == "__main__":
    create_matrix()
