from sly import Parser
from scanner import Scanner
import AST


class Mparser(Parser):

    tokens = Scanner.tokens

    debugfile = 'parser.out'

    precedence = (
        ('right', '=', ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN),
        ('left', 'EQUALS', 'NOTEQUALS', 'LESSEQUALS', 'GREATEREQUALS', '<', '>'),
        ('left', '+', '-', MATADD, MATSUB),
        ('left', '*', '/', MATMUL, MATDIV),
        ('right', 'UMINUS'),
        ('nonassoc', 'IFX'),
        ('nonassoc', 'ELSE'),
        ('left', "'"),
        ('left', ':'),
    )

    @_('instructions_opt')
    def program(self, p):
        return AST.Block(p.instructions_opt)

    @_('instructions')
    def instructions_opt(self, p):
        return p.instructions

    @_('')
    def instructions_opt(self, p):
        return []

    @_('instructions instruction')
    def instructions(self, p):
        return p.instructions + [p.instruction]

    @_('instruction')
    def instructions(self, p):
        return [p.instruction]

    @_('expression ";"')
    def instruction(self, p):
        return p.expression

    @_('assignment ";"')
    def instruction(self, p):
        return p.assignment

    @_('if_statement')
    def instruction(self, p):
        return p.if_statement

    @_('while_loop')
    def instruction(self, p):
        return p.while_loop

    @_('for_loop')
    def instruction(self, p):
        return p.for_loop

    @_('BREAK ";"')
    def instruction(self, p):
        return AST.Break()

    @_('CONTINUE ";"')
    def instruction(self, p):
        return AST.Continue()

    @_('RETURN expression ";"')
    def instruction(self, p):
        return AST.Return(p.expression)

    @_('PRINT expression_list ";"')
    def instruction(self, p):
        return AST.Print(p.expression_list)

    @_('"{" instructions_opt "}"')
    def instruction(self, p):
        return AST.Block(p.instructions_opt)

    @_('expression "=" expression')
    def assignment(self, p):
        return AST.AssignExpr('=', p.expression0, p.expression1)

    @_('expression ADDASSIGN expression')
    def assignment(self, p):
        return AST.AssignExpr('+=', p.expression0, p.expression1)

    @_('expression SUBASSIGN expression')
    def assignment(self, p):
        return AST.AssignExpr('-=', p.expression0, p.expression1)

    @_('expression MULASSIGN expression')
    def assignment(self, p):
        return AST.AssignExpr('*=', p.expression0, p.expression1)

    @_('expression DIVASSIGN expression')
    def assignment(self, p):
        return AST.AssignExpr('/=', p.expression0, p.expression1)

    @_('IF "(" expression ")" instruction %prec IFX')
    def if_statement(self, p):
        return AST.If(p.expression, p.instruction)

    @_('IF "(" expression ")" instruction ELSE instruction')
    def if_statement(self, p):
        return AST.If(p.expression, p.instruction0, p.instruction1)

    @_('WHILE "(" expression ")" instruction')
    def while_loop(self, p):
        return AST.While(p.expression, p.instruction)

    @_('FOR variable "=" range instruction')
    def for_loop(self, p):
        return AST.For(p.variable, p.range, p.instruction)

    @_('variable')
    def expression(self, p):
        return p.variable

    @_('ID')
    def variable(self, p):
        return AST.Variable(p.ID)

    @_('variable "[" expression_list "]"')
    def expression(self, p):
        return AST.Reference(p.variable, p.expression_list)

    @_('vector')
    def expression_list(self, p):
        return [p.vector]

    @_('expression ":" expression')
    def range(self, p):
        return AST.Range(p.expression0, p.expression1)

    @_('expression')
    def expression_list(self, p):
        return [p.expression]

    @_('expression_list "," expression')
    def expression_list(self, p):
        return p.expression_list + [p.expression]

    @_('expression_list "," vector')
    def expression_list(self, p):
        return p.expression_list + [p.vector]

    @_('expression "=" vector')
    def expression(self, p):
        return AST.AssignExpr('=', p.expression, p.vector)
    
    @_('"[" expression_list "]"')
    def vector(self, p):
        return AST.Vector(p.expression_list)

    @_('expression "+" expression')
    def expression(self, p):
        return AST.BinExpr('+', p.expression0, p.expression1)

    @_('expression "-" expression')
    def expression(self, p):
        return AST.BinExpr('-', p.expression0, p.expression1)

    @_('expression "*" expression')
    def expression(self, p):
        return AST.BinExpr('*', p.expression0, p.expression1)

    @_('expression "/" expression')
    def expression(self, p):
        return AST.BinExpr('/', p.expression0, p.expression1)

    @_('expression MATADD expression')
    def expression(self, p):
        return AST.BinExpr('.+', p.expression0, p.expression1)

    @_('expression MATSUB expression')
    def expression(self, p):
        return AST.BinExpr('.-', p.expression0, p.expression1)

    @_('expression MATMUL expression')
    def expression(self, p):
        return AST.BinExpr('.*', p.expression0, p.expression1)

    @_('expression MATDIV expression')
    def expression(self, p):
        return AST.BinExpr('./', p.expression0, p.expression1)

    @_('expression EQUALS expression')
    def expression(self, p):
        return AST.RelExpr('==', p.expression0, p.expression1)

    @_('expression NOTEQUALS expression')
    def expression(self, p):
        return AST.RelExpr('!=', p.expression0, p.expression1)

    @_('expression LESSEQUALS expression')
    def expression(self, p):
        return AST.RelExpr('<=', p.expression0, p.expression1)

    @_('expression GREATEREQUALS expression')
    def expression(self, p):
        return AST.RelExpr('>=', p.expression0, p.expression1)

    @_('expression "<" expression')
    def expression(self, p):
        return AST.RelExpr('<', p.expression0, p.expression1)

    @_('expression ">" expression')
    def expression(self, p):
        return AST.RelExpr('>', p.expression0, p.expression1)

    @_('"-" expression %prec UMINUS')
    def expression(self, p):
        return AST.UnaryExpr('-', p.expression)

    @_('expression "\'"')
    def expression(self, p):
        return AST.Transpose(p.expression)

    @_('"(" expression ")"')
    def expression(self, p):
        return p.expression

    @_('INT')
    def expression(self, p):
        return AST.IntNum(p.INT)

    @_('FLOAT')
    def expression(self, p):
        return AST.FloatNum(p.FLOAT)

    @_('STRING')
    def expression(self, p):
        return AST.String(p.STRING)

    @_('EYE "(" expression ")"')
    def expression(self, p):
        return AST.Eye(p.expression)

    @_('ZEROS "(" expression ")"')
    def expression(self, p):
        return AST.Zeros(p.expression)

    @_('ONES "(" expression ")"')
    def expression(self, p):
        return AST.Ones(p.expression)

    def error(self, token):
        if token:
            lineno = token.lineno
            print(f"Syntax error in line {lineno}: Unexpected token {token.type}")
        else:
            print("Syntax error: Unexpected end of input")
        return AST.Error()

