from dataclasses import dataclass

from assemble.model.operand.symbol import Symbol
from assemble.model.operand.address import AddressInfo

@dataclass
class Context():
    sym: dict[Symbol, AddressInfo]