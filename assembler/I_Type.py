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
<<<<<<< HEAD
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
        return
=======
        for key in instructions.keys():
            
        return
>>>>>>> 93df6d6d45befffc26a263107e45b1dc19399855
