%option case-insensitive
%{
#include <stdio.h>
%}

%%

"I"|"me"|"you"|"he"|"she"|"it"|"we"|"they"|"my"|"your"|"his"|"her"|"its"|"our"|"their" { printf("%s is a pronoun.\n", yytext); }

"run"|"jump"|"swim"|"read"|"write"|"sing"|"talk"|"listen"|"eat"|"drink" { printf("%s is a verb.\n", yytext); }

"happy"|"sad"|"big"|"small"|"bright"|"dark"|"heavy"|"light"|"soft"|"hard" { printf("%s is an adjective.\n", yytext); }

"cat"|"dog"|"house"|"car"|"tree"|"book"|"phone"|"computer"|"city"|"river" { printf("%s is a noun.\n", yytext); }

"in"|"on"|"at"|"from"|"to"|"with"|"by"|"for"|"against"|"about" { printf("%s is a preposition.\n", yytext); }

[0-9] { printf("%s is a digit.\n", yytext); }
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
