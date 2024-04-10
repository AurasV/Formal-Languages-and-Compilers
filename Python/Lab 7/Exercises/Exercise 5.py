import numpy as np
import matplotlib.pyplot as plt


def plot_matrices():
    matrix1 = np.random.rand(20)
    matrix2 = np.random.rand(20)
    print("Matrix 1:\n", matrix1)
    print("Matrix 2:\n", matrix2)

    plt.figure(figsize=(10, 5))
    plt.plot(matrix1, label='Matrix 1', color='blue')
    plt.plot(matrix2, label='Matrix 2', color='green')
    plt.title('Random Values Comparison')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot_matrices()
