%option noyywrap
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* targetWord;
char* replacementWord;
%}

%%

[a-zA-Z]+   {
                if(strcmp(yytext, targetWord) == 0) {
                    fprintf(yyout, "%s", replacementWord);
                } else {
                    fprintf(yyout, "%s", yytext);
                }
            }

.|\n        { fprintf(yyout, "%s", yytext); }

%%

int main(int argc, char **argv) {
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <target_word> <replacement_word> <input_file>\n", argv[0]);
        exit(1);
    }

    targetWord = argv[1];
    replacementWord = argv[2];

    FILE *inputFile = fopen(argv[3], "r");
    if (inputFile == NULL) {
        perror("Error opening input file");
        exit(1);
    }

    yyin = inputFile;
    yyout = fopen("output.txt", "w");
    if (yyout == NULL) {
        perror("Error creating output file");
        fclose(inputFile);
        exit(1);
    }

    yylex();

    fclose(inputFile);
    fclose(yyout);

    return 0;
}
