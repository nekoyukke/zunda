from dataclasses import dataclass

@dataclass(frozen=True)
class Operand():
    pass

# Values

@dataclass(frozen=True)
class Value(Operand):
    pass

@dataclass(frozen=True)
class LValue(Value):
    pass

@dataclass(frozen=True)
class RValue(Value):
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
class Immediate(RValue):
    def get_value(self) -> int|str:
        raise
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
class CodeLabel:
    name:str
    def __repr__(self) -> str:
        return f"{self.name}"

# functionlabel

@dataclass(frozen=True)
class FunctionLabel:
    name:str
    def __repr__(self) -> str:
        return f"@{self.name}"
