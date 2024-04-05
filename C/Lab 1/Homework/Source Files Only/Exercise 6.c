#include <stdio.h>
#include <string.h>

int main() {
    char str[256], rev[256];
    int i, length, isPalindrome = 1;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    str[strcspn(str, "\n")] = 0;

    length = strlen(str);

    for (i = 0; i < length; i++) {
        rev[i] = str[length - 1 - i];
    }
    rev[i] = '\0';

    isPalindrome = (strcmp(str, rev) == 0);

    if (isPalindrome) {
        printf("The string is a palindrome.\n");
    }
    else {
        printf("The string is not a palindrome.\n");
    }

    return 0;
}
