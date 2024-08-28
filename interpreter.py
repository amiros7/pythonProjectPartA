from parser import NumberNode, BinaryOperationNode

class Interpreter:
    def __init__(self, ast):
        self.ast = ast
        self.environment = {}

    def interpret(self):
        result = self.ast.evaluate(self.environment)
        print(result)
