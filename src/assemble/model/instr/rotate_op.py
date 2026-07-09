from dataclasses import dataclass

from src.assemble.model.instr.instr import Instr

@dataclass(frozen=True)
class Rotate_Operation(Instr):
    pass