#include <stdio.h>

int main() {
    int sum = 0;

    for (int i = 1; i <= 20; i += 2) {
        sum += i;
    }

    printf("The sum of all odd numbers between 0 and 20 is: %d\n", sum);

    return 0;
}
