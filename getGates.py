AND = lambda a,b : a * b
XOR = lambda a,b : abs(a - b)
NOT = lambda a : XOR(a,1)
NAND = lambda a,b : NOT(AND(a,b))
XNOR = lambda a,b : NOT(XOR(a,b))
NOR = lambda a,b : AND(NOT(a), NOT(b))
OR = lambda a,b : NOT(NOR(a,b))

truth = {
    "0000" : lambda a,b : 0,
    "0001" : AND,
    "0010" : lambda a,b : AND(a, NOT(b)),
    "0011" : lambda a,b : a,
    "0100" : lambda a,b : NOR(a, NOT(b)),
    "0101" : lambda a,b : b,
    "0110" : XOR,
    "0111" : OR,
    "1000" : NOR,
    "1001" : XNOR,
    "1010" : lambda a,b : NOT(b),
    "1011" : lambda a,b : OR(a, NOT(b)),
    "1100" : lambda a,b : NOT(a),
    "1101" : lambda a,b : NAND(a, NOT(b)),
    "1110" : NAND,
    "1111" : lambda a,b : 1,
    "00" : lambda a : 0,
    "01" : lambda a : a,
    "10" : NOT,
    "11" : lambda a : 1
}

def _combine(lambdaA, lambdaB):
    x = lambda *arg : AND(NOT(arg[0]), lambdaA(*arg[1:]))
    y = lambda *arg : AND(arg[0], lambdaB(*arg[1:]))
    return lambda *arg : OR(x(*arg), y(*arg))

def get(table: str):
    if len(table) == 4:
        return truth[table]
    elif len(table) == 2:
        return truth[table]
    else:
        l = len(table) // 2
        x = get(table[:l])
        y = get(table[l:])
        return _combine(x,y)
