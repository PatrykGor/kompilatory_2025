

class Node(object):
    pass

class IntNum(Node):
    def __init__(self, value):
        self.value = value

class FloatNum(Node):
    def __init__(self, value):
        self.value = value

class String(Node):
    def __init__(self, value):
        self.value = value

class Variable(Node):
    def __init__(self, name):
        self.name = name

class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class RelExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class UnaryExpr(Node):
    def __init__(self, op, variable):
        self.op = op
        self.variable = variable
    
class AssignExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right
                 
class Block(Node):
    def __init__(self, content):
        self.content = content

class If(Node):
    def __init__(self, condition, instruction, else_instruction=None):
        self.condition = condition
        self.instruction = instruction
        self.else_instruction = else_instruction

class While(Node):
    def __init__(self, condition, instruction):
        self.condition = condition
        self.instruction = instruction

class For(Node):
    def __init__(self, variable, Range, instruction):
        self.variable = variable
        self.Range = Range
        self.instruction = instruction

class Break(Node):
    def __init__(self):
        pass

class Continue(Node):
    def __init__(self):
        pass

class Return(Node):
    def __init__(self, value):
        self.value = value

class Print(Node):
    def __init__(self, value):
        self.value = value

class Zeros(Node):
    def __init__(self, value):
        self.value = value

class Eye(Node):
    def __init__(self, value):
        self.value = value
        
class Ones(Node):
    def __init__(self, value):
        self.value = value

class Transpose(Node):
    def __init__(self, value):
        self.value = value

class Reference(Node):
    def __init__(self, array, indices):
        self.array = array
        self.indices = indices

class Vector(Node):
    def __init__(self, elements):
        self.elements = elements
        
class Range(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Error(Node):
    def __init__(self):
        pass
      
