from enum import Enum

class Reserve(Enum):
    space = {' ', '\t', '\n'}
    next_line = '\n'
    underline = '_'
    dot = '.'
    quote = "'"
    operations = {'+', '-', '*', '/', '=', '<', '>', '**','<=','>=','<<','>>',
                  "div", "mod", "not", "and", "or", "ord", "chr", "sizeof", "pi",
                  "int", "trunc", "round", "frac", "odd"}
    plus_minus = {'+', '-'}
    multiply_divide = {'*', '/'}
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
    open_brace = '{'
    close_brace = '}'
    int_formats = {16: '$', 8:'&', 2: '%'}
    tab = '\t'