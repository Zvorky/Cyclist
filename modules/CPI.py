#	CPI.py

#	~ Enzo Zavorski Delevatti
#	Aug 2022

''' UNIVALI – Arquitetura e Organização de Computadores II
    Prof. Douglas Rossi de Melo
    Avaliação 01 – Desempenho                               '''


#   RISC-V RV32I OpCodes
opcode = {  '0000011': 5,
            '0100011': 4,
            '1100011': 3,
            '1100111': 3,
            '0001111': 4,
            '1101111': 3,
            '0010011': 4,
            '0110011': 4,
            '1110011': 4,
            '0010111': 4,
            '0110111': 4
        }

def pathInput(msg = ''):
    path = input(msg)

    if(len(path) > 1):
        # Remove initial blank spaces
        while(path[0] == ' ' and len(path) > 1):
            path = path[1:]

        # Remove final blank spaces
        while(path[len(path)-1] == ' ' and len(path) > 1):
            path = path[:len(path)-1]

        # Remove '' and ""
        if((path[0] == "'" and path[len(path)-1] == "'") or (path[0] == '"' and path[len(path)-1] == '"')):
            path = path[1:len(path)-1]
    
    return path

def checkFile(path: str):
    try:
        with open(path, 'rb') as file:
            for line in file:
                line = line.decode()

                if(line[30:32] != '11'):    # OpCode
                    return False

                for digit in line:
                    if(digit != '0' and digit != '1' and digit != '\n'):
                        return False

            return True

    except FileNotFoundError:
        return False

    except IsADirectoryError:
        return False

class CPI:
    def __init__(self, path):
        self.path = path
        self.file = open(path)
        self.log = ''
        self.cycles_log = [[],[],[]]    # index + 3 = cycles
        self.instructions = self.Instructions()
        self.cycles = self.Cycles()
        self.cpi = self.CPI()
    
    def Instructions(self):
        self.instructions = 0
        for line in self.file:
            self.instructions += 1
        return self.instructions
    
    def Cycles(self):
        self.cycles = 0
        self.log = 'line \tinstruction[31:7] \t\tOpCode    \tCycles\n'
        with open(self.path) as self.file:
            l = 0
            for line in self.file:
                l += 1
                self.log += str(l) + ' \t' + line[0:25] + ' \t' + line[25:32]
                try:
                    self.cycles += opcode[line[25:32]]
                    self.cycles_log[opcode[line[25:32]]-3].append(l)
                    self.log += ' \t' + str(opcode[line[25:32]]) + '\n'

                except KeyError:
                    self.log += ' \tInvalid OpCode\n'
                    return -1
                    
        return self.cycles

    def CPI(self):
        if(self.cycles < 0):    # Error
            self.cpi = -1
            return -1
        
        self.cpi = self.cycles / self.instructions
        return self.cpi
    
    def CyclesLog(self):
        log = ['3 Cycles: ','4 Cycles: ','5 Cycles: ']
        log[0] += str(len(self.cycles_log[0]))
        log[1] += str(len(self.cycles_log[1]))
        log[2] += str(len(self.cycles_log[2]))
        return log


if __name__ == "__main__":
    filepath = pathInput('Input File to calculate: ')
    while(not checkFile(filepath)):
        filepath = pathInput('\nIncompatible or Inexistent File...\n{}\n\n: '.format(filepath))

    cpi = CPI(filepath)
    print('\n{} Instructions\n{} Cycles\nCPI = {}'.format(cpi.instructions, cpi.cycles, cpi.cpi))
    print('\nInstructions with:')
    for i in cpi.CyclesLog():
        print(i)
    print('\n' + cpi.log)