%option noyywrap
%{
#include <stdio.h>
#include <string.h>
%}

%%

(http|https):\/\/[^\s]+ { printf("%s\nValid URL\n", yytext); }
[^\n]+                 { printf("Not a URL\n"); }
\n                     { }

%%

int main() {
  char line[1024];

  while (fgets(line, sizeof(line), stdin)) {
    line[strcspn(line, "\n")] = 0;

    YY_BUFFER_STATE bufferState = yy_scan_string(line);
    yylex();
    yy_delete_buffer(bufferState);
  }

  return 0;
}
