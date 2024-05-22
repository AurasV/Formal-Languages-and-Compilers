%{
#include <stdio.h>
int valid=0;
%}

%%

([0-2][0-9]|[3][0-1])\/((0(1|3|5|7|8))|(10|12))\/([1-2][0-9]{3})    { valid=1; printf("Valid Date\n"); }

([0-2][0-9]|30)\/((0(4|6|9))|11)\/([1-2][0-9]{3})    { valid=1; printf("Valid Date\n"); }

([0-1][0-9]|2[0-8])\/02\/([1-2][0-9]{3})    { valid=1; printf("Valid Date\n"); }

29\/02\/([1-2][0-9]{3})    {
    int yr=0, i=0;
    while(yytext[i] != '/') i++;
    i++;
    while(yytext[i] != '/') i++;
    i++;
    while(yytext[i]) yr = yr * 10 + (yytext[i++] - '0');
    if ((yr % 4 == 0 && yr % 100 != 0) || yr % 400 == 0) {
        valid=1;
        printf("Valid Date\n");
    }
}

\n    { }

.    { 
if(valid == 0)
    {
        printf("Invalid Date\n");
		valid = 1;
    }
}

%%

int main()
{
    printf("Enter date (DD/MM/YYYY): ");
	int valid = 0;
    fflush(stdout);
    yylex();
	valid = 0;

    return 0;
}

int yywrap()
{
    return 1;
}
