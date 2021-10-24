from enum import Enum

class Reserve(Enum): # это резерв для символов и слов
    space = {' ', '\t', '\n'}  # \t - табуляция \n - новая строка
    next_line = '\n'
    underline = '_'
    dot = '.'
    quote = "'"
    operations = {'+', '-', '*', '/', '=', '<', '>', "div", "mod", "not", "and", "or", "ord", "chr", "sizeof", "pi",
                  "int", "trunc", "round", "frac", "odd"}
    plus_minus = {'+', '-'}
    multiply_divide = {'*', '/'}
    degree = '**' #степень
    reserved = {"array", "asm", "begin", "case", "const", "constructor", "destructor", "do",
                "downto", "else", "end", "exports", "file", "for", "function", "goto", "if",
                "implementation","in", "inherited", "inline", "interface", "label", "library", "nil",
                "object","of", "packed", "procedure", "program", "record", "repeat", "set", "shl",
                "shr","string", "then", "to", "type", "unit", "until", "uses", "var", "while", "with",
                "xor","abs", "arctan", "boolean", "char", "cos", "dispose", "eof", "eoln", "exp",
                "false", "get", "input", "integer", "ln", "maxint", "new", "output",
                "pack", "page", "pred", "put", "read", "readln", "real", "reset", "rewrite",
                "sin", "sqr", "sqrt", "succ", "text", "true", "unpack", "write", "writeln"}
    separators = {'.', ',', ':', ';', '(', ')', '[', ']'}
    open_bracket = '('
    close_bracket = ')'
    assignments = {":=", "+=", "-=", "*=", "/="}
    comments = '//'
    tab = '    '