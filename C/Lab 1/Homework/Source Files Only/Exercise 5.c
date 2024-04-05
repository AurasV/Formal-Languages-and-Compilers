#include <stdio.h>
#include <string.h>

int main() {
    char ex[256];
    const char word[] = "FILS";

    printf("Enter a phrase: ");
    fgets(ex, sizeof(ex), stdin);

    ex[strcspn(ex, "\n")] = 0;

    char* p = ex;
    int found = 0;

    while ((p = strstr(p, word)) != NULL) {
        found = 1;
        printf("Found '%s' at index: %ld\n", word, (long)(p - ex));
        p++; 
    }

    if (!found) {
        printf("The word '%s' was not found in the entered phrase.\n", word);
    }

    return 0;
}
