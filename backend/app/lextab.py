# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AND', 'COMMA', 'COMMENT', 'DIVIDE', 'DO', 'ELIF', 'ELSE', 'EQUALS', 'EQUALSEQUALS', 'FALSE', 'FLOATNUMBER', 'FOR', 'FUNCTION', 'GREATER', 'GREATEREQUALS', 'IF', 'INTNUMBER', 'LBRACE', 'LESS', 'LESSEQUALS', 'LPAREN', 'MINUS', 'MULTIPLICATION', 'NOT', 'NOTEQUALS', 'OR', 'PLUS', 'RBRACE', 'RETURN', 'RPAREN', 'SHOW', 'STRING', 'TRUE', 'VAR', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_FLOATNUMBER>(\\d*\\.\\d+|\\d+\\.\\d*))|(?P<t_INTNUMBER>\\d+)|(?P<t_COMMENT>\\#\\#\\#.*)|(?P<t_VAR>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_STRING>(\\\'[^\\\']*\\\'|\\"[^\\"]*\\"))|(?P<t_newline>\\n+)|(?P<t_process>process)|(?P<t_NOTEQUALS><!>)|(?P<t_PLUS>\\+)|(?P<t_MULTIPLICATION>\\*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_LBRACE>\\{)|(?P<t_RBRACE>\\})|(?P<t_EQUALSEQUALS>==)|(?P<t_LESSEQUALS><=)|(?P<t_GREATEREQUALS>>=)|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)|(?P<t_LESS><)|(?P<t_GREATER>>)|(?P<t_EQUALS>=)|(?P<t_COMMA>,)', [None, ('t_FLOATNUMBER', 'FLOATNUMBER'), None, ('t_INTNUMBER', 'INTNUMBER'), ('t_COMMENT', 'COMMENT'), ('t_VAR', 'VAR'), ('t_STRING', 'STRING'), None, ('t_newline', 'newline'), ('t_process', 'process'), (None, 'NOTEQUALS'), (None, 'PLUS'), (None, 'MULTIPLICATION'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'LBRACE'), (None, 'RBRACE'), (None, 'EQUALSEQUALS'), (None, 'LESSEQUALS'), (None, 'GREATEREQUALS'), (None, 'MINUS'), (None, 'DIVIDE'), (None, 'LESS'), (None, 'GREATER'), (None, 'EQUALS'), (None, 'COMMA')])]}
_lexstateignore = {'INITIAL': ' \t \r\n \r \n'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
