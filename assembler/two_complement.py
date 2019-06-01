import sys

import decimal_and_binary_converter as db


# Function to reverse a string
def reverse(string):
    string = "".join(reversed(string))
    return string


def tow_comp(num):
    n = db.decimal_to_binary(abs(num))
    b = str(n)
    if len(b) > 16:
        sys.exit('tow comp: len/imm out of range')
    zero = ''
    for i in range(0, 16-len(b)):
        zero += '0'
    binary = zero + b
    binary = reverse(binary)
    cnt = 0
    result = ''
    for i in range(0, 16):
        if binary[i] == '1':
            cnt += 1
        if cnt <= 1:
            result += binary[i]
            cnt += 1
        else:
            if binary[i] == '1':
                result += '0'
            elif binary[i] == '0':
                result += '1'
            else:
                sys.exit('two comp bad bit')
    print(reverse(result))
    return reverse(result)

