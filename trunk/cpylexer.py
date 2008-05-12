from ply import lex as LEX
import tokens as tok_mod

tokens = tok_mod.name_of.values()

digit = r'[0-9]'
nondigit = r'[a-zA-Z_]'
H = r'[a-fA-F0-9]'
E = r'[Ee][+-]?{D}+'
FS = r'(f|F|l|L)'
IS = r'(u|U|l|L)*'

t_ignore = ' \t'

keywords = { 'const': 'CONST',
             'char' : 'CHAR',
             'void' : 'VOID',
             'int' : 'INT', 
             'extern' : 'EXTERN'
             }

identifier  = r'(' + nondigit + r'(' + digit + r'|' + nondigit + r')*)' 
literals = r';,:{}=()[].&!~-+*/%<>^|?'

@LEX.TOKEN(identifier)
def t_IDENTIFIER (t):
    t.type = keywords.get(t.value, 'IDENTIFIER')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def lex(s):
    'Lexes a single string'
    lexer = LEX.lex()
    lexer.input(s)
    lex_list = []
    while True:
        tok = lexer.token()
        if not tok: break
        lex_list.append(tok)
    return lex_list

