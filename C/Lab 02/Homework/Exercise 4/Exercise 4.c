#include <stdio.h>

long long factorial(int n) {
    if (n == 0) return 1;

    return n * factorial(n - 1);
}

int main() {
    int number;
    long long result;

    printf("Positive integer: ");
    scanf_s("%d", &number);

    if (number < 0) {
        printf("Factorial of negative number doesn't exist.\n");
        return 1;
    }

    result = factorial(number);

    printf("Factorial of %d = %lld\n", number, result);

    return 0;
}


