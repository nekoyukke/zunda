from dataclasses import dataclass

from src.assemble.model.instr.instr import Instr

from src.assemble.model.operand.value import LValue, Value, Operand

@dataclass(frozen=True)
class Move(Instr):
    dst: LValue
    src: Value
    def __repr__(self, ident:int=0) -> str:
        return "    "*ident+f"MOV {self.dst}, {self.src}"
    def get_children(self) -> list[Operand]:
        return [self.dst, self.src]