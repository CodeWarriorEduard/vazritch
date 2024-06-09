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
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            if not isinstance(p[1], str) and not isinstance(p[3], str):
                p[0] = p[1] - p[3]
            else:
                print("unsupported operation")
        elif p[2] == '*':
            p[0] = p[1] * p[3]
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
    if p[3] in variables or isinstance(p[3], (int, str, float)):
        variables[p[1]] = p[3]
        p[0] = p[3] 

def p_factor_boolean(p):
    '''factor : TRUE
              | FALSE'''
    p[0] = p[1]

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
            if type(p[1]) == type(p[3]):
                p[0] = 'Truth' if p[1] > p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '<':
            if type(p[1]) == type(p[3]):
                p[0] = 'Truth' if p[1] < p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '>=':
            if type(p[1]) == type(p[3]):
                p[0] = 'Truth' if p[1] >= p[3] else 'Lie'
            else:
                print(f"Cannot compare different types")
        elif p[2] == '<=':
            if type(p[1]) == type(p[3]):
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

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

s = '''
show("Hola Cachón") 
a = 1+2
show(a)
'''


lines = s.splitlines()

for line in lines:
    if line.strip(): 
        result = parser.parse(line)
        if result is not None:
            print(result)
