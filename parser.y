%{
#include <stdio.h>
#include <stdlib.h>

void yyerror(const char *s);
int yylex();
%}

%token CREATE READ UPDATE DELETE WHERE SET
%token ID STRING NUMBER

%%

programa:
    instruccion
    | programa ';' instruccion
    ;

instruccion:
      create
    | read
    | update
    | delete
    ;

create:
    CREATE ID '{' pares '}'
    { printf("CREATE valido\n"); }
    ;

read:
    READ ID
    { printf("READ valido\n"); }
    | READ ID WHERE condicion
    { printf("READ con condicion\n"); }
    ;

update:
    UPDATE ID SET pares
    { printf("UPDATE valido\n"); }
    | UPDATE ID SET pares WHERE condicion
    { printf("UPDATE con condicion\n"); }
    ;

delete:
    DELETE ID
    { printf("DELETE valido\n"); }
    | DELETE ID WHERE condicion
    { printf("DELETE con condicion\n"); }
    ;

pares:
    par
    | pares ',' par
    ;

par:
    ID ':' valor
    ;

condicion:
    ID '=' valor
    ;

valor:
      STRING
    | NUMBER
    ;

%%

void yyerror(const char *s) {
    printf("Error: %s\n", s);
}

int main() {
    return yyparse();
}
