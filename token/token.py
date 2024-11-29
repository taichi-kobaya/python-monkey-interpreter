class TokenType:
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # 識別子 + リテラル
    IDENT = "IDENT"  # add, foobar, x, y, ...
    INT = "INT"      # 1343456

    # 演算子
    ASSIGN = "="
    PLUS = "+"

    # デリミタ
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # キーワード
    FUNCTION = "FUNCTION"
    LET = "LET"

class Token:
    def __init__(self, type:str, literal:str):
        self.type = type
        self.literal = literal