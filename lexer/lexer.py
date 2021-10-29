from enum import Enum
from lexer.lexem import Lexem
from error import LexicalError
from Reserve import Reserve


class States(Enum):
    start = 'start'
    integer = 'integer'
    integer16 = 'integer16'
    integer8 = 'integer8'
    integer2 = 'integer2'
    real = 'real'
    identifier = 'identifier'
    reserved = 'reserved'
    string = 'string'
    operation = 'operation'
    separator = 'separator'
    assignment = 'assignment'
    comment = 'comment'
    comment2 = 'comment2'
    end_of_file = 'end'
    error = 'error'


class Lexer:
    def __init__(self, path):
        self.file = open(path, 'r')
        self.col = 0
        self.line = 1
        self.state = States.start
        self.symbol = ''
        self.next_symbol()
        self.buf = ''
        self.coordinates = []

    def next_lexem(self):
        self.clear_buf()
        while self.buf or self.symbol:
            if self.state == States.start:
                if self.symbol in Reserve.space.value:
                    if self.symbol == Reserve.next_line.value:
                        self.next_line()
                    self.next_symbol()
                elif self.symbol.isalpha():
                    self.state = States.identifier
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol.isdigit():
                    self.state = States.integer
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol == Reserve.int_formats.value[16]:
                    self.state = States.integer16
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol == Reserve.int_formats.value[8]:
                    self.state = States.integer8
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol == Reserve.int_formats.value[2]:
                    self.state = States.integer2
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol == Reserve.quote.value:
                    self.state = States.string
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol in Reserve.operations.value:
                    self.state = States.operation
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol in Reserve.separators.value:
                    self.state = States.separator
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()
                elif self.symbol == Reserve.open_brace.value:
                    self.state = States.comment2
                    self.next_symbol()
                else:
                    self.state = States.error
                    self.add_buf()
                    self.save_coordinates()
                    self.next_symbol()

            elif self.state == States.identifier:
                if self.symbol.isalpha() or self.symbol.isdigit() or self.symbol == Reserve.underline.value:
                    self.add_buf()
                    self.next_symbol()
                else:
                    if self.buf in Reserve.reserved.value:
                        self.state = States.reserved
                    elif self.buf in Reserve.operations.value:
                        self.state = States.operation
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf.lower())
                    self.state = States.start
                    return self.lexem

            elif self.state == States.integer:
                if self.symbol.isdigit():
                    self.add_buf()
                    self.next_symbol()
                elif self.symbol == Reserve.dot.value:
                    self.state = States.real
                    self.add_buf()
                    self.next_symbol()
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, int(self.buf))
                    self.state = States.start
                    return self.lexem

            elif self.state == States.integer16:
                if self.symbol.isdigit() or 'a' <= self.symbol.lower() <= 'f':
                    self.add_buf()
                    self.next_symbol()
                elif len(self.buf) == 1 or 'g' <= self.symbol.lower() <= 'z':
                    self.state = States.error
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, int(self.buf[1:], 16))
                    self.state = States.start
                    return self.lexem

            elif self.state == States.integer8:
                if '0' <= self.symbol <= '7':
                    self.add_buf()
                    self.next_symbol()
                elif len(self.buf) == 1 or self.symbol >= '8':
                    self.state = States.error
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, int(self.buf[1:], 8))
                    self.state = States.start
                    return self.lexem

            elif self.state == States.integer2:
                if '0' <= self.symbol <= '1':
                    self.add_buf()
                    self.next_symbol()
                elif len(self.buf) == 1 or self.symbol >= '2':
                    self.state = States.error
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, int(self.buf[1:], 2))
                    self.state = States.start
                    return self.lexem

            elif self.state == States.real:
                if self.symbol.isdigit():
                    self.add_buf()
                    self.next_symbol()
                elif self.symbol == Reserve.dot.value:
                    self.state = States.error
                    self.add_buf()
                    self.next_symbol()
                else:
                    if self.buf.endswith(Reserve.dot.value):
                        self.state = States.error
                    else:
                        self.lexem = Lexem(self.coordinates, self.state.value, self.buf, float(self.buf))
                        self.state = States.start
                        return self.lexem

            elif self.state == States.string:
                if not self.symbol or self.symbol == Reserve.next_line.value:
                    raise LexicalError(f'{self.coordinates}{Reserve.tab.value * 2}Lexical Error: {self.buf}')
                elif not self.symbol == Reserve.quote.value:
                    self.add_buf()
                    self.next_symbol()
                else:
                    self.add_buf()
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    self.next_symbol()
                    return self.lexem

            elif self.state == States.operation:
                if self.buf + self.symbol in Reserve.operations.value:
                    self.add_buf()
                    self.next_symbol()
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    return self.lexem
                elif self.buf + self.symbol in Reserve.assignments.value:
                    self.add_buf()
                    self.next_symbol()
                    self.state = States.assignment
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    return self.lexem
                elif self.symbol + self.buf == Reserve.comments.value:
                    self.clear_buf()
                    self.next_symbol()
                    self.state = States.comment
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    return self.lexem

            elif self.state == States.comment:
                if self.symbol == Reserve.next_line.value:
                    self.next_line()
                    self.next_symbol()
                    self.state = States.start
                else:
                    self.next_symbol()

            elif self.state == States.comment2:
                if self.symbol == Reserve.next_line.value:
                    self.next_line()
                elif self.symbol == Reserve.close_brace.value:
                    self.state = States.start
                self.next_symbol()

            elif self.state == States.separator:
                if self.buf + self.symbol in Reserve.assignments.value:
                    self.add_buf()
                    self.next_symbol()
                    self.state = States.assignment
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    return self.lexem
                else:
                    self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf)
                    self.state = States.start
                    return self.lexem

            elif self.state == States.error:
                if self.symbol in Reserve.space.value or self.symbol in Reserve.separators.value or not self.symbol:
                    raise LexicalError(f'{self.coordinates}{Reserve.tab.value * 2}Lexical Error: {self.buf}')
                self.add_buf()
                self.next_symbol()

        self.save_coordinates()
        self.state = States.end_of_file
        self.lexem = Lexem(self.coordinates, self.state.value, self.buf, self.buf.lower())
        return self.lexem

    def current_lexem(self):
        return self.lexem

    def next_symbol(self):
        self.symbol = self.file.read(1)
        self.col += 1

    def next_line(self):
        self.col = 0
        self.line += 1

    def clear_buf(self):
        self.buf = ''

    def add_buf(self):
        self.buf += self.symbol

    def save_coordinates(self):
        self.coordinates = [self.line, self.col]
