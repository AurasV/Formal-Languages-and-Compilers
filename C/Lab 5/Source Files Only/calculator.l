%option noyywrap

%{
#include <stdio.h>
#include <stdlib.h>
#include "calculator.tab.h"
%}

%%

[ \t]             ;
[0-9]+            { yylval.ival = atoi(yytext); return T_INT; }
\n                { return T_NEWLINE; }
"+"               { return T_PLUS; }
"-"               { return T_MINUS; }
"*"               { return T_MULTIPLY; }
"/"               { return T_DIVIDE; }
"^"               { return T_POWER; }
"("               { return T_LPAREN; }
")"               { return T_RPAREN; }

%%
