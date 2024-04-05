%{
#include <stdio.h>
%}

%%

"/*"            { char c;
                 c = input();
                 while(c != 0) {
                     if(c == '*') {
                         if((c = input()) == '/') break;
                     } else {
                         c = input();
                     }
                 }
               }
"//"            { char c;
                 while((c = input()) != '\n' && c != 0);
               }
.               { ECHO; }
\n              { ECHO; }

%%

int main(int argc, char **argv)
{
    yyin = fopen("input.txt", "r");
    if (!yyin) {
        perror("Error opening input.txt");
        return 1;
    }
    
    yyout = fopen("output.txt", "w");
    if (!yyout) {
        perror("Error opening output.txt");
        fclose(yyin);
        return 1;
    }

    yylex();

    fclose(yyin);
    fclose(yyout);

    return 0;
}

int yywrap(void)
{
    return 1;
}
