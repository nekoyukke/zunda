from dataclasses import dataclass

from src.assemble.model.block.function import Function

from src.assemble.model.block.section import Section

@dataclass(frozen=True)
class Program():
    instr:list[Function]
    section: list[Section]
    def __repr__(self) -> str:
        return "\n".join([i.__repr__()for i in self.section]) + "\n" + "\n".join([i.__repr__()for i in self.instr])