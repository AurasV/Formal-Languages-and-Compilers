%{
#include <stdio.h>
%}

%%

[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}   { printf("Valid email address: %s\n", yytext); }
\n                                              { }
.                                               { printf("Invalid input: %s\n", yytext); }

%%

int main()
{
    printf("Enter a string to check if it's an email address: ");
    fflush(stdout);
    yylex();
    return 0;
}

int yywrap()
{
    return 1;
}
