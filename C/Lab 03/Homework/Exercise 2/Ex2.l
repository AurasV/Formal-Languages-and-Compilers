%option case-insensitive
%{
#include <stdio.h>
%}

%%

"I"|"me"|"you"|"he"|"she"|"it"|"we"|"they"|"my"|"your"|"his"|"her"|"its"|"our"|"their" {
    printf("%s is a pronoun.\n", yytext);
}
.|\n        { }

%%

int main()
{
    yyin = stdin;    
    yylex();    
    return 0;
}

int yywrap()
{
    return 1;
}
