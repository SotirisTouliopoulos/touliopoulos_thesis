
#Filter files for OpenBabel

import sys

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line.startswith('ATOM') or line.startswith('HETATM') or line.startswith("MODEL") or line.startswith("ENDMDL") or line.startswith("END") or line.startswith("TER"):
            #only A conformations for LYS , ARG etc
            if line[16] == 'A' or line[16] == ' ' :
                print(line[:-1])
