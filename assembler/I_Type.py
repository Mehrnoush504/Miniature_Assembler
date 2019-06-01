import sys
import decimal_and_binary_converter as db
import two_complement as towComp


class IType:
    instructions = {'addi': '0101', 'ori': '0111', 'slti': '0110', 'lui': '1000', 'lw': '1001', 'sw': '1010',
                    'beq': '1011', 'jalr': '1100'}
    op = ''
    rs = ''
    rt = ''
    imm = ''

    def __init__(self):
        pass

    def calc(self, line, pc, symbol_table, registers):
        print('i type ', line)
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

        fields = line_content[index].split(',')

        print(fields)
        if line_content[index - 1] == 'lui':
            found = False
            for key in registers.keys():
                f = int(fields[0])
                if f == key:
                    self.rt = registers[key]
                    found = True
                    break

            if not found:
                sys.exit('I_type:rt not found!')

            for key in symbol_table.keys():
                if fields[1] == key:
                    self.imm = str(db.decimal_to_binary(symbol_table[key]))
            if len(self.imm) > 16:
                sys.exit('I_type:imm out of range!')
            zero = ''
            for i in range(0, 16 - len(self.imm)):
                zero += '0'
            self.imm = zero + self.imm

        elif line_content[index - 1] == 'jalr':
            found = False
            for key in registers.keys():
                f = int(fields[0])
                if f == key:
                    self.rt = registers[key]
                    found = True
                    break

            if not found:
                sys.exit('I_type:rt not found!')

            found = False
            for key in registers.keys():
                f = int(fields[1])
                if f == key:
                    self.rs = registers[key]
                    found = True
                    break

            if not found:
                sys.exit('I_type:rs not found!')

            for i in range(0, 16):
                self.imm += '0'
        else:
            found = False
            for key in registers.keys():
                f = int(fields[0])
                if f == key:
                    self.rt = registers[key]
                    found = True
                    break

            if not found:
                sys.exit('I_type:rt not found!')

            found = False
            for key in registers.keys():
                f = int(fields[1])
                if f == key:
                    self.rs = registers[key]
                    found = True
                    break

            if not found:
                sys.exit('I_type:rs not found!')

            # az inja be payin chek shavad
            not_in_symbols = True
            for key in symbol_table.keys():
                print(key)
                if fields[2] == key:
                    self.imm = str(db.decimal_to_binary(symbol_table[key]))
                    if len(self.imm) > 16:
                        sys.exit('I_type:imm out of range!')
                    zero = ''
                    for i in range(0, 16 - len(self.imm)):
                        zero += '0'
                    self.imm = zero + self.imm
                    print('after symbol', self.imm)
                    not_in_symbols = False

            not_in_numbers = True
            f = fields[2].lstrip('-')
            if f.isdigit():
                #
                not_in_numbers = False
                if fields[2].startswith('-'):
                    self.imm += towComp.tow_comp(int(fields[2]))
                    if len(self.imm) > 16:
                        sys.exit('imm out of range')
                    zero = ''
                    for i in range(0, 16 - len(self.imm)):
                        zero += '0'
                    self.imm = zero + self.imm
                    not_in_numbers = False
                elif fields[2].isdigit():  # find digit target
                    self.imm += str(db.decimal_to_binary(int(fields[2])))
                    if len(self.imm) > 16:
                        sys.exit('imm out of range')
                    zero = ''
                    for i in range(0, 16 - len(self.imm)):
                        zero += '0'
                    self.imm = zero + self.imm
                    not_in_numbers = False
                #
            #   if line_content[index-1]=='slti':
            #      if self.rs<self.imm:
            #        self.rt='0001'
            #      else:
            #        self.rt='0000'
            in_beq = False
            if line_content[index - 1] == 'beq':
                label = db.binary_to_decimal(self.imm)
                if label - pc - 1 >= 0:
                    self.imm = str(db.decimal_to_binary(label - pc - 1))
                    if len(self.imm) > 16:
                        sys.exit('i type: in beq imm out of bound')
                    zero = ''
                    for i in range(0, 16 - len(self.imm)):
                        zero += '0'
                    self.imm = zero + self.imm
                    in_beq = True
                else:
                    self.imm = towComp.tow_comp(label - pc - 1)
                    in_beq = True

            if not in_beq:
                if not_in_symbols and not_in_numbers:
                    sys.exit('I_type: imm not found!')
        return '0000' + self.op + self.rs + self.rt + self.imm
