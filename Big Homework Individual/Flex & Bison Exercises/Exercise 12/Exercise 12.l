%option noyywrap

%x IN_WORD

%{
#include <stdio.h>
int capital_word_count = 0;
%}

%%

"finish"    {
                printf("Total words starting with a capital letter: %d\n", capital_word_count);
                printf("Press Enter to Exit\n");
                getchar();
                return 0;
            }

<INITIAL>[A-Z][a-zA-Z]*   { BEGIN(IN_WORD); capital_word_count++; }
<IN_WORD>[a-zA-Z]+         {}
<IN_WORD>" "                { BEGIN(INITIAL);}

.                           {}

%%

int main()
{
    printf("Enter text (type 'finish' on a single line to see the count):\n");

    yylex();
    
    return 0;
}
