%option noyywrap

%{
#include <stdio.h>

int capital_count = 0;
int whitespace_count = 0;
int newline_count = 0;
int tab_count = 0;
%}

%%

[A-Z]           { capital_count++; }
[ \t]           { whitespace_count++; }
\n              { newline_count++; }
'\t'           { tab_count++; }  // Corrected rule for matching tabs
.               { /* Ignore other characters */ }

%%

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file) {
        perror("Error opening file");
        return 1;
    }

    yyin = file;

    yylex();

    fclose(file);

    printf("Capital letters: %d\n", capital_count);
    printf("Whitespaces: %d\n", whitespace_count);
    printf("Newlines: %d\n", newline_count);
    printf("Tabs: %d\n", tab_count);

    return 0;
}
