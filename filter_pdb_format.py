
import sys

with open(sys.argv[1], 'r') as file:
    for line in file:
        if line.startswith('ATOM') or line.startswith('HETATM') or line.startswith("MODEL"):
            #only A conformations for LYS , ARG etc
            if line[16] == 'A' or line[16] == ' ' :
                print(line[:-1])
