import os
import sys
import decimal_and_binary_converter as db
from R_Type import RType
from I_Type import IType
from J_Type import JType


# function for creating instruction table
def instruction_table():
    instructions = {"add": "0000", "sub": "0001", "slt": "0010", "or": "0011", "nand": "0100", "addi": "0101",
                    "slti": "0110", "ori": "0111", "lui": "1000", "lw": "1001", "sw": "1010", "beq": "1011",
                    "jalr": "1100", "j": "1101", "halt": "1110"}  # what about "1111" ?
    return instructions


# function for creating register table
def register_table():
    registers = {0: "0000", 1: "0001", 2: "0010", 3: "0011", 4: "0100", 5: "0101", 6: "0110", 7: "0111", 8: "1000",
                 9: "1001", 10: "1010", 11: "1011", 12: "1100", 13: "1101", 14: "1110", 15: "1111"}
    return registers


# function for reading reading information from command line
def read_form_cmd():
    input1 = input()
    list1 = input1.split()
    return list1


# function for reading information from given file
def read_from_file(assembly_file_name):
    content = open(assembly_file_name, 'r')
    # content.close() # remember to close the file at the end of your work
    return content


# function for writing information to given file
def write_to_file(file_name, machine_codes):

    output_file = open(file_name, 'w')

    for item in machine_codes:
        code = str(item) + '\n'
        output_file.write(code)  # this is just an example it needs more work on it
    output_file.close()

    return


# function for checking multiple definition of one label
def multiple_definition_of_one_label(symbol_table, label):
    for key in symbol_table.keys():
        if key == label:
            return True
    return False


# function for making symbol table
def create_symbol_table(file_list, instructions):
    symbol_table = dict()
    line = -1
    for item in file_list:
        line += 1
        line_content = item.split()
        if len(line_content) == 0:
            continue
        flag = False
        for key in instructions.keys():  # I have to correct this
            if key == line_content[0].lower():
                if multiple_definition_of_one_label(symbol_table, line_content[0]):
                    sys.exit(1)
                if len(line_content) >= 2:
                    for k in instructions.keys():
                        if k == line_content[1]:
                            sys.exit(1)
                flag = True

        if flag:
            continue
        if multiple_definition_of_one_label(symbol_table, line_content[0]):
            sys.exit('repeated label')
        symbol_table.update({line_content[0]: line})

    return symbol_table


def process():
    machine_codes = list()
    incoming_list = read_form_cmd()
    file_content = read_from_file(incoming_list[1])
    # pay attention to read_form_file function after using it you have to close the file

    registers = register_table()
    file_list = list()

    # take every line of given file as an element of file_list
    for line in file_content.readlines():
        file_list.append(line)

    symbol_table = create_symbol_table(file_list, instruction_table())
    print("final symbol table is: ", symbol_table)
    # take every element of file_list and remove the spaces every element and put them in line_content
    pc = 0
    for item in file_list:
        line_content = item.split()
        # check every element of line content in order  to understand what is that element
        if len(line_content) == 0:
            continue
        index = 0

        rt = RType()
        it = IType()
        jt = JType()

        for key in symbol_table.keys():
            if key == line_content[0]:
                index = 1
        check = check_type(line_content[index])
        if check == 'r':
            machine_codes.append(db.binary_to_decimal(rt.calc(item, registers)))
            print('first: ', machine_codes)
        elif check == 'i':
            machine_codes.append(db.binary_to_decimal(it.calc(item, pc, symbol_table, registers)))
            print('second: ', machine_codes)
        elif check == 'j':
            machine_codes.append(db.binary_to_decimal(jt.calc(item, symbol_table)))
            print('third: ', machine_codes)
        elif check == 'd':
            if line_content[index] == '.fill':
                flag = False
                for key in symbol_table.keys():
                    if key == line_content[index+1]:
                        machine_codes.append(symbol_table[key])
                        print('forth: ', machine_codes)
                        flag = True
                        break

                if not flag:
                    num = line_content[index+1].lstrip('-')
                    if num.isdigit():
                        machine_codes.append(int(line_content[index+1]))
                        print('fifth: ', machine_codes)
                        flag = True

                if not flag:
                    sys.exit('.fill value not found')

            elif line_content[index] == '.space':
                size = 0
                flag = False
                for key in symbol_table.keys():
                    if key == line_content[index + 1]:
                        size = symbol_table[key]
                        flag = True
                        break

                if not flag:
                    if line_content[index + 1].isdigit():
                        size = int(line_content[index + 1])
                        flag = True

                if not flag:
                    sys.exit('process: wrong .space value')
                for i in range(0, size):
                    machine_codes.append(0)
                print('6th: ', machine_codes)

        else:
            sys.exit('process: instruction not found!')
        pc += 1
        if pc > 65536:
            sys.exit('memory over fellow pc is more than 65536!')
    print('machine codes: ', machine_codes)
    write_to_file(incoming_list[2], machine_codes)
    return


def check_type(instruction):
    for key in RType.instructions.keys():
        if instruction == key:
            return 'r'
    for key in IType.instructions.keys():
        if instruction == key:
            return 'i'
    for key in JType.instructions.keys():
        if instruction == key:
            return 'j'
    if instruction == '.fill' or instruction == '.space':
        return 'd'

    return ''


# main function
def main():
    process()


if __name__ == '__main__':
    main()
