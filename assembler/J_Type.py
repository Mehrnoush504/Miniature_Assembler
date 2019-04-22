class JType:
    instructions = dict()
    op = ''
    target = ''
    instructions = {'j': '1101', 'halt': '1110'}

    def __init__(self):
        pass

    def calc(self, line, symbol_table):
        linecontent=line.splite()
        flag=False
        index=-1
        for key in this.instructions.key():
            if linecontent[0]==key:
                op=this.instructions[key]
                index=1
                flag=True
                break
            if not flag:
                for key in this.instructions.key():
                    if linecontent[1]==key:
                        op=this.instructions[key]
                        index=2
                        break
        if op=='j':
            for key in symbol_table.keys():
                if linecontent[index]==key:
                    target+=str(desimal_to_inary(symbol_table[key]))
                    if len(target)>16:
                        sys.exit('target out of range')
                    zero=''
                    for i in range(0,16-len(target)):
                        zero+='0'
                        target=zero+ target
                        break
        elif op='halt':
            target='0000000000000000'

        return'0000'+op+'00000000'+target
