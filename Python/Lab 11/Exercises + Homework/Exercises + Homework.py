from math import factorial
from sly import Lexer, Parser


class CalcLexer(Lexer):
    tokens = {NAME, NUMBER, PLUS, MINUS, MULTIPLY, DIVIDE, PARENTHESIS_OPEN, PARENTHESIS_CLOSE, POWER, FACTORTIAL, ASSIGN}
    ignore = ' \t'

    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    NUMBER = r'\d+'

    PLUS = r'\+'
    MINUS = r'-'
    ASSIGN = r'='
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    PARENTHESIS_OPEN = r'\('
    PARENTHESIS_CLOSE = r'\)'
    POWER = r'\^'
    FACTORTIAL = r'!'


class CalcParser(Parser):
    tokens = CalcLexer.tokens

    def __init__(self):
        self.names = {}

    @_('NAME ASSIGN expr')
    def statement(self, p):
        self.names[p.NAME] = p.expr

    @_('expr')
    def statement(self, p):
        print(p.expr)

    @_('expr PLUS expr')
    def expr(self, p):
        return p.expr0 + p.expr1

    @_('expr MINUS expr')
    def expr(self, p):
        return p.expr0 - p.expr1

    @_('NUMBER')
    def expr(self, p):
        return int(p.NUMBER)

    @_('expr MULTIPLY expr')
    def expr(self, p):
        return p.expr0 * p.expr1

    @_('expr DIVIDE expr')
    def expr(self, p):
        return p.expr0 / p.expr1

    @_('PARENTHESIS_OPEN expr PARENTHESIS_CLOSE')
    def expr(self, p):
        return p.expr

    @_('expr POWER expr')
    def expr(self, p):
        return p.expr0 ** p.expr1

    @_('expr FACTORTIAL')
    def expr(self, p):
        return factorial(p.expr)


if __name__ == '__main__':
    lexer = CalcLexer()
    parser = CalcParser()
    while True:
        try:
            text = input('calc > ')
        except EOFError:
            break
        if text:
            parser.parse(lexer.tokenize(text))