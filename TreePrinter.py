import AST
INDENT_STRING = "| "

def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator

class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + str(self.value))

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + str(self.value))

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + self.name)

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.RelExpr)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + self.op)
        self.variable.printTree(indent + 1)

    @addToClass(AST.AssignExpr)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + self.op)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        for instruction in self.content:
            instruction.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "IF")
        self.condition.printTree(indent + 1)
        print(INDENT_STRING * indent + "THEN")
        self.instruction.printTree(indent + 1)
        if self.else_instruction is not None:
            print(INDENT_STRING * indent + "ELSE")
            self.else_instruction.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "WHILE")
        self.condition.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "FOR")
        self.variable.printTree(indent + 1)
        self.Range.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "RETURN")
        self.value.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "PRINT")
        for val in self.value:
            val.printTree(indent + 1)

    @addToClass(AST.Zeros)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "zeros")
        for val in self.values:
            val.printTree(indent + 1)

    @addToClass(AST.Eye)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "eye")
        self.value.printTree(indent + 1)

    @addToClass(AST.Ones)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "ones")
        for val in self.values:
            val.printTree(indent + 1)
            
    @addToClass(AST.Transpose)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "TRANSPOSE")
        self.value.printTree(indent + 1)

    @addToClass(AST.Reference)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "REF")
        self.array.printTree(indent + 1)
        for index in self.indices:
            index.printTree(indent + 1)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "VECTOR")
        for element in self.elements:
            element.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print(INDENT_STRING * indent + "RANGE")
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass

