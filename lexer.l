%{
#include "parser.tab.h"
%}

%%

"CREATE"   { return CREATE; }
"READ"     { return READ; }
"UPDATE"   { return UPDATE; }
"DELETE"   { return DELETE; }
"WHERE"    { return WHERE; }
"SET"      { return SET; }

[0-9]+     { return NUMBER; }
\".*\"     { return STRING; }
[a-zA-Z_][a-zA-Z0-9_]* { return ID; }

"{"        { return '{'; }
"}"        { return '}'; }
":"        { return ':'; }
","        { return ','; }
"="        { return '='; }
";"        { return ';'; }

[ \t\n]    ;
.          { printf("Error lexico: %s\n", yytext); }

%%
