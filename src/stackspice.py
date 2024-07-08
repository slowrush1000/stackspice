
import sys

class Stackspice:
    def __init__(self):
        self.m_output_filename  = ''
        self.m_input_filename   = ''
        self.m_start_N          = 0
        self.m_end_N            = 0
        self.m_pinnames         = []
        self.m_cellname         = ''
        self.m_rvalue           = ''
    def PrintUsage(self):
        print(f'# stack_spice.py usage:')
        print(f'% python3 stack_spice.py output_file input_file start_N end_N rvalue')
    def ReadArgs(self, args):
        print(f'# read args start')
        if 6 != len(args):
            self.PrintUsage()
            exit()
        self.m_output_filename  = args[1]
        self.m_input_filename   = args[2]
        self.m_start_N          = int(args[3])
        self.m_end_N            = int(args[4])
        self.m_rvalue           = args[5]
        print(f'# read args end')
    def PrintInputs(self):
        print(f'# print inputs start')
        print(f'    output file : {self.m_output_filename}')
        print(f'    input file  : {self.m_input_filename}')
        print(f'    start N     : {self.m_start_N}')
        print(f'    end N       : {self.m_end_N}')
        print(f'    rvalue      : {self.m_rvalue}')
        print(f'# print inputs end')
    def ReadInputFile(self):
        print(f'# read input file({self.m_input_filename}) start')
        fin = open(self.m_input_filename, 'rt')
        lines  = []
        while True:
            line    = fin.readline()
            if not line:
                break
            line    = line.rstrip().lstrip()
            if 0 == len(line):
                continue
            #
            if '+' == line[0]:
                lines.append(line[1:])
            else:
                total_line  = ' '.join(lines)
                self.ReadTotalLine(total_line)
                lines       = [ line ]
        fin.close()
        print(f'# read input file({self.m_input_filename}) end')
    def ReadTotalLine(self, total_line):
        tokens      = total_line.split()
        if 0 == len(tokens):
            return
        #
        if '.subckt' == tokens[0].lower():
            self.m_cellname = tokens[1]
            for pos in range(2, len(tokens)):
                self.m_pinnames.append(tokens[pos])
    def PrintInputFile(self):
        print(f'# print input file start')
        print(f'    cellname : {self.m_cellname}')
        for pinname in self.m_pinnames:
            print(f'    pin      : {pinname}')
        print(f'    rvalue   : {self.m_rvalue}')
        print(f'# print input end start')
    def MakeSpiceFile(self):
        print(f'# make spice file({self.m_output_filename}) start')
        fout = open(self.m_output_filename, 'wt')
        for pos in range(self.m_start_N, self.m_end_N):
            fout.write(f'* {pos} stack\n')
            #
            lines   = []
            #
            lines.append(f'x_{pos}')
            #
            for pinname in self.m_pinnames:
                lines.append(f'+ {pinname}_{pos}')
            #
            lines.append(f'+ {self.m_cellname}')
            #
            total_line  = '\n'.join(lines)
            #
            fout.write(f'{total_line}\n')
        for pos in range(self.m_start_N, self.m_end_N - 1):
            fout.write(f'* {pos} - {pos + 1}\n')
            for pinname in self.m_pinnames:
                fout.write(f'r_{pinname}_{pos}_{pos + 1} {pinname}_{pos} {pinname}_{pos + 1} {self.m_rvalue}\n')
        fout.close()
        print(f'# make spice file({self.m_output_filename}) end')
    def Run(self, args):
        print(f'# stack_spice.py start')
        self.ReadArgs(args)
        self.PrintInputs()
        self.ReadInputFile()
        self.PrintInputFile()
        self.MakeSpiceFile()
        print(f'# stack_spice.py end')

def main(args):
    my_stack_spice  = Stackspice()
    my_stack_spice.Run(args)

if __name__ == '__main__':
    main(sys.argv)