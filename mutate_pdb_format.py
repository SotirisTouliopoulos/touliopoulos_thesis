

# script that converts HETATM records from crystallographic water to ATOM records

import sys

try:    
    with open(sys.argv[1], 'r') as file:
        print('MODEL        1')
        for line in file:
            if line.startswith('ATOM'):
                if line[16] == 'A' or line[16] == ' ' :
                    print(line[:-1])
                    #pass
            elif line.startswith('ENDMDL') :
                break
        
            elif line.startswith("HETATM"):
                residue = line[17:20] 
                if residue == "HOH":
                    atom_number = line[6:13]
                    print("ATOM ", atom_number, line[14:-1])
        
except:
    print("error in mutating")            
            