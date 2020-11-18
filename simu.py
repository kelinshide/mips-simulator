import os


def calc(number):
    return int(number, 2)


def glo():
    global r
    global thenumber_address


def simu(thenumber_address, theaddress_break, simu_line):
    thenumber_address = thenumber_address  # 地址中的数据
    theaddress_break = theaddress_break  # break的地址
    r = [0] * 32  # 32个寄存器
    simu_line = simu_line  # 任务二输出指令
    glo()

    # 读文件
    path = str(os.getcwd())
    readin = path + "/sample.txt"
    f = open(readin, "r")
    lines = f.readlines()

    # 写入文件的地址
    simulation_path = path + "/simulation.txt"
    simulation_writein = open(simulation_path, 'w')  # 模拟路径

    now_line = 0  # 记录当前运行指令

    cycle = 1
    while now_line <= (theaddress_break - 64) / 4:

        thesign_jump = False  # 判断是否跳转
        theline_jump = now_line  # 记录跳转的指令行数

        simu_sign_break = False  # 防止break不写入
        thestring = "--------------------\n"  # 写入文件的字符串

        line = lines[now_line]
        line = line.replace('\n', '').replace(' ', '').replace('\t', '')




        sign_nop = True
        for ll in line:
            if ll == "1":
                sign_nop = False
                break
        if sign_nop:
            pass





        elif line[0] == '0':
            if line[0:6] == '000000':
                if line[-11:] == "00000100000":
                    r = sim_add(line, r)  # add

                elif line[-11:] == "00000100010":
                    r = sim_sub(line, r)  # sub

                elif line[-11:] == "00000100100":
                    r = sim_theand(line, r)  # and

                elif line[-11:] == "00000100111":
                    r = sim_nor(line, r)  # nor

                elif line[-11:] == "00000101010":
                    r = sim_slt(line, r)  # slt


                elif line[-6:] == "001101":
                    simu_sign_break = True  # break

                elif line[-6:] == "001000" and line[11:21] == "0000000000":
                    now_line = int((sim_jr(line) - 64) / 4)-1  # jr
                    thesign_jump=True

                elif line[6:11] == "00000":
                    if line[-6:] == '000000':
                        r = sim_sll(line, r)  # sll

                    elif line[-6:] == "000010":
                        r = sim_srl(line, r)  # srl

                    elif line[-6:] == '000011':
                        r = sim_sra(line, r)  # sra

            else:

                if line[0:6] == "000010":
                    now_line = int((sim_j(line) - 64) / 4) - 1  # j
                    thesign_jump = True  # 标记跳转

                elif line[0:6] == "000100":
                    thesign_beq, thenumber_beq = sim_beq(line, r)  # beq
                    if thesign_beq:
                        now_line = now_line + thenumber_beq
                        thesign_jump = True  # 标记跳转

                elif line[0:6] == "011100" and line[-11:] == "00000000010":
                    r = sim_mul(line, r)  # mul

                elif line[11:16] == "00000":
                    if line[0:6] == "000001":
                        thesign_bltz, thenumber_bltz = sim_bltz(line, r)  # bltz
                        if thesign_bltz:
                            thesign_jump = True  # 标记跳转
                            now_line = now_line + int(thenumber_bltz / 4)

                    elif line[0:6] == "000111":
                        thesign_bgtz, thenumber_bgtz = sim_bgtz(line, r)  # bgtz
                        if thesign_bgtz:
                            thesign_jump = True  # 标记跳转
                            now_line = now_line + int(thenumber_bgtz / 4)
        else:
            if line[0:6] == "101011":
                thenumber_address = sim_sw(line, r, thenumber_address, theaddress_break)  # sw

            elif line[0:6] == "100011":
                r = sim_lw(line, r, thenumber_address, theaddress_break)  # lw

            else:
                if line[1:6] == "10000":
                    r = sim_add2(line, r)  # add2

                elif line[1:6] == "10001":
                    r = sim_sub2(line, r)  # sub2

                elif line[1:6] == "00001":
                    r = sim_mul2(line, r)  # mul2

                elif line[1:6] == "10010":
                    r = sim_theand2(line, r)  # and2

                elif line[1:6] == "10011":
                    r = sim_nor2(line, r)  # nor2

                elif line[1:6] == "10101":
                    r = sim_slt2(line, r)  # slt2

        if thesign_jump == False:
            thestring += ("Cycle:" + str(cycle) + "\t" + str(now_line * 4 + 64) + "\t" + simu_line[
                now_line] + "\n\nRegisters\nR00:") #不跳转时
        else:
            thestring += ("Cycle:" + str(cycle) + "\t" + str(theline_jump * 4 + 64) + "\t" + simu_line[
                theline_jump] + "\n\nRegisters\nR00:") #跳转时

        # 输出寄存器的值
        for i in range(0, 16):
            print(r[i], " ", end="")
            thestring += ("\t" + str(r[i]))
            if i == 15:
                thestring += "\n"
                print()

        thestring += "R16:"
        for i in range(16, 32):
            thestring += ("\t" + str(r[i]))
            print(r[i], " ", end="")
            if i == 31:
                thestring += "\n"
                print()

        thestring += "\nData"
        print()

        #输出地址中的值
        count = 0
        for i in range(len(thenumber_address)):
            if i == 0 or i % 8 == 0:
                thestring += ("\n" + str(theaddress_break + count * 32) + ":\t")
                count += 1
            thestring += (str(thenumber_address[i]) + "\t")

            if i % 8 == 0:
                print()
            print(thenumber_address[i], "\t", end="")

        thestring += "\n\n"

        #写入文件
        simulation_writein.write(thestring)
        cycle += 1
        now_line += 1

        #break时退出循环
        if simu_sign_break:
            break


