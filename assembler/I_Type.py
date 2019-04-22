class IType:
    instructions = dict()
    instructions ={'addi':'0101' , 'ori':'0111' , 'slti':'0110' , 'lui':'1000' , 'lw':'1001' , 'sw':'1010' , 'beq':'1011' , 'jalr':'1100'}
    op = ''
    rs = ''
    rt = ''
    imm = ''

    def __init__(self):
        pass

    def calc(self, line, pc, symbol_table):
        linecontent=line.split()
        flag=False
        index=-1
        print linecontent
        for key in self.instructions.keys():
            if linecontent[0]==key:
                op=self.instructions[key]
                index=1
                flag=True
                break
        if flag==False:
            for key in self.instructions.keys():
                if linecontent[1]==key:
                    op=self.instructions[key]
                    index=2
                    break
        fields=linecontent[index].split(',')
        if linecontent[index-1]=='lui'     #neveshte shavadddd
             found =False
             for key in registers.keys():
                 if fields[0]==key:
                   rt=registers[key]
                   found=True
                   break
             if found==False:
                 sys.exit('rt not found!')
        for key in symbol_table.keys():
            if fields[1]==key:
                imm=str(decimal_to_binary(symbol_table[key]))
        if len(imm)>16:
            sys.exit('imm out of range!')
        zero=''
        for i in range (0,16-len(imm)):
            zero+='0'
        imm=zero+imm


        return