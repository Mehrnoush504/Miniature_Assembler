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
        for key in instructions.keys():
            
        return
