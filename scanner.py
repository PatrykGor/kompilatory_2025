import sys
from sly import Lexer


class Scanner(Lexer):

    literals = {'+', '-', '*', '/', '='
                '(', ')', '[', ']', '{', '}',
                ':', ',', ';', '\'', '<', '>'}
    tokens = {MATPLUS, MATMINUS, MATTIMES, MATDIV,
              INCREMENT, DECREMENT, TIMESASSIGN, DIVASSIGN,
              LESSEQUALS, GREATEREQUALS, NOTEEQUALS, EQUALS,
              INT, FLOAT, STRING, ID}
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

    STRING = r'".*"'
    FLOAT = r'\d+\.\d*'
    INT = r'\d+'
        
    INCREMENT = r'\+='
    DECREMENT = r'-='
    TIMESASSIGN = r'\*='
    DIVASSIGN = r'/='

    LESSEQUALS = r'<='
    GREATEREQUALS = r'>='
    NOTEQUALS = r'\!='
    EQUALS = r'=='

    MATPLUS = r'\.\+'
    MATMINUS = r'\.-'
    MATTIMES = r'\.\*'
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


  
