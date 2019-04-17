import sys


# function for turning decimal into binary
def decimal_to_binary(num):
    s = bin(num)
    s = s[2:]
    print(s)
    return s


# main function
def main():
    print("hello world!")
    sys.exit(0)


if __name__ == '__main__':
    main()
