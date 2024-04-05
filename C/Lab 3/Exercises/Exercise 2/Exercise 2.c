#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

int main() {
    FILE* file1, * file2;
    char line1[1024], line2[1024];
    errno_t err1, err2;
    int same = 1;

    err1 = fopen_s(&file1, "file1.txt", "r");
    if (err1 != 0) {
        printf("Can't open file1.txt\n");
        return 1;
    }

    err2 = fopen_s(&file2, "file2.txt", "r");
    if (err2 != 0) {
        printf("Can't open file2.txt\n");
        fclose(file1);
        return 1;
    }

    while (fgets(line1, sizeof(line1), file1) != NULL && fgets(line2, sizeof(line2), file2) != NULL) {
        if (strcmp(line1, line2) != 0) {
            same = 0;
            break;
        }
    }

    if (same && (fgets(line1, sizeof(line1), file1) != NULL || fgets(line2, sizeof(line2), file2) != NULL)) {
        same = 0;
    }

    if (same) {
        printf("Same content\n");
    }
    else {
        printf("NOT same content\n");
    }

    fclose(file1);
    fclose(file2);

    return 0;
}
