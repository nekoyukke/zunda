from enum import Enum

from dataclasses import dataclass

from src.assemble.model.operand.value import ValueLabel, RValue

class SectionKind(Enum):
    DATA = "data"

@dataclass(frozen=True)
class Section():
    kind: SectionKind
    name: ValueLabel
    value: RValue

    def __repr__(self) -> str:
        return f".{self.kind.value} {self.name} = {self.value}"