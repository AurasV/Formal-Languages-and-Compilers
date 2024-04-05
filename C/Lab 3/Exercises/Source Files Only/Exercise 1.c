#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* file;
    char line[100];
    errno_t err;

    err = fopen_s(&file, "example.txt", "r");
    if (err != 0) {
		printf("Error opening file for reading.\n");
		return 1;
	}

    printf("Content of file before appending:\n");
    while (fgets(line, sizeof(line), file) != NULL) {
		printf("%s", line);
	}
    printf("\n");
    fclose(file);

    err = fopen_s(&file, "example.txt", "a");
    if (err != 0) {
        printf("Error opening file for writing.\n");
        return 1;
    }

    fprintf(file, "Appending a line\n");
    fprintf(file, "Appending another line\n");
    fprintf(file, "And another one\n");

    fclose(file);

    err = fopen_s(&file, "example.txt", "r");
    if (err != 0) {
        printf("Error opening file for reading.\n");
        return 1;
    }

    printf("Contents of file after appending:\n");
    while (fgets(line, sizeof(line), file) != NULL) {
        printf("%s", line);
    }

    fclose(file);

    return 0;
}
