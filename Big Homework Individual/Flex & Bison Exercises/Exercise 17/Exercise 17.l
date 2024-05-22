%{
#include "Exercise 17.tab.h"
#include <stdio.h>

unsigned int binary_to_decimal(const char *binary);
%}

%%
[ \t]+              { /* Ignore whitespace */ }
[01]+               { yylval = binary_to_decimal(yytext); return BINARY_NUMBER; }
"+"                 { return ADD; }
"-"                 { return SUB; }
"*"                 { return MUL; }
"/"                 { return DIV; }
\n                  { return '\n'; }
.                   { return yytext[0]; }

%%

unsigned int binary_to_decimal(const char *binary) {
    unsigned int decimal = 0;
    while (*binary == '0' || *binary == '1') {
        decimal = (decimal << 1) | (*binary++ - '0');
    }
    return decimal;
}

int yywrap() {
    return 1;
}
