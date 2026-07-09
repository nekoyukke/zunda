from src.assemble.model.block.block import *
from src.assemble.model.block.function import *
from src.assemble.model.block.program import *
from src.assemble.model.block.section import *
from src.assemble.model.instr.instr import *
from src.assemble.model.instr.arithmetic import *
from src.assemble.model.instr.bit_op import *
from src.assemble.model.instr.branch import *
from src.assemble.model.instr.call import *
from src.assemble.model.instr.halt import *
from src.assemble.model.instr.move import *
from src.assemble.model.instr.nop import *
from src.assemble.model.instr.rotate_op import *
from src.assemble.model.instr.shift_op import *
from src.assemble.model.operand.value import *

from src.assemble.parser.token import *

class Parser():
    def __init__(self, toks:list[Token], source:str) -> None:
        self.tokens = toks
        self.souece = source
        self.pos = 0
    
    def peek(self) -> Token:
        """現在のトークンを覗き見る"""
        return self.tokens[self.pos]

    def is_at_end(self) -> bool:
        """最後まで行ったか"""
        return self.peek().type == TokenType.EOF

    def advance(self) -> Token:
        """一つ進めて、進める前のトークンを返す"""
        if not self.is_at_end():
            self.pos += 1
        return self.previous()

    def previous(self) -> Token:
        """一つ前のトークン"""
        return self.tokens[self.pos - 1]

    def check(self, type: TokenType) -> bool:
        """型が一致するか確認(消費しない)"""
        if self.is_at_end():
            return False
        return self.peek().type == type

    def match(self, *types: TokenType) -> bool:
        """型が一致すれば消費してTrue"""
        for t in types:
            if self.check(t):
                self.advance()
                return True
        return False
    
    def accept(self, *types: TokenType) -> Token | None:
        """型が一致すれば消費してそれ自身を返し、そうでなければNoneを返す"""
        for t in types:
            if self.check(t):
                res = self.advance()
                return res 
        return

    def consume(self, type: TokenType, message: str) -> Token:
        """期待した型なら消費、違えばError"""
        if self.check(type):
            return self.advance()
        current = self.peek()
        self.CallError(message+repr(current))
    
    def CallError(
            self, message:str
        ):
        """
        エラー呼び出し
        """
        raise RuntimeError(message)
    
    def register(self) -> Register:
        self.consume(TokenType.MOD, "レジスタには%が必要です")
        register = self.consume(TokenType.ID, "レジスタIDが不明です")
        return Register(register.value)
    
    def immediate(self) -> Immediate:
        self.consume(TokenType.SHARP, "定数には#が必要です")
        if self.peek().type==TokenType.STRING:
            return Immediate_String(self.advance().value)
        else:
            return Immediate_Int(int(self.advance().value))
    
    def memory(self) -> Memory:
        self.consume(TokenType.LBRACKET, "メモリ始まりが不明")
        reg = self.register()
        self.consume(TokenType.LBRACKET, "メモリ終わりが不明")
        return Memory(reg)
    
    def value_label(self) -> ValueLabel:
        self.consume(TokenType.DOLLAR, "value label始まり不明")
        vl = self.consume(TokenType.ID, "IDが不明です")
        return ValueLabel(vl.value)
    
    def rvalue(self) -> RValue:
        if self.peek().type == TokenType.DOLLAR:
            return self.value_label()
        else:
            return self.immediate()
    
    def lvalue(self) -> LValue:
        if self.peek().type == TokenType.MOD:
            return self.register()
        else:
            return self.memory()
        
    def value(self) -> Value:
        if self.peek().type == TokenType.DOLLAR:
            return self.value_label()
        elif self.peek().type == TokenType.SHARP:
            return self.immediate()
        elif self.peek().type == TokenType.MOD:
            return self.register()
        else:
            return self.memory()
    
    def parse(self) -> Program:
        instr:list[Function] = []
        section:list[Section] = []
        while self.peek().type != TokenType.EOF:
            stmt = self.stmt()
            if isinstance(stmt, Function):
                instr += [stmt]
            else:
                section += [stmt]
        return Program(instr, section)
    
    def stmt(self) -> Function | Section:
        if self.match(TokenType.DOT):
            return self.section()
        else:
            return self.function()

    def section(self) -> Section:
        section = self.consume(TokenType.ID, "IDが不明です")
        if section.value == "data":
            kind = SectionKind.DATA
        else:
            raise
        name = self.value_label()
        lv = self.rvalue()
        return Section(kind,  name, lv)
    
    def function(self) -> Function:
        self.consume(TokenType.AT, "関数定義が不明")
        name = self.consume(TokenType.ID, "IDが不明")
        self.consume(TokenType.LPAREN, "不明")
        reg: list[Register] = []
        while not self.match(TokenType.RPAREN):
            reg += [self.register()]
            if not self.match(TokenType.COMMA):
                if self.match(TokenType.RPAREN):
                   break
        self.consume(TokenType.LBRACE, "bodyが不明")
        bk:list[Block] = []
        while not self.match(TokenType.RBRACE):
            bk += [self.block()]
        return Function(bk, FunctionLabel(name.value), reg)

    def block(self) -> Block:
        self.consume(TokenType.COLON, "不明なBlock名")
        name = self.consume(TokenType.ID, "不明なBlock名前")
        instr: list[Instr] = []
        while not self.check(TokenType.COLON):
            instr+=[self.instr()]
            if self.check(TokenType.RBRACE):
                break
        return Block(instr, CodeLabel(name.value))
    
    def instr(self) -> Instr:
        match (self.advance().value):
            case "ADD":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                self.consume(TokenType.COMMA, "commaないです")
                v2 = self.value()
                return ADD(lv, v1, v2)
            case "SUB":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                self.consume(TokenType.COMMA, "commaないです")
                v2 = self.value()
                return SUB(lv, v1, v2)
            case "MUL":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                self.consume(TokenType.COMMA, "commaないです")
                v2 = self.value()
                return MUL(lv, v1, v2)
            case "DIV":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                self.consume(TokenType.COMMA, "commaないです")
                v2 = self.value()
                return DIV(lv, v1, v2)
            case "MOD":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                self.consume(TokenType.COMMA, "commaないです")
                v2 = self.value()
                return MOD(lv, v1, v2)
            case "ABS":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                return ABS(lv, v1)
            case "HALT":
                return Halt()
            case "NOP":
                return Nop()
            case "MOV":
                lv = self.lvalue()
                self.consume(TokenType.COMMA, "commaないです")
                v1 = self.value()
                return Move(lv, v1)
            case _:
                raise RuntimeError(self.tokens[self.pos-1])