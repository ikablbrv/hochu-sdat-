class Lexem:
    def __init__(self, coordinate, type, code, value):
        self.coordinate = coordinate
        self.type = type
        self.code = code
        self.value = value
        self.tab = '    '

    def to_string(self):
        return f'{self.coordinate}{self.tab * 2}{self.type}{self.tab * 2}{self.code}{self.tab * 2}{self.value}'

    def is_end(self):
        return self.type == 'end'

    def get_coordinate(self):
        return self.coordinate

    def get_type(self):
        return self.type

    def get_code(self):
        return self.code

    def get_value(self):
        return self.value