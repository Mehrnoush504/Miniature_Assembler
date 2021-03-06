import sys
import decimal_and_binary_converter as db
import two_complement as towComp

class JType:
    op = ''
    target = ''
    instructions = {'j': '1101', 'halt': '1110',}

    def __init__(self):
        pass

    def calc(self, line, symbol_table):
        line_content = line.split()
        flag = False
        index = -1
        for key in self.instructions.keys():
            if line_content[0] == key:
                self.op = self.instructions[key]
                index = 1
                flag = True
                break

        if not flag:
            for key in self.instructions.keys():
                if line_content[1] == key:
                    self.op = self.instructions[key]
                    index = 2
                    break

        if self.op == '1101':  # j
            flag=False
            if line_content[index].startswith('-'):
                self.target += towComp.tow_comp(int(line_content[index]))
                if len(self.target) > 16:
                    sys.exit('target out of range')
                zero = ''
                for i in range(0, 16 - len(self.target)):
                    zero += '0'
                self.target = zero + self.target
                flag = True
            elif line_content[index].isdigit():  #find digit target
                self.target += str(db.decimal_to_binary(int(line_content[index])))
                if len(self.target) > 16:
                    sys.exit('target out of range')
                zero = ''
                for i in range(0, 16 - len(self.target)):
                    zero += '0'
                self.target = zero + self.target
                flag = True
            else:
                for key in symbol_table.keys():
                    if line_content[index] == key:
                        self.target += str(db.decimal_to_binary(symbol_table[key]))
                        if len(self.target) > 16:
                            sys.exit('target out of range')
                        zero = ''
                        for i in range(0, 16 - len(self.target)):
                            zero += '0'
                        self.target = zero + self.target
                        flag = True
                        break
            if not flag:
                sys.exit('lable is not definded')
        elif self.op == '1110':  # halt
            self.target = '0000000000000000'

        return '0000' + self.op + '00000000' + self.target
