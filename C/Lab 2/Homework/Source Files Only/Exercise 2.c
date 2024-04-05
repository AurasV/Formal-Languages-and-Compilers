#include <stdio.h>

int isPerfect(int n) {
    int sum = 0;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) {
            sum += i;
        }
    }
    if (sum == n && n != 0) {
        return 1;
    }
    else {
        return 0;
    }
}

void displayPerfectNumbers(int start, int end) {
    printf("Perfect numbers in interval %d to %d:\n", start, end);
    for (int i = start; i <= end; i++) {
        if (isPerfect(i)) {
            printf("%d\n", i);
        }
    }
}

int main() {
    int start, end;

    printf("Start of interval: ");
    scanf_s("%d", &start);
    printf("End of interval: ");
    scanf_s("%d", &end);

    displayPerfectNumbers(start, end);

    return 0;
}
