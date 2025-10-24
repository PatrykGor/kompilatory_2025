from sly import Parser
from scanner import Scanner


class Mparser(Parser):

    tokens = Scanner.tokens

    debugfile = 'parser.out'


    precedence = (
        ('right', '=', ADDASSIGN, SUBASSIGN, MULASSIGN, DIVASSIGN),
        ('left', 'EQUALS', 'NOTEQUALS', 'LESSEQUALS', 'GREATEREQUALS', '<', '>'),
        ('left', '+', '-', MATADD, MATSUB),
        ('left', '*', '/', MATMUL, MATDIV),
        ('right', 'UMINUS'),
        ('nonassoc', 'IF'),
        ('nonassoc', 'ELSE'),
        ('left', "'"),
    )


    @_('instructions_opt')
    def program(self, p):
        pass

    @_('instructions')
    def instructions_opt(self, p):
        pass

    @_('')
    def instructions_opt(self, p):
        pass

    @_('instructions instruction')
    def instructions(self, p):
        pass

    @_('instruction')
    def instructions(self, p):
        pass

    @_('expression ";"')
    def instruction(self, p):
        return ('expr_stmt', p.expression)

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
        return ('break',)

    @_('CONTINUE ";"')
    def instruction(self, p):
        return ('continue',)

    @_('RETURN expression ";"')
    def instruction(self, p):
        return ('return', p.expression)

    @_('PRINT expression_list ";"')
    def instruction(self, p):
        return ('print', p.expression_list)

    @_('"{" instructions_opt "}"')
    def instruction(self, p):
        return ('block', p.instructions_opt)

    @_('ID "=" expression')
    def assignment(self, p):
        return ('assign', p.ID, p.expression)

    @_('ID ADDASSIGN expression')
    def assignment(self, p):
        return ('add_assign', p.ID, p.expression)

    @_('ID SUBASSIGN expression')
    def assignment(self, p):
        return ('sub_assign', p.ID, p.expression)

    @_('ID MULASSIGN expression')
    def assignment(self, p):
        return ('mul_assign', p.ID, p.expression)

    @_('ID DIVASSIGN expression')
    def assignment(self, p):
        return ('div_assign', p.ID, p.expression)

    @_('ID "[" expression_list "]" "=" expression')
    def assignment(self, p):
        return ('assign_indexed', p.ID, p.expression_list, p.expression)

    @_('IF "(" expression ")" instruction')
    def if_statement(self, p):
        return ('if', p.expression, p.instruction, None)

    @_('IF "(" expression ")" instruction ELSE instruction')
    def if_statement(self, p):
        return ('if', p.expression, p.instruction, p.instruction1)

    @_('WHILE "(" expression ")" instruction')
    def while_loop(self, p):
        return ('while', p.expression, p.instruction)

    @_('FOR ID "=" range instruction')
    def for_loop(self, p):
        return ('for', p.ID, p.range, p.instruction)

    @_('expression ":" expression')
    def range(self, p):
        return ('range', p.expression0, p.expression1)

    @_('expression')
    def expression_list(self, p):
        return [p.expression]

    @_('expression_list "," expression')
    def expression_list(self, p):
        return p.expression_list + [p.expression]

    @_('"[" matrix_rows "]"')
    def expression(self, p):
        return ('matrix', p.matrix_rows)

    @_('matrix_row')
    def matrix_rows(self, p):
        return [p.matrix_row]

    @_('matrix_rows ";" matrix_row')
    def matrix_rows(self, p):
        return p.matrix_rows + [p.matrix_row]

    @_('expression_list')
    def matrix_row(self, p):
        return p.expression_list

    @_('expression "+" expression')
    def expression(self, p):
        return ('add', p.expression0, p.expression1)

    @_('expression "-" expression')
    def expression(self, p):
        return ('sub', p.expression0, p.expression1)

    @_('expression "*" expression')
    def expression(self, p):
        return ('mul', p.expression0, p.expression1)

    @_('expression "/" expression')
    def expression(self, p):
        return ('div', p.expression0, p.expression1)

    @_('expression MATADD expression')
    def expression(self, p):
        return ('matadd', p.expression0, p.expression1)

    @_('expression MATSUB expression')
    def expression(self, p):
        return ('matsub', p.expression0, p.expression1)

    @_('expression MATMUL expression')
    def expression(self, p):
        return ('matmul', p.expression0, p.expression1)

    @_('expression MATDIV expression')
    def expression(self, p):
        return ('matdiv', p.expression0, p.expression1)

    @_('expression EQUALS expression')
    def expression(self, p):
        return ('eq', p.expression0, p.expression1)

    @_('expression NOTEQUALS expression')
    def expression(self, p):
        return ('ne', p.expression0, p.expression1)

    @_('expression LESSEQUALS expression')
    def expression(self, p):
        return ('le', p.expression0, p.expression1)

    @_('expression GREATEREQUALS expression')
    def expression(self, p):
        return ('ge', p.expression0, p.expression1)

    @_('expression "<" expression')
    def expression(self, p):
        return ('lt', p.expression0, p.expression1)

    @_('expression ">" expression')
    def expression(self, p):
        return ('gt', p.expression0, p.expression1)

    @_('"-" expression %prec UMINUS')
    def expression(self, p):
        return ('uminus', p.expression)

    @_('expression "\'"')
    def expression(self, p):
        return ('transpose', p.expression)

    @_('ID "(" expression_list ")"')
    def expression(self, p):
        return ('call', p.ID, p.expression_list)

    @_('ID "[" expression_list "]"')
    def expression(self, p):
        return ('indexed', p.ID, p.expression_list)

    @_('"(" expression ")"')
    def expression(self, p):
        return p.expression

    @_('INT')
    def expression(self, p):
        return ('int', p.INT)

    @_('FLOAT')
    def expression(self, p):
        return ('float', p.FLOAT)

    @_('STRING')
    def expression(self, p):
        return ('string', p.STRING)

    @_('ID')
    def expression(self, p):
        return ('id', p.ID)

    @_('EYE "(" INT ")"')
    def expression(self, p):
        return ('eye', p.INT)

    @_('ZEROS "(" INT ")"')
    def expression(self, p):
        return ('zeros', p.INT)

    @_('ONES "(" INT ")"')
    def expression(self, p):
        return ('ones', p.INT)

    def error(self, token):
        if token:
            lineno = token.lineno
            print(f"Syntax error in line {lineno}: Unexpected token {token.type}")
        else:
            print("Syntax error: Unexpected end of input")

