%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

extern int yylex();
extern void yyerror(const char *s);
%}

%union {
    int ival;
}

%token<ival> T_INT
%token T_PLUS T_MINUS T_MULTIPLY T_DIVIDE T_POWER
%token T_NEWLINE
%token T_LPAREN T_RPAREN

%type<ival> expression

%left T_PLUS T_MINUS
%left T_MULTIPLY T_DIVIDE
%right T_POWER
%nonassoc T_LPAREN T_RPAREN

%start calculation

%%

calculation:
       | calculation line
;

line: T_NEWLINE
    | expression T_NEWLINE { printf("\tResult: %d\n", $1); }
;

expression: T_INT                                { $$ = $1; }
          | expression T_PLUS expression         { $$ = $1 + $3; }
          | expression T_MINUS expression        { $$ = $1 - $3; }
          | expression T_MULTIPLY expression     { $$ = $1 * $3; }
          | expression T_DIVIDE expression       { if ($3 == 0)
                                                      { yyerror("Division by zero."); $$ = 0; }
                                                    else
                                                      { $$ = $1 / $3; } }
          | expression T_POWER expression        { $$ = (int)pow((double)$1, (double)$3); }
          | T_LPAREN expression T_RPAREN         { $$ = $2; }
;

%%

int main() {
  do {
    yyparse();
  } while (!feof(stdin));
  return 0;
}

void yyerror(const char *s) {
  fprintf(stderr, "Error: %s\n", s);
}
