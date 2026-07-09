from dataclasses import dataclass

from src.assemble.model.instr.instr import Instr

@dataclass(frozen=True)
class Nop(Instr):
    def __repr__(self, ident:int=0) -> str:
        return "    "*ident+"NOP"