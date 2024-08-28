from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

class REPL:
    def __init__(self):
        pass

    def start(self):
        while True:
            try:
                line = input('>> ')
                if line.lower() in ['exit', 'quit']:
                    break
                lexer = Lexer(line)
                tokens = lexer.tokenize()
                parser = Parser(tokens)
                ast = parser.parse()
                interpreter = Interpreter(ast)
                interpreter.interpret()
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    repl = REPL()
    repl.start()
