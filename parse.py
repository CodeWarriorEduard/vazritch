from lexer import tokens
import ply.yacc as yacc
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

variables = {}

# Definición de operadores binarios
def p_binary_operators(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | term MULTIPLICATION factor
                  | term DIVIDE factor'''
    if isinstance(p[1], (int, str, float)) and isinstance(p[3], (int, str, float)):
        if p[2] == '+':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = p[1] + p[3]
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = p[1] + p[3]
            else:
                p[0] = ('ERROR',  "Cannot concatenate non-strings to strings") #CHANG

        elif p[2] == '-':
            if not isinstance(p[1], str) and not isinstance(p[3], str):
                p[0] = p[1] - p[3]
            else:
                p[0] = ('ERROR','Unsupported operation') 

        elif p[2] == '*':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = p[1] * p[3]
            elif isinstance(p[1], int) and isinstance(p[3], str):
                p[0] = p[1] * p[3]
            elif isinstance(p[1], str) and isinstance(p[3], int):
                p[0] = p[1] * p[3]
            else:
                p[0] = ('ERROR',"Cannot multiply sequence by non-int of type 'float'")

        elif p[2] == '/':
            if not isinstance(p[1], str) and not isinstance(p[3], str):
                p[0] = p[1] / p[3]
            else:
               p[0] = ('ERROR',"Unsupported operation")

# Definición de variables y asignaciones
def p_factor_var(p):
    'factor : VAR'
    if p[1] not in variables:
        p[0] = ('ERROR',f"Undefined variable => {p[1]}")
    else:
        p[0] = variables[p[1]]

def p_assignment(p):
    'factor : VAR EQUALS expression'
    variables[p[1]] = p[3]
    p[0] = p[3] 

# Definición de valores booleanos
def p_factor_boolean(p):
    '''factor : TRUE
              | FALSE'''
    p[0] = p[1]

# Definición de operadores lógicos
def p_expression_and(p):
    'expression : expression AND expression'
    if isinstance(p[1], (str, int, float)) and isinstance(p[3], (str, int, float)):
        if(p[1] == 'Truth' and p[3] == 'Truth'):
            p[0] = 'Truth'
        elif(p[1] == 'Truth' and p[3] == 'Lie' or p[1] == 'Lie' and p[3] == 'Truth'):
            p[0] = 'Lie'
        else:
            if(p[1] == 'Lie' or p[3] == 'Lie'):
                p[0] = 'Lie'
            else:
                p[0] = p[3]

def p_expression_or(p):
    'expression : expression OR expression'
    if isinstance(p[1], (str, int, float)) and isinstance(p[3], (str, int, float)):
        if(p[1] == 'Lie' and p[3] == 'Lie'):
            p[0] = 'Lie'
        elif(p[1] == 'Truth' and p[3] == 'Lie' or p[1] == 'Lie' and p[3] == 'Truth'):
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

# Definición de operadores de comparación
def p_expression_comparison(p):
    '''expression : expression EQUALSEQUALS expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression GREATEREQUALS expression
                  | expression LESSEQUALS expression
                  | expression NOTEQUALS expression'''
    if isinstance(p[1], (int, str, float)) and isinstance(p[3], (int, str, float)):
        if p[2] == '==':
            p[0] = 'Truth' if p[1] == p[3] else 'Lie'
        elif p[2] == '>':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = 'Truth' if p[1] > p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] > p[3] else 'Lie'
            else:
                p[0] = ('ERROR',"Cannot compare different types")
        elif p[2] == '<':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = 'Truth' if p[1] < p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] < p[3] else 'Lie'
            else:
                p[0] = ('ERROR',"Cannot compare different types")
        elif p[2] == '>=':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = 'Truth' if p[1] >= p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] >= p[3] else 'Lie'
            else:
                p[0] = ('ERROR',"Cannot compare different types")
        elif p[2] == '<=':
            if isinstance(p[1], (int, float)) and isinstance(p[3], (int, float)):
                p[0] = 'Truth' if p[1] <= p[3] else 'Lie'
            elif isinstance(p[1], str) and isinstance(p[3], str):
                p[0] = 'Truth' if p[1] <= p[3] else 'Lie'
            else:
                p[0] = ('ERROR',"Cannot compare different types")
        elif p[2] == '!=':
            p[0] = 'Truth' if p[1] != p[3] else 'Lie'    
    else:
        p[0] = ('ERROR',"Unsupported operation")

# Definición de términos y factores
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
    p[0] = ('SHOW', p[3])

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_factor_brac(p):
    'factor : LBRACE expression RBRACE'
    p[0] = p[2]

def p_factor_neg(p):
    'factor : MINUS factor'
    p[0] = -p[2]

# Definición de las reglas if, elif y else
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE elif_clauses else_clause
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE elif_clauses
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE else_clause
                    | IF LPAREN expression RPAREN LBRACE statements RBRACE'''
    
    if len(p) == 8:  # Solo IF
        if p[3] == 'Truth':
            p[0] = p[6]
    elif len(p) == 9:  # IF y ELIF o IF y ELSE
        if p[3] == 'Truth':
            p[0] = p[6]
        else:
            p[0] = p[8]
    elif len(p) == 10:  # IF, múltiples ELIF y ELSE
        if p[3] == 'Truth':
            p[0] = p[6]
        elif p[8] != None:
            p[0] = p[8]
        else:
            p[0] = p[9]

def p_elif_clauses(p):
    '''elif_clauses : ELIF LPAREN expression RPAREN LBRACE statements RBRACE elif_clauses
                    | ELIF LPAREN expression RPAREN LBRACE statements RBRACE'''
    if p[3] == 'Truth':
        p[0] = p[6]
    elif len(p) == 9:
        p[0] = p[8]
    else:
        p[0] = None

def p_else_clause(p):
    '''else_clause : ELSE LBRACE statements RBRACE
                   | empty'''
    if len(p) == 5:
        p[0] = p[3]
    else:
        p[0] = None

def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement(p):
    '''statement : expression'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_expression(p):
    '''expression : if_statement
                  | VAR'''
    p[0] = p[1]

# Regla de error para expresiones
def p_expression_error(p):
    'expression : error'
    p[0] = ('ERROR', "Unsupported operation")

# Manejo de errores de sintaxis
erroraa = None
def p_error(p):
    global erroraa
    error_info = "" 
    if p:
        error_info = (f"Syntax error at '{p.value}'", f"line {p.lineno}")
    else:
        error_info = ("Syntax error at EOF")
   
    erroraa = error_info

# Construir el parser
parser = yacc.yacc()

#Aqui debe llegar del front una lista de string donde cada espacion representa una linea
# inputLines = ["condition(1<2){string1 = 'jon' string2 = 'raf' condition(string1 == string2){show('No lo veras')}}otherwise_if(2>1){show('RJJ')}otherwise{show('Pi: ' + '3.1416')}"] 

def formatLines(lines:str):
    s = [] 
    inIfBlock = False
    ifBlockLines = []

    lin = lines.splitlines()

    for line in lin:
        if inIfBlock:
            if line.strip().endswith("}"):
                ifBlockLines.append(line)
                ifBlock = ' '.join(ifBlockLines)
                s.append(ifBlock)  
                ifBlockLines = []
                inIfBlock = False
            else:
                ifBlockLines.append(line)
        else:
            if line.strip().startswith("condition"):
                inIfBlock = True
                ifBlockLines.append(line)
            else:
                s.append(line) 

    if ifBlockLines:
        ifBlock = ' '.join(ifBlockLines)
        s.append(ifBlock)
    
    return s

#La lista S es la lista con la que va a trabajar el parser, una lista de lineas muy bien procesadas
#Hasta donde se termina este código sirve para concatenar cada linea de una forma especial para nuestro parser

def parsear(linesFormat):
    global erroraa
    output = []
    result = None
    for line in linesFormat: 
        try:
            if line not in " \t \r\n \r \n":
                result = parser.parse(line)
                if erroraa:
                    output.append(('ERROR', erroraa))
                    erroraa = None
            if result is not None :
                output.append(result)
        except EOFError:
            break

    outputFormat = []
    for result in output:
        if type(result) is tuple:
            if result[0] in ('SHOW', 'ERROR'):
                outputFormat.append(result[1])
        elif type(result) is list:
            if result[0][0] in ('SHOW', 'ERROR'):
                outputFormat.append(result[0][1])

    return str(outputFormat)



class CodeInput(BaseModel):
    code: str

app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://localhost:5173",
    "http://54.241.139.9/",
    "http://54.241.139.9"
]


app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["GET", "POST", "OPTIONS"],  
    allow_headers=["Content-Type", "Authorization"],  
)


@app.post("/code")
def evaluate_expression(expression):
    print(expression)
    try:
        lines = formatLines(expression)
        result = parsear(lines)
        return {"result": result}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)