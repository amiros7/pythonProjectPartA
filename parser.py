class ASTNode:
    def evaluate(self, environment):
        raise NotImplementedError()

class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def evaluate(self, environment):
        return self.value

class BinaryOperationNode(ASTNode):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def evaluate(self, environment):
        left_value = self.left.evaluate(environment)
        right_value = self.right.evaluate(environment)

        if self.operator == 'ADD':
            return left_value + right_value
        elif self.operator == 'SUB':
            return left_value - right_value
        elif self.operator == 'MUL':
            return left_value * right_value
        elif self.operator == 'DIV':
            return left_value // right_value
        elif self.operator == 'MOD':
            return left_value % right_value
        elif self.operator == 'AND':
            return left_value and right_value
        elif self.operator == 'OR':
            return left_value or right_value
        elif self.operator == 'EQ':
            return left_value == right_value
        elif self.operator == 'NEQ':
            return left_value != right_value
        elif self.operator == 'GT':
            return left_value > right_value
        elif self.operator == 'LT':
            return left_value < right_value
        elif self.operator == 'GTE':
            return left_value >= right_value
        elif self.operator == 'LTE':
            return left_value <= right_value
        else:
            raise ValueError(f"Unknown operator: {self.operator}")

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        node = self.parse_term()

        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('ADD', 'SUB'):
            operator = self.tokens[self.pos][0]
            self.pos += 1
            right = self.parse_term()
            node = BinaryOperationNode(node, operator, right)

        return node

    def parse_term(self):
        node = self.parse_factor()

        while self.pos < len(self.tokens) and self.tokens[self.pos][0] in ('MUL', 'DIV', 'MOD'):
            operator = self.tokens[self.pos][0]
            self.pos += 1
            right = self.parse_factor()
            node = BinaryOperationNode(node, operator, right)

        return node

    def parse_factor(self):
        token_type, value = self.tokens[self.pos]
        self.pos += 1

        if token_type == 'NUMBER':
            return NumberNode(value)
        elif token_type == 'LPAREN':
            node = self.parse_expression()
            if self.tokens[self.pos][0] != 'RPAREN':
                raise SyntaxError("Missing closing parenthesis")
            self.pos += 1
            return node
        else:
            raise SyntaxError(f"Unexpected token: {token_type}")
