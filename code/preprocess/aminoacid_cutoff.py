

import sys

with open( sys.argv[1] , 'r' ) as file:
    atom_list = []
    for line in file:
        if line.startswith('ATOM'):
            atom = line[13:15]
            atom_list.append(atom)


aminoacid = 0
for i in range(len(atom_list)):
    if atom_list[i] == 'CA' :
        aminoacid +=1


if aminoacid < 51:
    with open ( 'cutoff.txt' , 'a' ) as output :
        output.write( str(sys.argv[1]) + str('\n'))


