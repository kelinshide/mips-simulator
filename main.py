
from disa import *
from simu import *

def calc(number):
    return int(number, 2)

#计算负数补码
def replace_char(string, char, index):
    string = list(string)
    string[index] = char
    return ''.join(string)

#任务一插入空格
def insert_char(string, lis, char):
    string = list(string)
    for i in range(0, 5):
        string.insert(lis[i], char)
    return ''.join(string)
#读入文件
path = str(os.getcwd())
readin = path + "/sample.txt"
f = open(readin, "r")
lines = f.readlines()

#任务一输出文件
write_path = path + "/disassembly.txt"
writein = open(write_path, 'w')


address = 60
code = True

thenumber_address = []          #记录地址中的数据
thesign_break = False           #记录是否break
theaddress_break = 60           #记录break地址


length = len(lines)

# 计算地址中的数据
for ii in range(length):
    line = lines[ii]
    line = line.replace('\n', '').replace(' ', '').replace('\t', '')
    if not thesign_break:
        theaddress_break += 4

    if thesign_break:
        if line[0] == '1':
            for i in range(1, 32):
                if line[i] == '1':
                    line = replace_char(line, '0', i)
                else:
                    line = replace_char(line, '1', i)
            number = -calc(line[1:]) - 1
        else:
            number = calc(line[1:])
        thenumber_address.append(number)  #将地址中的数据记录到thenumber_address中

    if line[0:6] == "000000" and line[-6:] == "001101":
        thesign_break = True



simu_line=[] #记录任务二的指令格式


#任务一
for line in lines:
    sign_break = False #标记break
    line = line.replace('\n', '').replace(' ', '').replace('\t', '')
    theline = line
    address += 4
    thestring = ""
    if code:
        #判断是否是nop指令
        sign_nop = True
        for ll in line:
            if ll == "1":
                sign_nop = False
                break
        if sign_nop:
            thestring="NOP"
            simu_line.append(thestring)

        #判断是什么指令
        elif line[0] == '0':
            if line[0:6] == '000000':
                if line[-11:] == "00000100000":
                    thestring,nextline = add(line)#add
                    simu_line.append(nextline)
                elif line[-11:] == "00000100010":
                    thestring,nextline = sub(line)#sub
                    simu_line.append(nextline)
                elif line[-11:] == "00000100100":
                    thestring,nextline = theand(line)#and
                    simu_line.append(nextline)
                elif line[-11:] == "00000100111":
                    thestring,nextline = nor(line)#nor
                    simu_line.append(nextline)

                elif line[-11:] == "00000101010":
                    thestring,nextline = slt(line)#slt
                    simu_line.append(nextline)

                elif line[-6:] == "001101":
                    thestring,nextline = thebreak(line)#break
                    simu_line.append(nextline)
                    code = False
                    sign_break = True

                elif line[-6:] == "001000" and line[11:21] == "0000000000":
                    thestring,nextline = jr(line) #jr
                    simu_line.append(nextline)
                elif line[6:11] == "00000":
                    if line[-6:] == '000000':
                        thestring,nextline = sll(line)#sll
                        simu_line.append(nextline)
                    elif line[-6:] == "000010":
                        thestring,nextline = srl(line)#srl
                        simu_line.append(nextline)
                    elif line[-6:] == '000011':
                        thestring,nextline = sra(line)#sra
                        simu_line.append(nextline)
            else:
                if line[0:6] == "000010":
                    thestring,nextline = j(line)#j
                    simu_line.append(nextline)
                elif line[0:6] == "000100":
                    thestring,nextline = beq(line)#beq
                    simu_line.append(nextline)

                elif line[0:6] == "011100" and line[-11:] == "00000000010":
                    thestring,nextline = mul(line)#mul
                    simu_line.append(nextline)

                elif line[11:16] == "00000":
                    if line[0:6] == "000001":
                        thestring,nextline = bltz(line)#bltz
                        simu_line.append(nextline)
                    elif line[0:6] == "000111":
                        thestring,nextline = bgtz(line)#bgtz
                        simu_line.append(nextline)

                # else:
                #     if line[1:6] == "10000":
                #         thestring = add(line)
                #     elif line[1:6] == "10001":
                #         thestring = sub(line)
                #     elif line[1:6] == "00001":
                #         thestring = mul(line)
                #     elif line[1:6] == "10010" or line[1:6]=="11100":
                #         thestring = theand(line)
                #     elif line[1:6] == "10011":
                #         thestring = nor(line)
                #     elif line[1:6] == "10101":
                #         thestring = slt(line)
        else:
            if line[0:6] == "101011":
                thestring,nextline = sw(line)#sw
                simu_line.append(nextline)
            elif line[0:6] == "100011":
                thestring,nextline = lw(line)#lw
                simu_line.append(nextline)
            else:
                if line[1:6] == "10000":
                    thestring,nextline = add2(line)#第二类add
                    simu_line.append(nextline)
                elif line[1:6] == "10001":
                    thestring,nextline = sub2(line)#第二类sub
                    simu_line.append(nextline)
                elif line[1:6] == "00001":
                    thestring,nextline= mul2(line)#第二类mul
                    simu_line.append(nextline)
                elif line[1:6] == "10010":
                    thestring,nextline = theand2(line)#第二类and
                    simu_line.append(nextline)
                elif line[1:6] == "10011":
                    thestring,nextline = nor2(line)#第二类nor
                    simu_line.append(nextline)
                elif line[1:6] == "10101":
                    thestring,nextline = slt2(line)#slt
                    simu_line.append(nextline)
    else:

        #计算地址中的数据
        if line[0] == '1':
            for i in range(1, 32):
                if line[i] == '1':
                    line = replace_char(line, '0', i)
                else:
                    line = replace_char(line, '1', i)
            number = -calc(line[1:]) - 1
        else:
            number = calc(line[1:])
        thestring = str(number)

    if code or sign_break:
        lis = [6, 12, 18, 24, 30]
        line = insert_char(line, lis, ' ') #插入空格
        thestring = line + '\t' + str(address) + '\t' + thestring
    else:
        thestring = theline + "\t" + str(address) + '\t' + thestring
    thestring += "\n"
    writein.write(thestring)#写入文件
    print(thestring,end="")



#任务二
simu(thenumber_address,theaddress_break+4 ,simu_line)















