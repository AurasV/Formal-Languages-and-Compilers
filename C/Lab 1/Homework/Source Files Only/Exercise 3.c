#include <stdio.h>

#define MAX_SIZE 100  // Maximum size for our 2D arrays

int main() {
    int rows, cols;
    int arr1[MAX_SIZE][MAX_SIZE], arr2[MAX_SIZE][MAX_SIZE];
    int equal = 1;

    printf("Enter the number of rows (max 100): ");
    scanf_s("%d", &rows);
    printf("Enter the number of columns (max 100): ");
    scanf_s("%d", &cols);

    if (rows > MAX_SIZE || cols > MAX_SIZE) {
        printf("Error: The number of rows or columns exceeds the maximum allowed size of 100.\n");
        return 1;
    }

    printf("Enter elements for the first array:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("arr1[%d][%d] = ", i, j);
            scanf_s("%d", &arr1[i][j]);
        }
    }

    printf("Enter elements for the second array:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("arr2[%d][%d] = ", i, j);
            scanf_s("%d", &arr2[i][j]);
        }
    }

    for (int i = 0; i < rows && equal; i++) {
        for (int j = 0; j < cols; j++) {
            if (arr1[i][j] != arr2[i][j]) {
                equal = 0;
                break;
            }
        }
    }

    if (equal) {
        printf("The two arrays are equal.\n");
    }
    else {
        printf("The two arrays are not equal.\n");
    }

    return 0;
}
