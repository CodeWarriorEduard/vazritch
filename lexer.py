import ply.lex as lex
from tokens import *

# Float numbers
def t_FLOATNUMBER(t):
    r'(\d*\.\d+|\d+\.\d*)'
    t.value = float(t.value)
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

# Varible
def t_VAR(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VAR')   
    return t

# Strings
def t_STRING(t):
    r'(\'[^\']*\'|\"[^\"]*\")'
    t.value = str(t.value[1:-1])
    return t


# Next Line
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_process(t):
    r'process'
    return t

# Build the lexer
lexer = lex.lex()
lexer = lex.lex(optimize=True, lextab='lextab')

# # Test
# data = '''

# 22
# 1.5 .5
# + - * /
# ()
# {}
# ==
# >=
# <=
# <!>
# =
# condition
# otherwise_if
# otherwise
# during
# make
# cycle
# and
# or
# not
# miVariable
# mi_variable
# miVar
# "Tremendo"
# process
# show
# ###comentario
# ,
# '''

# # Data input
# lexer.input(data)

# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok: 
#         break  
#     print(f"Type: {tok.type} | Value: {tok.value} | Line: {tok.lineno} | Position: {tok.lexpos}")