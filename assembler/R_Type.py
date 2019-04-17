import sys


class RType:
    instructions = dict()
    op = ''
    rs = ''
    rt = ''
    rd = ''
    instructions = {'add': '0000', 'sub': '0001', 'slt': '0010', 'or': '0011', 'nand': '0100'}

    def __init__(self):
        pass

    def calc(self, line, registers):
        linecontent = line.split()
        flag = False
        index = -1
        for key in self.instructions.keys():
            if linecontent[0] == key:
                op = self.instructions[key]
                flag = True
                index = 1
                break
        if not flag:
            for key in self.instructions.keys():
                if linecontent[1] == key:
                    op = self.instructions[key]
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
