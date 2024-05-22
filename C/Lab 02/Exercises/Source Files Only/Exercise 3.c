#include <stdio.h>

int isEven(int n) {
    return (n % 2 == 0);
}

int main() {
    int n;

    printf("Enter your number: ");
    scanf_s("%d", &n);

    if (isEven(n)) {
        printf("%d = even\n", n);
    }
    else {
        printf("%d = odd\n", n);
    }

    return 0;
}
