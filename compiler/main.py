from compiler.lexer import Lexer
from compiler.parser import Parser, ParserState
from compiler.JSONparsedTree import Node, write
from rply.lexer import LexerStream
from copy import copy
from pprint import pprint
import traceback

basicProgram = """
    set a = 60;
    set b = 2;
    set c = a + b * 60;
    print(c);
    print(a);
"""
declareCallFunc = """
function main() {
    set a = 60;
    set b = 2;
    set c = b + a * 60;
    print(c);
}
main();
"""
ifElse = """
set a = 10;
set b = 15;
if (a > b) {
    print(a + 10);
    print(21.34 + b);
    print(tan(a * 6));
} else {
    print(abs(3.5 - 4));
    print(sin(3.5 - 4));
    print(cos(__E__ - __PI__));
    print(tan(__PI__ - __E__));
    print(pow(-2, a));
}
"""
someOp = """
    set a = 5 - 2;
    set b = 5;
    print(sin(a));
    print(cos(b));
    print(abs(a-b));
    print(pow(a,b));
"""
userDefinedFunc = """
function sum(){
    set a = 5;
    set b = 7;
    print(a + b + 10);
}
function userDefined() {
    set pi = __PI__;
    set e = __E__;
    print(pi);
    print(e);
    print(2 * (pi + e - 1) / 3);
    print(abs(e - pi));
    print(sin(pi));
    print(cos(pi));
    print(tan(pi));
    print(pow(pi, e));
    print(__PI__);
    print(__E__);
}

function main() {
    set i = input("Input a number: ");
    if (i > 5) {
        print();
        print("Call User Defined Function: ");
        userDefined();
    } else {
        print();
        print("Call Sum Function: ");
        sum();
    }
}

main();
"""

lexer = Lexer().build()  # Build the lexer using LexerGenerator
tokens: LexerStream
try:
    tokens = lexer.lex(userDefinedFunc)  # Stream the input to analysis the lexical syntax
    tokenType = map(lambda x: x.gettokentype(), copy(tokens))
    tokenName = map(lambda x: x.getstr(), copy(tokens))
    pprint(list(copy(tokens)))
    # pprint(list(copy(tokenType)))
    # pprint(list(copy(tokenName)))
except (BaseException, Exception):
    traceback.print_exc()
finally:
    print("Finish lexical analysis !")

SymbolTable = ParserState()
syntaxRoot: Node
semanticRoot = Node("main")
try:
    syntaxRoot = Node("main", Parser(syntax=True).build().parse(copy(tokens), state=SymbolTable))  # Get syntax tree !
    Parser().build().parse(copy(tokens), state=SymbolTable).eval(semanticRoot)  # Get semantic tree !
except (BaseException, Exception):
    traceback.print_exc()
finally:
    write(syntaxRoot, "SyntaxAnalyzer")
    write(semanticRoot, "SemanticAnalyzer")
    print("-----------------------------------------Symbol Table------------------------------------------")
    print("------------------------------Declared Variables & Functions are:------------------------------")
    pprint(SymbolTable.variables)
    pprint(SymbolTable.functions)
