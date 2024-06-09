# List of token names.   This is always required
reserved = {
    'condition': 'IF',
    'otherwise_if': 'ELIF',
    'otherwise': 'ELSE',
    'during': 'WHILE',
    'make': 'DO',
    'cycle': 'FOR',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'process': 'FUNCTION'
}

tokens = [
   'INTNUMBER',
   'FLOATNUMBER',
   'PLUS',
   'MINUS',
   'MULTIPLICATION',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'LBRACE',
   'RBRACE',
   'EQUALSEQUALS',
   'LESSEQUALS',
   'GREATEREQUALS',
   'NOTEQUALS',
   'EQUALS',
   'COMMENT',
   'VAR',
   'STRING'
] + list(reserved.values())

# Operations
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_MULTIPLICATION   = r'\*'
t_DIVIDE  = r'/'

# Group
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'

# Comparison
t_EQUALSEQUALS  = r'=='
t_LESSEQUALS  = r'<='
t_GREATEREQUALS  = r'>='
t_NOTEQUALS  = r'<!>'

# Assignment
t_EQUALS  = r'='

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
