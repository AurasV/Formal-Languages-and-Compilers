#include <stdio.h>

int main() {
    int arr[100];
    int n, sum = 0;

    printf("Enter the number of elements in the array: ");
    scanf("%d", &n);

    if (n > 100) {
        printf("Error: Cannot enter more than 100 elements.\n");
        return 1; 
    }

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]); 
    }

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }

    printf("The sum of all elements in the array is: %d\n", sum);

    return 0;
}
