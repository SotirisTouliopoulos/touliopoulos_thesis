
import sys
from statistics import mean 


atomic_mass_dictionary = {
	"C":	{"mass": 12.011},
	"N":	{"mass": 14.0067},
	"O":	{"mass": 15.9994},
	"F":	{"mass": 18.998403},
	"NE":	{"mass": 20.179},
	"NA":	{"mass": 22.98977},
	"MG":	{"mass": 24.305},
	"AL":	{"mass": 26.98154},
	"SI":	{"mass": 28.0855},
	"P":	{"mass": 30.97376},
	"S":	{"mass": 32.06},
	"CL":	{"mass": 35.453},
	"K":	{"mass": 39.0983},
	"AR":	{"mass": 39.948},
	"CA":	{"mass": 40.08},
	"SC":	{"mass": 44.9559},
	"TI":	{"mass": 47.90},
	"V":	{"mass": 50.9415},
	"CR":	{"mass": 51.996},
	"MN":	{"mass": 54.9380},
	"FE":	{"mass": 55.847},
	"NI":	{"mass": 58.70},
	"CO":	{"mass": 58.9332},
	"CU":	{"mass": 63.546},
	"ZN":	{"mass": 65.38},
	"GA":	{"mass": 69.72},
	"GE":	{"mass": 72.59},
	"AS":	{"mass": 74.9216},
	"SE":	{"mass": 78.96},
	"BR":	{"mass": 79.904},
	"KR":	{"mass": 83.80},
	"RB":	{"mass": 85.4678},
	"SR":	{"mass": 87.62},
	"Y":	{"mass": 88.9059},
	"ZR":	{"mass": 91.22},
	"NB":	{"mass": 92.9064},
	"MO":	{"mass": 95.94},
	"TC":	{"mass": 98},
	"RU":	{"mass": 101.07},
	"RH":	{"mass": 102.9055},
	"PD":	{"mass": 106.4},
	"AG":	{"mass": 107.868},
	"CD":	{"mass": 112.41},
	"IN":	{"mass": 114.82},
	"SN":	{"mass": 118.69},
	"SB":	{"mass": 121.75},
	"I":	{"mass": 126.9045},
	"TE":	{"mass": 127.60},
	"XE":	{"mass": 131.30},
	"CS":	{"mass": 132.9054},
	"BA":	{"mass": 137.33},
	"LA":	{"mass": 138.9055},
	"CE":	{"mass": 140.12},
	"PR":	{"mass": 140.9077},
	"ND":	{"mass": 144.24},
	"PM":	{"mass": 145},
	"SM":	{"mass": 150.4},
	"EU":	{"mass": 151.96},
	"GD":	{"mass": 157.25},
	"TB":	{"mass": 158.9254},
	"DY":	{"mass": 162.50},
	"HO":	{"mass": 164.9304},
	"ER":	{"mass": 167.26},
	"TM":	{"mass": 168.9342},
	"YB":	{"mass": 173.04},
	"LU":	{"mass": 174.967},
	"HF":	{"mass": 178.49},
	"TA":	{"mass": 180.9479},
	"W":	{"mass": 183.85},
	"RE":	{"mass": 186.207},
	"OS":	{"mass": 190.2},
	"IR":	{"mass": 192.22},
	"PT":	{"mass": 195.09},
	"AU":	{"mass": 196.9665},
	"HG":	{"mass": 200.59},
	"TL":	{"mass": 204.37},
	"PB":	{"mass": 207.2},
	"BI":	{"mass": 208.9804},
	"PO":	{"mass": 209},
	"AT":	{"mass": 210},
	"RN":	{"mass": 222},
	"FR":	{"mass": 223},
	"RA":	{"mass": 226.0254},
	"AC":	{"mass": 227.0278},
	"PA":	{"mass": 231.0359},
	"TH":	{"mass": 232.0381},
	"NP":	{"mass": 237.0482},
	"U":	{"mass": 238.029},
	"PU":	{"mass": 242},
	"AM":	{"mass": 243},
	"BK":	{"mass": 247},
	"CM":	{"mass": 247},
	"NO":	{"mass": 250},
	"CF":	{"mass": 251},
	"ES":	{"mass": 252},
	"HS":	{"mass": 255},
	"MT":	{"mass": 256},
	"FM":	{"mass": 257},
	"MD":	{"mass": 258},
	"LR":	{"mass": 260},
	"RF":	{"mass": 261},
	"BH":	{"mass": 262},
	"DB":	{"mass": 262},
	"SG":	{"mass": 263},
	"UUN":	{"mass": 269},
	"UUU":	{"mass": 272},
	"UUB":	{"mass": 277} 	
}


#create an empty list to store element types
elem_id_list = []

#identify errors in parsing the PDB
try:
	#opens a pdb file given as 1st command line parameter
    with open(sys.argv[1], 'r') as file:
    
    	#for every line
        for line in file:

        	#only for lines starting with 'ATOM'
            if line.startswith('ATOM') or line.startswith('HETATM'):
            
            	#only A conformations for LYS , ARG etc
                if line[16] == 'A' or line[16] == ' ' :

                	#creates a variable from the column of the element type
                    element_id = line[76:78]
                	
                    #if element id is defined in 1 char
                    if element_id[0] == ' ':
                        #keep elements with sufficient electron density
                        if element_id[1] != 'H' and element_id[1] != 'B' and element_id[1] != 'D' and element_id[1] != 'X':
                            elem_id_list.append(element_id[1])
                	
                    #else if it is defined in 2 chars
                    else:
                        #keep elements with sufficient electron density                        
                        if element_id[0:2] != 'BE' and element_id[0:2] != 'HE' and element_id[0:2] != 'LI':
                            elem_id_list.append(element_id[0:2])
                
        	#for lines starting with ENDMDL stops the proccess,
        	#the current structure model ends
            elif line.startswith('ENDMDL') :
                break

except:
    print('error in parsing')
    

#create a list to add every atomic weight
weights_list = []

#loop through element id list
for j in range(len(elem_id_list)):
    
    #call the corresponding element id from its list
    element_id = elem_id_list[j] 

    #return the corresponding atomic mass from the dictionary
    weight = atomic_mass_dictionary[element_id]["mass"]
    
    weights_list.append(weight)

    
#calculate mean value from weights list
mean = mean(weights_list)

print( "%.5f" % mean )
