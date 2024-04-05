%{
#include <stdio.h>

FILE *inputFile, *outputFile;
int line_num = 1;
%}

%%

\n  { fprintf(outputFile, " %d\n", line_num++); } 
[^ \n]+  { fprintf(outputFile, "%s", yytext); }

%%

int yywrap() {
    return 1;
}

int main() {
    inputFile = fopen("InputEx2.txt", "r");
    if (inputFile == NULL) {
        perror("Error opening InputEx2.txt");
        return 1;
    }
    outputFile = fopen("output.txt", "w");
    if (outputFile == NULL) {
        perror("Error opening output.txt");
        fclose(inputFile);
        return 1;
    }

    yyin = inputFile;
    
    int at_start_of_line = 1;

    char c;
    while ((c = fgetc(inputFile)) != EOF) {
        if (at_start_of_line) {
            at_start_of_line = 0;
        } else if (c == '\n') {
            fprintf(outputFile, " %d\n", line_num++);
            at_start_of_line = 1;
            continue;
        }

        fputc(c, outputFile);
    }

    if (!at_start_of_line) {
        fprintf(outputFile, " %d", line_num);
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
