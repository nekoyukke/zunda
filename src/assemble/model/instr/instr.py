from dataclasses import dataclass


from src.assemble.model.operand.value import Operand

@dataclass(frozen=True)
class Instr():
    def __repr__(self, ident:int=0) -> str:
        raise
    def get_children(self) -> list[Operand]:
        raise