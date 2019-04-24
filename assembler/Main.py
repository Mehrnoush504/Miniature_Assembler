import  sys

# function for turning decimal into binary

def decimal_to_binary(num):
    s = bin(num)
    s = s[2:]
    print(s)
    return s

def calcJtype(line, symbol_table,instructions):

    op = ''
    target = ''

    linecontent=line.splite()
    flag=False
    index=-1
    for key in instructions.keys():
        if linecontent[0]==key:
            op=instructions[key]
            index=1
            flag=True
            break
        if not flag:
            for key in instructions.keys():
                if linecontent[1]==key:
                    op=instructions[key]
                    index=2
                    break
    if op=='j':
        for key in symbol_table.keys():
            if linecontent[index]==key:
                target+=str(desimal_to_inary(symbol_table[key]))
                if len(target)>16:
                    sys.exit('target out of range')
                zero=''
                for i in range(0,16-len(target)):
                    zero+='0'
                target=zero+ target
                break
    elif op=='halt':
        target='0000000000000000'

    return'0000'+op+'00000000'+target







def calcRtype(line, registers,instructions):

    op = ''
    rs = ''
    rt = ''
    rd = ''

    linecontent = line.split()
    flag = False
    index = -1
    for key in instructions.keys():
        if linecontent[0] == key:
            op = instructions[key]
            flag = True
            index = 1
            break
    if not flag:
        for key in instructions.keys():
            if linecontent[1] == key:
                op = instructions[key]
                flag = True
                index = 2
                break
    fields = linecontent[index].split(',')
    found = False
    for key in registers.keys():
        if fields[0] == key:
            rd = registers[key]
            found = True
            break
    if not found:
        sys.exit('R_type : rd not found')

    found = False
    for key in registers.keys():
        if fields[1] == key:
            rs = registers[key]
            found = True
            break
    if not found:
        sys.exit('R_type : rs not found')

    found = False
    for key in registers.keys():
        if fields[2] == key:
            rt = registers[key]
            found = True
            break
    if not found:
        sys.exit('R_type : rt not found')

    return '0000' + op + rs + rt + rd + '000000000000'








def calcItype(line, pc, symbol_table,registers,instructions):

    op = ''
    rs = ''
    rt = ''
    imm = ''
    linecontent = line.split()
    flag = False
    index = -1
    for key in instructions.keys():
        if linecontent[0] == key:
            op = instructions[key]
            index = 1
            flag = True
            break
    if flag == False:
        for key in instructions.keys():
            if linecontent[1] == key:
                op = instructions[key]
                index = 2
                break

    fields = linecontent[index].split(',')

    if linecontent[index - 1] == 'lui':
        found = False
        for key in registers.keys():
            if fields[0] == key:
                rt = registers[key]
                found = True
                break
        if found == False:
            sys.exit('I_type:rt not found!')
        for key in symbol_table.keys():
            if fields[1] == key:
                imm = str(decimal_to_binary(symbol_table[key]))
        if len(imm) > 16:
            sys.exit('I_type:imm out of range!')
        zero = ''
        for i in range(0, 16 - len(imm)):
            zero += '0'
        imm = zero + imm
    elif linecontent[index - 1] == 'jalr':
        found = False
        for key in registers.keys():
            if fields[0] == key:
                rt = registers[key]
                found = True
                break
        if found == False:
            sys.exit('I_type:rt not found!')

        found = False
        for key in registers.keys():
            if fields[1] == key:
                rs = registers[key]
                found = True
                break
        if found == False:
            sys.exit('I_type:rs not found!')

        for i in range(0, 16):
            imm += '0'
    else:
        found = False
        for key in registers.keys():
            if fields[0] == key:
                rt = registers[key]
                found = True
                break
        if found == False:
            sys.exit('I_type:rt not found!')

        found = False
        for key in registers.keys():
            if fields[1] == key:
                rs = registers[key]
                found = True
                break
        if found == False:
            sys.exit('I_type:rs not found!')

        # az inja be payin chek shavad
        flage = False
        for key in symbol_table.keys():
            if fields[2] == key:
                imm = str(desimal_to_bainary(symbol_table[key]))
                if len(imm) > 16:
                    sys.exit('I_type:imm out of range!')
                zero = ''
                for i in range(0, 16 - len(imm)):
                    zero += '0'
                imm += zero
                flag = True

            if flage == False and not isdigit(fields[2]):
                sys.exit('I_type: incorect imm')

            elif isdigit(fields[2]):
                num = int(fields[2])
                imm = str(decimal_to_binary(num))
                if len(imm) > 16:
                    sys.exit('I_type:imm out of range!')
                zero = ''
                for i in range(0, 16 - len(imm)):
                    zero += '0'
                imm += zero

        if linecontent[index - 1] == 'beq':
            lable = -1
            lable = int(imm)
            if lable - pc - 1 >= 0:
                imm = str(lable - pc - 1)

        else:
            imm = two_comp(lable - pc - 1)

    return '0000' + op + rs + rt + imm


# main function
def main():
    file=open('C:/Users/ErfanN/PycharmProjects/untitled1/venv/program.ac.txt','r')
    register=dict()
    register={'0':'0','1':'1',}
    R_instructions = dict()
    R_instructions = {'add': '0000', 'sub': '0001', 'slt': '0010', 'or': '0011', 'nand': '0100'}
    I_instructions = dict()
    I_instructions = {'addi': '0101', 'ori': '0111', 'slti': '0110', 'lui': '1000', 'lw': '1001', 'sw': '1010',
                      'beq': '1011', 'jalr': '1100'}
    J_instructions = dict()
    J_instructions = {'j': '1101', 'halt': '1110'}

    i=0
    type=''
    symbol_table = list()
    for line in file:
          ch = line.split()
          if not( line.startswith(' ') or line.startswith('\t')):
               symbol_table.append(str(i)+' '+ch[0])
               for item in R_instructions:
                   if item==ch[1]:
                       type='r'
                       break
               for item in J_instructions:
                   if item==ch[1]:
                       type='j'
                       break
               for item in I_instructions:
                   if item==ch[1]:
                       type='i'
                       break
          else :
              for item in R_instructions:
                  if item == ch[0]:
                      type = 'r'
                      break
              for item in J_instructions:
                  if item == ch[0]:
                      type = 'j'

                      break
              for item in I_instructions:
                  if item == ch[0]:
                      type = 'i'

                      break
          i+=1
          if type=='r':
              calcRtype(line,register,R_instructions)
          elif type=='j':
              calcJtype(line,symbol_table,J_instructions)
          elif type=='i':
              calcItype(line,i,symbol_table,register,I_instructions)

    file.close()
    sys.exit(0)


if __name__ == '__main__':
      main()



