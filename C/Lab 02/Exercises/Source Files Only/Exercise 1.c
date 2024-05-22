#include <stdio.h>

int main() {
    int n1, n2;
    int* ptr1 = &n1;
    int* ptr2 = &n2;

    printf("First number: ");
    scanf_s("%d", ptr1);

    printf("Second number: ");
    scanf_s("%d", ptr2);


    printf("Sum of %d and %d = %d\n", *ptr1, *ptr2, *ptr1 + *ptr2);

    return 0;
}
