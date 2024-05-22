%option case-insensitive
%{
#include <stdio.h>
#include <string.h>
int pronoun_count = 0;
int verb_count = 0;
int adjective_count = 0;
int noun_count = 0;
int preposition_count = 0;
int digit_count = 0;
%}

%%

"I"|"me"|"you"|"he"|"she"|"it"|"we"|"they"|"my"|"your"|"his"|"her"|"its"|"our"|"their" { printf("%s is a pronoun.\n", yytext); pronoun_count++; }

"run"|"jump"|"swim"|"read"|"write"|"sing"|"talk"|"listen"|"eat"|"drink" { printf("%s is a verb.\n", yytext); verb_count++; }

"happy"|"sad"|"big"|"small"|"bright"|"dark"|"heavy"|"light"|"soft"|"hard" { printf("%s is an adjective.\n", yytext); adjective_count++; }

"cat"|"dog"|"house"|"car"|"tree"|"book"|"phone"|"computer"|"city"|"river" { printf("%s is a noun.\n", yytext); noun_count++; }

"in"|"on"|"at"|"from"|"to"|"with"|"by"|"for"|"against"|"about" { printf("%s is a preposition.\n", yytext); preposition_count++; }

[0-9]+ { printf("%s is a digit.\n", yytext); digit_count++; }
"finish" { 
    printf("Pronouns: %d\n", pronoun_count);
    printf("Verbs: %d\n", verb_count);
    printf("Adjectives: %d\n", adjective_count);
    printf("Nouns: %d\n", noun_count);
    printf("Prepositions: %d\n", preposition_count);
    printf("Digits: %d\n", digit_count);
    printf("Enter any input to exit:\n");
    getchar(); // Wait for any input
    return 0;
}
.|\n        { }

%%

int main()
{
    printf("Enter text (type 'finish' to see counts):\n");

    while(1) {
        if (yylex() == 0)
            break;
    }
    
    return 0;
}

int yywrap()
{
    return 1;
}