def sim_lw(line, r, thenumber_address, theaddress_break):
    print("sim_lw", end="")
    base = calc(line[6:11])
    rt = calc(line[11:16])
    offset = calc(line[16:])
    offset = offset + r[base]
    r[rt] = thenumber_address[int((offset - theaddress_break) / 4)]
    print(int((offset - theaddress_break) / 4))
    return r


def sim_sw(line, r, thenumber_address, theaddress_break):
    print("sim_sw")
    base = calc(line[6:11])
    rt = calc(line[11:16])
    offset = calc(line[16:])

    thenumber_address[int((r[base] + offset - theaddress_break) / 4)] = r[rt]
    print(int((r[base] + offset - theaddress_break) / 4) - 1)
    return thenumber_address


def sim_slt2(line, r):
    print("sim_slt2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    if r[rs] < im:
        r[rt] = 1
    else:
        r[rt] = 0
    return r


def sim_nor2(line, r):
    print("sim_nor2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    r[rt] = r[rs] | im
    return r


def sim_theand2(line, r):
    print("sim_theand2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    r[rt] = r[rs] & im
    return r


def sim_mul2(line, r):
    print("sim_mul2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    r[rt] = r[rs] * im
    return r


def sim_sub2(line, r):
    print("sim_sub2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    r[rt] = r[rs] - im
    return r


def sim_add2(line, r):
    print("sim_add2")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    im = calc(line[16:])
    r[rt] = r[rs] + im
    return r


def sim_bgtz(line, r):
    print("sim_bgtz")
    rs = calc(line[6:11])
    offset = 4 * calc(line[16:])

    if r[rs] > 0:

        return True, offset
    else:

        return False, offset


def sim_bltz(line, r):
    print("sim_bltz")
    rs = calc(line[6:11])
    offset = 4 * calc(line[16:])
    if r[rs] < 0:
        return True, offset
    else:
        return False, offset


def sim_mul(line, r):
    print("sim_mul")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    r[rd] = r[rs] * r[rt]
    return r


def sim_beq(line, r):
    print("sim_beq")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    number = 4 * calc(line[16:])
    if r[rs] == r[rt]:
        return True, int(number / 4)
    else:
        return False, int(number / 4)


def sim_sra(line, r):
    print("sim_sra")
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    r[rd] = r[rt] >> r[sa]
    return r


def sim_srl(line, r):
    print("sim_srl")
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    r[rd] = r[rt] >> r[sa]
    return r


def sim_j(line):

    theaddress = calc(line[6:]) * 4
    return theaddress


def sim_sll(line, r):
    print("sim_sll")
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    sa = calc(line[21:26])
    mask = (2 ** 32) - 1

    r[rd] = (r[rt] << sa) & mask
    return r


def sim_add(line, r):
    print("sim_add")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    r[rd] = r[rs] + r[rt]
    return r


def sim_sub(line, r):
    print("sim_sub")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    r[rd] = r[rs] - r[rt]
    return r


def sim_theand(line, r):
    print("sim_theand")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    r[rd] = r[rs] & r[rt]
    return r


def sim_nor(line, r):
    print("sim_nor")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    r[rd] = r[rs] | r[rt]
    return r


def sim_slt(line, r):
    print("sim_slt")
    rs = calc(line[6:11])
    rt = calc(line[11:16])
    rd = calc(line[16:21])
    if r[rs] < r[rt]:
        r[rd] = 1
    else:
        r[rd] = 0
    return r

def sim_jr(line):
    print("sim_jr")
    jr_address = calc(line[6:11]) * 4
    return jr_address
