#include <stdio.h>
#include <ctype.h>
#include <errno.h>

int main() {
    FILE* file, * tempFile;
    char ch;
    errno_t errRead, errWrite;

    errRead = fopen_s(&file, "change.txt", "r");
    if (errRead != 0 || file == NULL) {
        printf("Error opening file for reading.\n");
        return 1;
    }

    errWrite = fopen_s(&tempFile, "tempfile.txt", "w");
    if (errWrite != 0 || tempFile == NULL) {
        printf("Error opening temp file for writing.\n");
        fclose(file);
        return 1;
    }

    while ((ch = fgetc(file)) != EOF) {
        if (islower(ch))
            fputc(toupper(ch), tempFile);
        else if (isupper(ch))
            fputc(tolower(ch), tempFile);
        else
            fputc(ch, tempFile);
    }

    fclose(file);
    fclose(tempFile);

    remove("change.txt");
    if(rename("tempfile.txt", "change.txt"))
        printf("Error renaming file.\n");
	else
        printf("Changes complete.\n");

    return 0;
}
