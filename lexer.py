import ply.lex as lex
from tokens import *

# Float numbers
def t_FLOATNUMBER(t):
    r'(\d*\.\d+|\d+\.\d*)'
    t.value = float(t.value)
    return t

# Greater than
def t_GREATER(t):
    r'>'
    return t

# Comma
def t_COMMA(t):
    r','
    return t

# Integer numbers
def t_INTNUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Comment
def t_COMMENT(t):
    r'\#\#\#.*'
    t.value = f"{t}"
    return t

# Variable
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')   
    return t

# Strings
def t_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = str(t.value[1:-1])
    return t

# Less than
def t_LESS(t):
    r'<'
    return t

# Next Line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test
data = '''
22
1.5 .5
+ - * /
()
{}
==
>=
<=
<!>
=
condition
otherwise_if
otherwise
during
make
cycle
and
or
not
miVariable
mi_variable
miVar
"Tremendo"
process
show(1<2)
###comentario
,
process
'''

# Data input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break  
    print(f"Type: {tok.type} | Value: {tok.value} | Line: {tok.lineno} | Position: {tok.lexpos}")
