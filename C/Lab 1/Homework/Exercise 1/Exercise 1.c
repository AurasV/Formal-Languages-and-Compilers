#include <stdio.h>

int main() {
    int n, i, x, found = 0;

    printf("Enter the size of the array: ");
    scanf_s("%d", &n);

    int arr[100];

    printf("Enter %d elements of the array: ", n);
    for (i = 0; i < n; i++) {
        scanf_s("%d", &arr[i]);
    }

    printf("Enter the element to search for: ");
    scanf_s("%d", &x);

    for (i = 0; i < n; i++) {
        if (arr[i] == x) {
            found = 1; 
            break;
        }
    }

    if (found) {
        printf("%d is in the array.\n", x);
    }
    else {
        printf("%d is not in the array.\n", x);
    }

    return 0;
}
