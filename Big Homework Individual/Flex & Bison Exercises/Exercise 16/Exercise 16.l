%option noyywrap

%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "Exercise 16.tab.h"
%}

%%

[ \t]             ;
[0-9]+\.[0-9]+    { yylval.fval = atof(yytext); return T_FLOAT; }
[0-9]+            { yylval.fval = atof(yytext); return T_FLOAT; }
\n                { return T_NEWLINE; }
"+"               { return T_PLUS; }
"-"               { return T_MINUS; }
"*"               { return T_MULTIPLY; }
"/"               { return T_DIVIDE; }
"^"               { return T_POWER; }
"!"               { return T_FACTORIAL; }
"sin"             { return T_SIN; }
"cos"             { return T_COS; }
"sqrt"            { return T_SQRT; }
"fabs"            { return T_FABS; }
"sinh"            { return T_SINH; }
"cosh"            { return T_COSH; }
"("               { return T_LPAREN; }
")"               { return T_RPAREN; }

%%
