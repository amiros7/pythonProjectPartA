import re

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.tokens = []
        self.current_pos = 0

    def tokenize(self):
        token_specification = [
            ('NUMBER',   r'\d+'),
            ('ADD',      r'\+'),
            ('SUB',      r'-'),
            ('MUL',      r'\*'),
            ('DIV',      r'/'),
            ('MOD',      r'%'),
            ('AND',      r'&&'),
            ('OR',       r'\|\|'),
            ('NOT',      r'!'),
            ('EQ',       r'=='),
            ('NEQ',      r'!='),
            ('GT',       r'>'),
            ('LT',       r'<'),
            ('GTE',      r'>='),
            ('LTE',      r'<='),
            ('LPAREN',   r'\('),
            ('RPAREN',   r'\)'),
            ('NAME',     r'[a-zA-Z_]\w*'),
            ('SKIP',     r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]

        token_regex = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in token_specification)
        for match in re.finditer(token_regex, self.source_code):
            kind = match.lastgroup
            value = match.group(kind)
            if kind == 'NUMBER':
                value = int(value)
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise SyntaxError(f'Unexpected token: {value}')
            self.tokens.append((kind, value))
        return self.tokens
