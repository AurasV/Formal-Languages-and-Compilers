%option noyywrap

%%
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}   { printf("%s is an email address.\n", yytext); }
.                                               { printf("%s is not an email address.\n", yytext); }
%%

int main()
{
    yylex();
    return 0;
}
