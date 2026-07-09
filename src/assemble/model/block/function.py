from dataclasses import dataclass

from src.assemble.model.block.block import Block
from src.assemble.model.operand.value import FunctionLabel, Register

@dataclass(frozen=True)
class Function():
    instr:list[Block]
    label:FunctionLabel
    parms: list[Register]
    def __repr__(self, ident:int=0) -> str:
        return \
            "    "*ident+self.label.__repr__()+\
            f"({", ".join([repr(i) for i in self.parms])})"+\
            "{\n"+"\n".join([i.__repr__(ident=ident+1) for i in self.instr])+\
            "\n"+"    "*ident+"}"