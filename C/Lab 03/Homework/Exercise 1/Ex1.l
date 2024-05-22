%{
#include <stdio.h>
%}

%%

[AaEeIiOoUu] { printf("%c is a vowel.\n", yytext[0]); }
.             { printf("%c is not a vowel.\n", yytext[0]); }

%%

int main(int argc, char **argv)
{
    yyin = stdin;
    
    yylex();
    
    return 0;
}

int yywrap()
{
    return 1;
}
