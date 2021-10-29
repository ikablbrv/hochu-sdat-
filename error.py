class CompilerError(Exception):
    pass

class LexicalError(CompilerError):
    pass

class SyntaxError(CompilerError):
    pass