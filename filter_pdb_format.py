
import sys

with open(sys.argv[1], 'r') as file:
    print('MODEL        1')
    for line in file:
        if line.startswith('ATOM') or line.startswith('HETATM'):
            #only A conformations for LYS , ARG etc
            if line[16] == 'A' or line[16] == ' ' :
                print(line[:-1])
        elif line.startswith('ENDMDL') :
            break