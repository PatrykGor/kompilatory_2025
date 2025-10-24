import sys
from sly import Lexer


class Scanner(Lexer):

    literals = {'+', '-', '*', '/', '=',
                '(', ')', '[', ']', '{', '}',
                ':', ',', ';', '\'', '<', '>'}
    tokens = {MATADD, MATSUB, MATMUL, MATDIV,
              ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN,
              LESSEQUALS, GREATEREQUALS, NOTEQUALS, EQUALS,
              INT, FLOAT, STRING, ID, IF, ELSE, FOR, WHILE,
              BREAK, CONTINUE, RETURN, EYE, ZEROS, ONES, PRINT}
    # String containing ignored characters (between tokens)
    ignore = ' \t'

    # Other ignored patterns
    ignore_comment = r'\#.*'

    # Base ID rule
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Special cases
    ID['if'] = IF
    ID['else'] = ELSE
    ID['for'] = FOR
    ID['while'] = WHILE
    ID['break'] = BREAK
    ID['continue'] = CONTINUE
    ID['return'] = RETURN
    ID['eye'] = EYE
    ID['zeros'] = ZEROS
    ID['ones'] = ONES
    ID['print'] = PRINT

    STRING = r'".*?"'

    @_(r'(?:\d+\.\d*|\.\d+)(?:[+-]?[eE]\d+)?|\d+[+-]?[eE]\d+')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t
        
    ADDASSIGN = r'\+='
    SUBASSIGN = r'-='
    MULASSIGN = r'\*='
    DIVASSIGN = r'/='

    LESSEQUALS = r'<='
    GREATEREQUALS = r'>='
    NOTEQUALS = r'\!='
    EQUALS = r'=='

    MATADD = r'\.\+'
    MATSUB = r'\.-'
    MATMUL = r'\.\*'
    MATDIV = r'\./'

    # Line number tracking
    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print('Line %d: Bad character %r' % (self.lineno, t.value[0]))
        self.index += 1


if __name__ == '__main__':

    lexer = Scanner()

    filename = sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    with open(filename, "r") as file:
        text = file.read()

    for tok in lexer.tokenize(text):
        print(f"{tok.lineno}: {tok.type}({tok.value})")


  
