from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass(frozen=True)
class Operand(ABC):
    pass

# Values

@dataclass(frozen=True)
class Value(Operand, ABC):
    pass

@dataclass(frozen=True)
class LValue(Value, ABC):
    pass

@dataclass(frozen=True)
class RValue(Value, ABC):
    pass

@dataclass(frozen=True)
class Register(LValue):
    name:str
    def __repr__(self) -> str:
        return f"%{self.name}"

@dataclass(frozen=True)
class ValueLabel(RValue):
    name:str
    def __repr__(self) -> str:
        return f"${self.name}"

# immediate

@dataclass(frozen=True)
class Immediate(RValue, ABC):
    @abstractmethod
    def get_value(self) -> int|str:
        raise
    @abstractmethod
    def __repr__(self) -> str:
        return f"#{self.get_value()}"

@dataclass(frozen=True)
class Immediate_String(Immediate):
    string:str
    def get_value(self):
        return self.string
    def __repr__(self) -> str:
        return f"#{self.get_value()}"

@dataclass(frozen=True)
class Immediate_Int(Immediate):
    value:int
    def get_value(self):
        return self.value
    def __repr__(self) -> str:
        return f"#{self.get_value()}"

# memorys

@dataclass(frozen=True)
class Memory(LValue):
    reg:Register
    def __repr__(self) -> str:
        return f"[{self.reg.__repr__()}]"

# codelabel

@dataclass(frozen=True)
class CodeLabel(Operand):
    name:str
    def __repr__(self) -> str:
        return f"{self.name}"

# functionlabel

@dataclass(frozen=True)
class FunctionLabel(Operand):
    name:str
    def __repr__(self) -> str:
        return f"@{self.name}"
