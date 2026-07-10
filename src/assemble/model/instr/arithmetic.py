from dataclasses import dataclass

from src.assemble.model.operand.value import LValue, Value, Operand

from src.assemble.model.instr.instr import Instr

@dataclass(frozen=True)
class Arithmetic(Instr):
    def __repr__(self, ident:int=0) -> str:
        raise

@dataclass(frozen=True)
class ADD(Instr):
    dst: LValue
    src1: Value
    src2: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"ADD {self.dst}, {self.src1}, {self.src2}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1, self.src2]


@dataclass(frozen=True)
class SUB(Instr):
    dst: LValue
    src1: Value
    src2: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"SUB {self.dst}, {self.src1}, {self.src2}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1, self.src2]


@dataclass(frozen=True)
class MUL(Instr):
    dst: LValue
    src1: Value
    src2: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"MUL {self.dst}, {self.src1}, {self.src2}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1, self.src2]


@dataclass(frozen=True)
class DIV(Instr):
    dst: LValue
    src1: Value
    src2: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"DIV {self.dst}, {self.src1}, {self.src2}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1, self.src2]


@dataclass(frozen=True)
class MOD(Instr):
    dst: LValue
    src1: Value
    src2: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"MOD {self.dst}, {self.src1}, {self.src2}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1, self.src2]


@dataclass(frozen=True)
class ABS(Instr):
    dst: LValue
    src1: Value
    def __repr__(self, ident: int = 0) -> str:
        return "    "*ident+f"ABS {self.dst}, {self.src1}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src1]
