from dataclasses import dataclass

@dataclass(frozen=True)
class Instr():
    def __repr__(self, ident:int=0) -> str:
        raise