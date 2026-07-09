from dataclasses import dataclass
from enum import Enum

class SymbolKind(Enum):
    CODE = 0
    DATA = 1

@dataclass
class Symbol():
    id: int
    name: str
    kind: SymbolKind