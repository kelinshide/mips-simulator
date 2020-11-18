# 第一个组件
def calc(number):
    return int(number, 2)


# sll指令
def sll(line):
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    theline = "SLL R" + str(rd) + ", R" + str(rt) + ", #" + str(sa)

    next_line = "SLL\tR" + str(rd) + ", R" + str(rt) + ", #" + str(sa)
    return theline, next_line


# srl指令
def srl(line):
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    theline = "SRL R" + str(rd) + ", R" + str(rt) + ", #" + str(sa)

    next_line = "SRL\tR" + str(rd) + ", R" + str(rt) + ", #" + str(sa)
    return theline, next_line


# sra指令
def sra(line):
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    theline = "SRA R" + str(rd) + ", R" + str(rt) + ", #" + str(sa)

    next_line = "SRA\tR" + str(rd) + ", R" + str(rt) + ", #" + str(sa)
    return theline, next_line


# jr指令
def jr(line):
    rs = 4 * calc(line[6:11])
    theline = "JR " + str(rs)

    next_line = "JR\t" + str(rs)
    return theline, next_line


# add指令
def add(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "ADD R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    next_line = "ADD\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, next_line


# 第二类add指令
def add2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "ADD R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "ADD\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# 第二类sub指令
def sub2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "SUB R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "SUB\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# 第二类mul指令
def mul2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "MUL R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "MUL\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# 第二类and指令
def theand2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "AND R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "AND\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# 第二类nor指令
def nor2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "NOR R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "NOR\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# 第二类slt指令
def slt2(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    return "SLT R" + str(rt) + ", R" + str(rs) + ", #" + str(im), "SLT\tR" + str(rt) + ", R" + str(rs) + ", #" + str(im)


# mul指令
def mul(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "MUL R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, "MUL\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)


# and指令
def theand(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "AND R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, "AND\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)


# nor指令
def nor(line):
    theline = ""
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "NOR R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, "NOR\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)


# slt指令
def slt(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "SLT R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, "SLT\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)


# sub指令
def sub(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    theline = "SUB R" + str(rd) + ", R" + str(rs) + ", R" + str(rt)
    return theline, "SUB\tR" + str(rd) + ", R" + str(rs) + ", R" + str(rt)

#break
def thebreak(line):
    return "BREAK", "BREAK"

# j指令
def j(line):
    theline = "J #" + str(4 * calc(line[6:]))
    return theline, "J\t#" + str(4 * calc(line[6:]))

# beq指令
def beq(line):
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    number = 4 * calc(line[16:])
    theline = "BEQ R" + str(rs) + ", R" + str(rt) + ", #" + str(number)
    return theline, "BEQ\tR" + str(rs) + ", R" + str(rt) + ", #" + str(number)


# bltz指令
def bltz(line):
    rs = calc(line[6:11])
    offset = 4 * calc(line[16:])
    theline = "BLTZ R" + str(rs) + ", #" + str(offset)
    return theline, "BLTZ\tR" + str(rs) + ", #" + str(offset)


# bgtz指令
def bgtz(line):
    rs = calc(line[6:11])
    offset = 4 * calc(line[16:])
    theline = "BGTZ R" + str(rs) + ", #" + str(offset)
    return theline, "BGTZ\tR" + str(rs) + ", #" + str(offset)


# sw指令
def sw(line):
    base = calc(line[6:11])
    rt = calc(line[11:16])
    offset = calc(line[16:])
    theline = "SW R" + str(rt) + ", " + str(offset) + "(R" + str(base) + ")"
    return theline, "SW\tR" + str(rt) + ", " + str(offset) + "(R" + str(base) + ")"


# lw指令
def lw(line):
    base = calc(line[6:11])
    rt = calc(line[11:16])
    offset = calc(line[16:])
    theline = "LW R" + str(rt) + ", " + str(offset) + "(R" + str(base) + ")"
    return theline, "LW\tR" + str(rt) + ", " + str(offset) + "(R" + str(base) + ")"
