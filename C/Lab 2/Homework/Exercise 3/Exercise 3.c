#include <stdio.h>

int fibonacci(int n) {
    if (n == 1 || n == 2) {
        return 1;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int length, i;

    printf("Length of the Fibonacci series: ");
    scanf_s("%d", &length);

    if (length <= 0) {
        printf("Enter positive integer.\n");
        return 1;
    }

    printf("Fibonacci Series up to %d positions:\n", length);
    for (i = 1; i <= length; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    return 0;
}
