from Reserve import Reserve


class Node:
    def to_string(self, level=1):
        pass


class IdNode(Node):
    def __init__(self, lexem):
        self.lexem = lexem

    def to_string(self, level=1):
        return f'{self.lexem.get_value()}'


class IntNode(Node):
    def __init__(self, lexem):
        self.lexem = lexem

    def to_string(self, level=1):
        return f'{self.lexem.get_value()}'


class RealNode(Node):
    def __init__(self, lexem):
        self.lexem = lexem

    def to_string(self, level=1):
        return f'{self.lexem.get_value()}'


class UnOpNode(Node):
    def __init__(self, operand, operation):
        self.operand = operand
        self.operation = operation

    def to_string(self, level=1):
        return f'{self.operation.get_value()}{self.operand.to_string()}'


class BinOpNode(Node):
    def __init__(self, operand1, operation, operand2):
        self.operand1 = operand1
        self.operation = operation
        self.operand2 = operand2

    def to_string(self, level=1):
        operation = self.operation.get_value()
        operand1 = self.operand1.to_string(level + 1)
        operand2 = self.operand2.to_string(level + 1)
        return f'{operation}\n' \
               f'{Reserve.tab.value * level}{operand1}\n' \
               f'{Reserve.tab.value * level}{operand2}'
