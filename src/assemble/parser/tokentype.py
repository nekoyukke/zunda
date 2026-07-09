from enum import Enum

class TokenType(Enum):
    # 演算子
    COMMENT = r';[^\n]*'
    ASSIGN = r'='
    LBRACE = r'\{'
    RBRACE = r'\}'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LPAREN = r'\('
    RPAREN = r'\)'
    COMMA = r','
    SHARP = r'#'
    DOLLAR = r'\$'
    MOD = r'%'
    AT = r'@'
    COLON = r':'

    # 可変
    SKIP = r'\s+'
    STRING = r'"(\\.|[^"\\])*"'
    NUMBER  = r'\d+'
    ID = r'[a-zA-Z_][a-zA-Z0-9_]*'

    # Section
    DOT = r'.'

    # 特殊
    EOF = ""
