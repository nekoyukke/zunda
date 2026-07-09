MOV dst, src

ADD dst, src1, src2\
SUB dst, src1, src2\
MUL dst, src1, src2\
DIV dst, src1, src2\
MOD dst, src1, src2\
NEG dst, src\
ABS dst, src

AND dst, src, src\
OR  dst, src, src\
XOR dst, src, src\
NOT dst, src

SHL dst, src, src\
SHR dst, src, src\
SAR dst, src, src

ROL dst, src, src\
ROR dst, src, src

BR_EQ a,b,label\
BR_NE a,b,label\
BR_LT a,b,label\
BR_LE a,b,label\
BR_GT a,b,label\
BR_GE a,b,label

CALL symbol\
RET

NOP\
HALT

~~ADC dst,src~~\
~~SBC dst,src~~

~~BSET dst,bit~~\
~~BCLR dst,bit~~\
~~BTST dst,bit~~

---

# Operand

## CodeLabel

## Value

### Register

### Immediate

### Memory

### ValueLabel