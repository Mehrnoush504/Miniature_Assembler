import sys


class RType:
    op = ''
    rs = ''
    rt = ''
    rd = ''
    instructions = {'add': '0000', 'sub': '0001', 'slt': '0010', 'or': '0011', 'nand': '0100'}

    def __init__(self):
        pass

    def calc(self, line, registers):
        line_content = line.split()
        flag = False
        index = -1
        for key in self.instructions.keys():
            if line_content[0] == key:
                op = self.instructions[key]
                flag = True
                index = 1
                break

        if not flag:
            for key in self.instructions.keys():
                if line_content[1] == key:
                    op = self.instructions[key]
                    index = 2
                    break

        fields = line_content[index].split(',')
        found = False
        for key in registers.keys():
            f = int(fields[0])
            if f == key:
                rd = registers[key]
                found = True
                break

        if not found:
            sys.exit('R_type : rd not found')

        found = False
        for key in registers.keys():
            f = int(fields[1])
            if f == key:
                rs = registers[key]
                found = True
                break
        if not found:
            sys.exit('R_type : rs not found')

        found = False
        for key in registers.keys():
            f = int(fields[2])
            if f == key:
                rt = registers[key]
                found = True
                break
        if not found:
            sys.exit('R_type : rt not found')

        return '0000' + op + rs + rt + rd + '000000000000'


