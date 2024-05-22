%option noyywrap

%%

[a-zA-Z]+     { printf("%s is a word.\n", yytext); }
[0-9]+        { printf("%s is a number.\n", yytext); }
.             { printf("%s is neither a word nor a number.\n", yytext); }

%%

int main()
{
    yylex();
    return 0;
}
