from dataclasses import dataclass

from src.assemble.model.instr.instr import Instr

from src.assemble.model.operand.value import CodeLabel

@dataclass(frozen=True)
class Block():
    instr:list[Instr]
    label:CodeLabel
    def __repr__(self, ident:int=0) -> str:
        return \
            "    "*ident+":"+self.label.__repr__()+"\n"+\
            "\n".join([i.__repr__(ident=ident+1) for i in self.instr])