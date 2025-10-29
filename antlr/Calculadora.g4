grammar Calculadora;

program
    : (statement ';'? NEWLINE?)* EOF
    ;

statement
    : assign
    | print
    | ifStatement
    ;

assign
    : ID '=' expr
    ;

print
    : 'print' '(' expr ')'
    ;

ifStatement
    : 'if' '(' condition ')' '{' statement* '}'
    ;

condition
    : expr ('>' | '<' | '==' | '>=' | '<=') expr
    ;

expr
    : expr op=('*'|'/') expr      # MulDiv
    | expr op=('+'|'-') expr      # AddSub
    | INT                         # Int
    | ID                          # Variable
    | '(' expr ')'                # Parens
    ;

ID  : [a-zA-Z][a-zA-Z_0-9]* ;
INT : [0-9]+ ;
NEWLINE : [\r\n]+ ;
WS : [ \t]+ -> skip ;