#include <stdio.h>

int main() {
    double n1, n2;

    printf("First number: ");
    scanf_s("%lf", &n1);
    printf("Second number: ");
    scanf_s("%lf", &n2);

    printf("Sum = %.2lf\n", n1 + n2);
    printf("dif = %.2lf\n", n1 - n2);
    printf("prod = %.2lf\n", n1 * n2);
    printf("div = %.2lf\n", n1 / n2);
    printf("Mean = %.2lf\n", (n1 +n2) / 2);

    return 0;
}
