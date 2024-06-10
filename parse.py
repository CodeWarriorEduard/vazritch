import ply.yacc as yacc
from lexer import tokens

variables = {}

def p_binary_operators(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  term       : term MULTIPLICATION factor
                  | term DIVIDE factor'''  
    if isinstance(p[1], (int,str,float)) and isinstance(p[3], (int,str,float)):
        if p[2] == '+':

            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = p[1] + p[3]
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = p[1] + p[3]
            else:
                print("Cant only concatenate string to string")

        elif p[2] == '-':
            if not isinstance(p[1], str) and not isinstance(p[3], str):
                p[0] = p[1] - p[3]
            else:
                print("unsupported operation")
        elif p[2] == '*':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = p[1] * p[3]
            elif isinstance(p[1], int) and isinstance(p[3], str):
                p[0] = p[1] * p[3]
            elif isinstance(p[1], str) and isinstance(p[3], int):
                p[0] = p[1] * p[3]
            else:
                print("can't multiply sequence by non-int of type 'float'")
        elif p[2] == '/':
            if not isinstance(p[1], str) and not isinstance(p[3], str):
                p[0] = p[1] / p[3]
            else:
                print("unsupported operation")

def p_factor_var(p):
    'factor : VAR'
    if p[1] not in variables:
        print(f"Undefined variable => {p[1]}")
    else:
        p[0] = variables[p[1]]

def p_assignment(p):
    'factor : VAR EQUALS expression'
    variables[p[1]] = p[3]
    p[0] = p[3] 

def p_factor_boolean(p):
    '''factor : TRUE
              | FALSE'''
    p[0] = p[1]

def p_expression_and(p):
    'expression : expression AND expression'
    if isinstance(p[1], (str, int, float)) and isinstance(p[3], (str, int, float)):
        if(p[1]=='Truth' and p[3]=='Truth'):
            p[0] = 'Truth'
        elif(p[1]=='Truth' and p[3]=='Lie' or p[1]=='Lie' and p[3]=='Truth'):
            p[0] = 'Lie'
        else:
            if(p[1] == 'Lie' or p[3] == 'Lie'):
                p[0] = 'Lie'
            else:
                p[0] = p[3]

def p_expression_or(p):
    'expression : expression OR expression'
    if isinstance(p[1], (str, int, float)) and isinstance(p[3], (str, int, float)):
        if(p[1]=='Lie' and p[3]=='Lie'):
            p[0] = 'Lie'
        elif(p[1]=='Truth' and p[3]=='Lie' or p[1]=='Lie' and p[3]=='Truth'):
            p[0] = 'Truth'
        else:
            if(p[1] == 'Lie' or p[3] == 'Lie'):
                a1 = p[1]
                a2 = p[3]
                if(a1 != 'Lie'):
                    p[0] = a1
                else:
                    p[0] = a2
            else:
                p[0] = p[1]

def p_expression_not(p):
    'expression : NOT expression'
    if isinstance(p[2], (str, int, float)):
        if p[2] == 'Lie':
            p[0] = 'Truth'
        else:
            p[0] = 'Lie'

def p_expression_comparison(p):
    '''expression : expression EQUALSEQUALS expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATEREQUALS expression
                  | expression LESSEQUALS expression
                  | expression NOTEQUALS expression'''
    if isinstance(p[1], (int,str,float)) and isinstance(p[3], (int,str,float)):
    
        if p[2] == '==':
            p[0] = 'Truth' if p[1] == p[3] else 'Lie'
        elif p[2] == '>':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int,float)):
                p[0] = 'Truth' if p[1] > p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] > p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '<':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int,float)):
                p[0] = 'Truth' if p[1] < p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] < p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '>=':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int,float)):
                p[0] = 'Truth' if p[1] >= p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] >= p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '<=':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int,float)):
                p[0] = 'Truth' if p[1] <= p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] <= p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '<!>':
            p[0] = 'Truth' if p[1] != p[3] else 'Lie'    
    else:
        print("Unsupported operation")

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_and(p):
    'factor : AND'
    p[0] = p[1]

def p_factor_or(p):
    'factor : OR'
    p[0] = p[1]

def p_factor_not(p):
    'factor : NOT'
    p[0] = p[1]

def p_factor_if(p):
    'factor : IF'
    p[0] = p[1]

def p_factor_elif(p):
    'factor : ELIF'
    p[0] = p[1]

def p_factor_else(p):
    'factor : ELSE'
    p[0] = p[1]

def p_factor_intnum(p):
    'factor : INTNUMBER'
    p[0] = p[1]

def p_factor_floatnum(p):
    'factor : FLOATNUMBER'
    p[0] = p[1]

def p_factor_string(p):
    'factor : STRING'
    p[0] = p[1]

def p_factor_comment(p):
    'factor : COMMENT'
    pass

def p_factor_show(p):
    'factor : SHOW LPAREN expression RPAREN'
    p[0] = p[3]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_brac(p):
    'factor : LBRACE expression RBRACE'
    p[0] = p[2]

def p_factor_neg(p):
    'factor : MINUS factor'
    p[0] = -p[2]

# If, elif and else
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses else_clause
                    | IF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses
                    | IF LPAREN expression RPAREN LBRACE expression RBRACE else_clause
                    | IF LPAREN expression RPAREN LBRACE expression RBRACE'''
    if p[3] == 'Truth':
        p[0] = p[6]
    elif len(p) == 9 and p[8] is not None:
        p[0] = p[8]
    elif len(p) >= 8 and p[8] is not None:
        p[0] = p[8]
    else:
        p[0] = p[9]

# Elif
def p_elif_clauses(p):
    '''elif_clauses : ELIF LPAREN expression RPAREN LBRACE expression RBRACE elif_clauses
                    | ELIF LPAREN expression RPAREN LBRACE expression RBRACE'''
    if p[3] == 'Truth':
        p[0] = p[6]
    elif len(p) == 9:
        p[0] = p[8]
    else:
        p[0] = None

# Else
def p_else_clause(p):
    '''else_clause : ELSE LBRACE expression RBRACE
                   | empty'''
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = None

# Empty rule
def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''expression : if_statement
                  | VAR'''
    p[0] = p[1]

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('\nvazritch > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    if result is not None:
        print(result)
