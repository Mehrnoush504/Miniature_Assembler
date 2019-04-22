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

        if linecontent[index-1]=='lui':   
            found =False
            for key in registers.keys():
                if fields[0]==key:
                    rt=registers[key]
                    found=True
                    break
            if found==False:
                sys.exit('I_type:rt not found!')
            for key in symbol_table.keys():
                if fields[1]==key:
                    imm=str(decimal_to_binary(symbol_table[key]))
            if len(imm)>16:
                sys.exit('I_type:imm out of range!')
            zero=''
            for i in range (0,16-len(imm)):
                zero+='0'
            imm=zero+imm
        elif linecontent[index-1]=='jalr':
            found =False
            for key in registers.keys():
                if fields[0]==key:
                   rt=registers[key]
                   found=True
                   break
            if found==False:
                sys.exit('I_type:rt not found!')
            
            found =False
            for key in registers.keys():
                if fields[1]==key:
                   rs=registers[key]
                   found=True
                   break
            if found==False:
                sys.exit('I_type:rs not found!')
            
            for i n range(0,16):
                imm+='0'
        else:
            found =False
            for key in registers.keys():
                if fields[0]==key:
                   rt=registers[key]
                   found=True
                   break
            if found==False:
                sys.exit('I_type:rt not found!')
            
            found =False
            for key in registers.keys():
                if fields[1]==key:
                   rs=registers[key]
                   found=True
                   break
            if found==False:
                sys.exit('I_type:rs not found!')
            
            #az inja be payin chek shavad
            flage=False
            for key in symbol_table.keys():
                if fields[2]==key:
                    imm=str(desimal_to_bainary(symbol_table[key]))
                    if len(imm)>16:
                        sys.exit('I_type:imm out of range!')
                    zero=''
                    for i in range(0,16-len(imm)):
                        zero+='0'
                    imm + = zero
                    flag=True
                
                if flage==False and not isdigit(fields[2]):
                    sys.exit('I_type: incorect imm')
                
                elif isdigit(fields[2]):
                    num=int (fields[2])
                    imm=str(decimal_to_binary(num))
                    if len(imm)>16:
                        sys.exit('I_type:imm out of range!')
                    zero=''
                    for i in range(0,16-len(imm)):
                        zero+='0'
                    imm + = zero
                
            if linecontent[index-1] == 'beq':
                    lable=-1
                    lable=int(imm)
                    if lable-pc-1>= 0:
                        imm=str(lable-pc-1)
                
            else:
                imm=two_comp(lable-pc-1)

        return '0000' + op + rs + rt + imm
