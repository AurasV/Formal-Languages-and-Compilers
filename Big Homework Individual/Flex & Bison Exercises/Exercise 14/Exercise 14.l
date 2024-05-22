%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define NUMBER 256
#define ADD 257
#define SUB 258
#define MUL 259
#define DIV 260
#define EOL 261

float yylval; // Declare yylval for storing the value of the parsed number

void yyerror(const char *s);
%}

digit   [0-9]
number  {digit}+(\.{digit}*)?([eE][+-]?{digit}+)?

%%
[ \t]+               { /* ignore whitespace */ }
{number}             { yylval = atof(yytext); return NUMBER; }
"+"                  { return ADD; }
"-"                  { return SUB; }
"*"                  { return MUL; }
"/"                  { return DIV; }
\n                   { return EOL; }
.                    { yyerror("Invalid character"); }

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main(void) {
    printf("Enter an expression (e.g., 3.5 + 4.2):\n");
    while (1) {
        int token;
        token = yylex();
        if (token == 0) break;

        if (token == NUMBER) {
            float val1, val2, result;
            val1 = yylval;
            token = yylex();
            if (token == ADD || token == SUB || token == MUL || token == DIV) {
                int op = token;
                token = yylex();
                if (token == NUMBER) {
                    val2 = yylval;
                    switch (op) {
                        case ADD: result = val1 + val2; break;
                        case SUB: result = val1 - val2; break;
                        case MUL: result = val1 * val2; break;
                        case DIV: 
                            if (val2 == 0) {
                                yyerror("Division by zero");
                                continue;
                            }
                            result = val1 / val2; 
                            break;
                        default: yyerror("Unknown operator"); continue;
                    }
                    printf("Result: %f\n", result);
                    // After printing the result, expect either an operator or EOL
                    continue;
                } else {
                    yyerror("Expected a number");
                }
            } else {
                yyerror("Expected an operator");
            }
        } else {
            ;
        }
    }
    return 0;
}

int yywrap() {
    return 1;
}
