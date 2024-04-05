#include <stdio.h>

#define MAX_SIZE 100

int main() {
    int array[MAX_SIZE];
    int size, i;

    printf("Enter the size of the array (up to %d): ", MAX_SIZE);
    scanf_s("%d", &size);

    if (size > MAX_SIZE) {
        printf("Size exceeds the maximum limit of %d.\n", MAX_SIZE);
        return 1;
    }

    printf("Enter %d elements:\n", size);
    for (i = 0; i < size; i++) {
        scanf_s("%d", &array[i]);
    }

    printf("Array elements are:\n");
    for (i = 0; i < size; i++) {
        
        printf("%d ", *(array + i));
    }
    printf("\n");

    return 0;
}
