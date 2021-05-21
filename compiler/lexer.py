from rply import LexerGenerator


class Lexer:
    def __init__(self):
        self.lexer = LexerGenerator()
        self.__add_tokens()

    def __add_tokens(self):
        # Constant Contractor
        self.lexer.add('e', r'-?__E__')
        self.lexer.add('Pi', r'-?__PI__')
        self.lexer.add('integer', r'-?\d+')
        self.lexer.add('float', r'-?\d+\.\d+')
        self.lexer.add('string', r'(""".*""")|(".*")|(\'.*\')')
        self.lexer.add('boolean', r'true(?!\w)|false(?!\w)|True(?!\w)|False(?!\w)|TRUE(?!\w)|FALSE(?!\w)')

        # Mathematical Contractor
        self.lexer.add('sum', r'\+')
        self.lexer.add('sub', r'\-')
        self.lexer.add('mul', r'\*')
        self.lexer.add('div', r'\/')

        # Binary Contractor
        self.lexer.add('==', r'\=\=')
        self.lexer.add('>=', r'\>\=')
        self.lexer.add('<=', r'\<\=')
        self.lexer.add('!=', r'\!\=')
        self.lexer.add('>', r'\>')
        self.lexer.add('<', r'\<')
        self.lexer.add('and', r'and(?!\w)')
        self.lexer.add('or', r'or(?!\w)')

        # Statement Contractor
        self.lexer.add('if', r'if(?!\w)')
        self.lexer.add('else', r'else(?!\w)')

        # Semi Colon Contractor
        self.lexer.add(',', r'\,')
        self.lexer.add(';', r'\;')

        # Parenthesis Contractor
        self.lexer.add('(', r'\(')
        self.lexer.add(')', r'\)')
        self.lexer.add('{', r'\{')
        self.lexer.add('}', r'\}')

        # Function Contractor
        self.lexer.add('input', r'input')
        self.lexer.add('function', r'function')
        self.lexer.add('print', r'print')
        self.lexer.add('sin', r'sin')
        self.lexer.add('cos', r'cos')
        self.lexer.add('tan', r'tan')
        self.lexer.add('power', r'pow')
        self.lexer.add('absolute', r'abs')

        # Assignment Contractor
        self.lexer.add('set', r'set(?!\w)')
        self.lexer.add('identifier', "[a-zA-Z_][a-zA-Z0-9_]*")
        self.lexer.add('=', r'\=')

        # Ignore spaces
        self.lexer.ignore('\s+')

    def build(self):
        return self.lexer.build()
