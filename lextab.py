# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('AND', 'COMMENT', 'DIVIDE', 'DO', 'ELIF', 'ELSE', 'EQUALS', 'EQUALSEQUALS', 'FLOATNUMBER', 'FOR', 'GREATEREQUALS', 'IF', 'INTNUMBER', 'LBRACE', 'LESSEQUALS', 'LPAREN', 'MINUS', 'MULTIPLICATION', 'NOT', 'NOTEQUALS', 'OR', 'PLUS', 'RBRACE', 'RPAREN', 'STRING', 'VAR', 'WHILE'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_FLOATNUMBER>(\\d*\\.\\d+|\\d+\\.\\d*))|(?P<t_INTNUMBER>\\d+)|(?P<t_COMMENT>\\#\\#\\#.*)|(?P<t_VAR>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_STRING>(\\\'[^\\\']*\\\'|\\"[^\\"]*\\"))|(?P<t_newline>\\n+)|(?P<t_ELIF>otherwise_if)|(?P<t_IF>condition)|(?P<t_ELSE>otherwise)|(?P<t_WHILE>during)|(?P<t_FOR>cycle)|(?P<t_DO>make)|(?P<t_NOTEQUALS><!>)|(?P<t_AND>and)|(?P<t_NOT>not)|(?P<t_PLUS>\\+)|(?P<t_MULTIPLICATION>\\*)|(?P<t_LPAREN>\\()|(?P<t_RPAREN>\\))|(?P<t_LBRACE>\\{)|(?P<t_RBRACE>\\})|(?P<t_EQUALSEQUALS>==)|(?P<t_LESSEQUALS><=)|(?P<t_GREATEREQUALS>>=)|(?P<t_OR>or)|(?P<t_MINUS>-)|(?P<t_DIVIDE>/)|(?P<t_EQUALS>=)', [None, ('t_FLOATNUMBER', 'FLOATNUMBER'), None, ('t_INTNUMBER', 'INTNUMBER'), ('t_COMMENT', 'COMMENT'), ('t_VAR', 'VAR'), ('t_STRING', 'STRING'), None, ('t_newline', 'newline'), (None, 'ELIF'), (None, 'IF'), (None, 'ELSE'), (None, 'WHILE'), (None, 'FOR'), (None, 'DO'), (None, 'NOTEQUALS'), (None, 'AND'), (None, 'NOT'), (None, 'PLUS'), (None, 'MULTIPLICATION'), (None, 'LPAREN'), (None, 'RPAREN'), (None, 'LBRACE'), (None, 'RBRACE'), (None, 'EQUALSEQUALS'), (None, 'LESSEQUALS'), (None, 'GREATEREQUALS'), (None, 'OR'), (None, 'MINUS'), (None, 'DIVIDE'), (None, 'EQUALS')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
