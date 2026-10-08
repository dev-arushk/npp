# N++ Language Specification

Version: 1.0.0

## 1. Lexical Grammar

### 1.1 Whitespace & Comments
- Horizontal whitespace (` `, `\t`, `\r`) is ignored except as token boundaries.
- Newlines (`\n`) and semicolons (`;`) serve as statement separators.
- Single-line comments begin with `//` or `#` and extend to end of line.
- Multi-line comments begin with `/*` and terminate with `*/`.
- Note comments begin with `note:` and extend to end of line.

### 1.2 Literals
- **Numbers**: Integer (`[0-9]+`) and IEEE-754 double precision floats (`[0-9]+\.[0-9]+`).
- **Strings**: Single- or double-quoted (`"..."`, `'...'`) supporting `\n`, `\t`, `\r`, `\\`, `\"`, `\'`.
- **Booleans**: `true`, `yes` (truthy), `false`, `no` (falsy).
- **Null**: `null`, `none`, `nothing`.

### 1.3 Compound English Tokens
The lexer recognizes multi-word natural phrases:
- `is not` -> `!=`
- `is greater than` / `greater than` -> `>`
- `is less than` / `less than` -> `<`
- `is at least` / `greater than or equal to` -> `>=`
- `is at most` / `less than or equal to` -> `<=`
- `otherwise if` / `else if` -> `ELIF`
- `give back` -> `RETURN`
- `for each` -> `FOR`

---

## 2. Syntax Grammar (EBNF)

```ebnf
Program        ::= ( Statement ( ';' | '\n' )* )* EOF ;

Statement      ::= SayStmt
                 | VarDecl
                 | ChangeStmt
                 | IfStmt
                 | WhileStmt
                 | RepeatStmt
                 | ForEachStmt
                 | FunctionDef
                 | ReturnStmt
                 | BreakStmt
                 | ContinueStmt
                 | AssignOrExprStmt ;

SayStmt        ::= ( 'say' | 'print' | 'display' | 'show' ) Expression ;

VarDecl        ::= ( 'set' | 'let' | 'make' | 'const' ) IDENTIFIER ( 'to' | '=' | ':' )? Expression ;

ChangeStmt     ::= 'change' IDENTIFIER ( 'to' | '=' ) Expression ;

IfStmt         ::= 'if' Expression ( 'then' | ':' )? Block
                   ( 'otherwise if' Expression ( 'then' | ':' )? Block )*
                   ( 'otherwise' ':'? Block )?
                   'end' ;

WhileStmt      ::= 'while' Expression ( 'do' | ':' )? Block 'end' ;

RepeatStmt     ::= ( 'repeat' | 'loop' ) Expression ( 'times' | 'do' | ':' )? Block 'end' ;

ForEachStmt    ::= 'for' 'each'? IDENTIFIER 'in' Expression ( 'do' | ':' )? Block 'end' ;

FunctionDef    ::= ( 'to' | 'fn' | 'function' | 'def' ) IDENTIFIER
                   ( 'with' IDENTIFIER ( ',' IDENTIFIER )*
                   | '(' ( IDENTIFIER ( ',' IDENTIFIER )* )? ')' )?
                   ':'? Block 'end' ;

ReturnStmt     ::= ( 'return' | 'give back' ) Expression? ;

Block          ::= Statement* ;

Expression     ::= LogicalOr ;
LogicalOr      ::= LogicalAnd ( ( 'or' | '||' ) LogicalAnd )* ;
LogicalAnd     ::= Equality ( ( 'and' | '&&' ) Equality )* ;
Equality       ::= Comparison ( ( '==' | '!=' | 'is' | 'is not' ) Comparison )* ;
Comparison     ::= Term ( ( '<' | '>' | '<=' | '>=' | 'greater than' | 'less than' | 'at least' | 'at most' ) Term )* ;
Term           ::= Factor ( ( '+' | '-' ) Factor )* ;
Factor         ::= Power ( ( '*' | '/' | '%' ) Power )* ;
Power          ::= Unary ( '^' Unary )* ;
Unary          ::= ( 'not' | '!' | '-' ) Unary | Postfix ;
Postfix        ::= Primary ( '(' ( Expression ( ',' Expression )* )? ')' | '[' Expression ']' )* ;

Primary        ::= NUMBER | STRING | BOOLEAN | NULL | IDENTIFIER
                 | 'ask' Expression?
                 | '(' Expression ')'
                 | '[' ( Expression ( ',' Expression )* )? ']'
                 | '{' ( Expression ':' Expression ( ',' Expression ':' Expression )* )? '}' ;
```
