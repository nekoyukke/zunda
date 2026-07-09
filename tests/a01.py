from src.assemble.parser.lexer import Lexer
from src.assemble.parser.parser import Parser

source = """
.data $NAME #"hello world"

@main(){
:entry
MOV %R2, #0
MOV %R1, $NAME
:end
ADD %R3, %R1, %R2
}
"""
lex = Lexer(source)
print(lex.tokenize())
pas = Parser(lex.tokenize(), source)
print(pas.parse())