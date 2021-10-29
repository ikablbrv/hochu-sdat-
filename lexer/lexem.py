class Lexem:
    def __init__(self, coordinate, type, code, value):
        self.coordinate = coordinate
        self.type = type
        self.code = code
        self.value = value

    def to_string(self):
        tab = "\t" * 2
        return f'{self.coordinate}{tab}{self.type}{tab}{self.code}{tab}{self.value}'

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