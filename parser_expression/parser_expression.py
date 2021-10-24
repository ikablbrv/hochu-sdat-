from error import SyntaxError
from Reserve import Reserve
from lexer.lexer import States
from parser_expression.node import IdNode, IntNode, RealNode, UnOpNode, BinOpNode

class ParserExpression:
    def __init__(self, lexer):
        self.lexer = lexer

    def expr(self):
        lexem = self.lexer.current_lexem()
        if lexem.is_end():
            raise SyntaxError(f'{lexem.get_coordinate()}{Reserve.tab.value * 2}Syntax Error: expression was expected')
        left = self.term()
        operation = self.lexer.current_lexem()
        while operation.get_code() in Reserve.plus_minus.value:
            self.lexer.next_lexem()
            right = self.term()
            left = BinOpNode(left, operation, right)
            operation = self.lexer.current_lexem()
        return left

    def term(self):
        left = self.factor()
        operation = self.lexer.current_lexem()
        while operation.get_code() in Reserve.multiply_divide.value:
            self.lexer.next_lexem()
            right = self.factor()
            left = BinOpNode(left, operation, right)
            operation = self.lexer.current_lexem()
        return left

    def factor(self):
        lexem = self.lexer.current_lexem()
        self.lexer.next_lexem()
        if lexem.get_type() == States.identifier.value:
            return IdNode(lexem)
        elif lexem.get_type() == States.integer.value:
            return IntNode(lexem)
        elif lexem.get_type() == States.real.value:
            return RealNode(lexem)
        elif lexem.get_code() in Reserve.plus_minus.value:
            operand = self.factor()
            return UnOpNode(operand, lexem)
        elif lexem.get_code() == Reserve.open_bracket.value:
            left = self.expr()
            lexem = self.lexer.current_lexem()
            if lexem.get_code() != Reserve.close_bracket.value:
                raise SyntaxError(f'{lexem.get_coordinate()}{Reserve.tab.value * 2}Syntax Error: ")" was expected')
            self.lexer.next_lexem()
            return left
        raise SyntaxError(f'{lexem.get_coordinate()}{Reserve.tab.value * 2}Syntax Error: {lexem.get_code()}')

