%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex(void);

char *decimal_to_binary(unsigned int decimal);
%}

%token BINARY_NUMBER
%token ADD SUB MUL DIV

%left ADD SUB
%left MUL DIV

%%
input:
    /* empty */
    | input line
    ;

line:
    '\n'
    | expr '\n' { printf("= %s\n", decimal_to_binary($1)); }
    ;

expr:
    BINARY_NUMBER { $$ = $1; }
    | expr ADD expr { $$ = $1 + $3; }
    | expr SUB expr { $$ = $1 - $3; }
    | expr MUL expr { $$ = $1 * $3; }
    | expr DIV expr { if ($3 == 0) { yyerror("Division by zero"); } else { $$ = $1 / $3; } }
    ;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

char *decimal_to_binary(unsigned int decimal) {
    static char binary[33];
    binary[32] = '\0';
    char *ptr = &binary[31];

    if (decimal == 0) {
        *ptr = '0';
        return ptr;
    }

    while (decimal > 0) {
        *ptr-- = (decimal % 2) ? '1' : '0';
        decimal /= 2;
    }
    return ptr + 1;
}

int main(void) {
    printf("Enter a binary expression:\n");
    yyparse();
    return 0;
}
