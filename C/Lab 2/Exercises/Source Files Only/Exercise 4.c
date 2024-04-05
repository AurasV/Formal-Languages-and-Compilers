#include <stdio.h>

double square(double n) {
    return n * n;
}

int main() {
    double n;

    printf("Enter your number: ");
    scanf_s("%lf", &n);

    printf("Square of %.2lf is %.2lf\n", n, square(n));
    printf("Square of %.2lf is %.2lf\n", square(n), square(square(n)));

    return 0;
}
