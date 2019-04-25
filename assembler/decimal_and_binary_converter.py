# function for turning decimal into binary
def decimal_to_binary(num):
    s = bin(num)
    s = s[2:]
    print(s)
    return s


# function for turning binary to decimal
def binary_to_decimal(binary):
    return int(binary, 2)
