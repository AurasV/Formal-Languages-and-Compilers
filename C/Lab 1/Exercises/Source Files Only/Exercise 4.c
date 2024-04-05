#include <stdio.h>

int main() {
    int x, no_digits = 0;
    printf("Enter an integer: ");
    scanf("%d", &x);

    if (x < 0) {
        x *= -1;
    }

    if (x == 0) {
        no_digits = 1;
    } else {
        while (x > 0) {
            x /= 10;
            no_digits++;
        }
    }

    printf("Number of digits: %d\n", no_digits);

    return 0;
}
