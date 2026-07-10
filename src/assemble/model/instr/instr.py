from dataclasses import dataclass
from abc import ABC, abstractmethod

from src.assemble.model.operand.value import Operand


@dataclass(frozen=True)
class Instr(ABC):
    @abstractmethod
    def __repr__(self, ident:int=0) -> str:
        raise
    @abstractmethod
    def get_children(self) -> list[Operand]:
        raise