class IType:
    instructions = dict()
    op = ''
    rs = ''
    rt = ''
    imm = ''

    def __init__(self):
        pass

    def calc(self, line, pc, symbol_table):
        return