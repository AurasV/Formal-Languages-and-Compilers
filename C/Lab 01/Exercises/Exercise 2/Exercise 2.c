#include <stdio.h>

int main() {
    int number;
    printf("Enter a number: ");
    scanf_s("%d", &number);
    
    int sign = (number > 0) - (number < 0);

    switch (sign) {
        case 1:
            printf("The number is positive.\n");
            break;
        case -1:
            printf("The number is negative.\n");
            break;
        case 0:
            printf("The number is zero.\n");
            break;
        default:
            printf("Error: Invalid input.\n");
    }
    
    return 0;
}
