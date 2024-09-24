
#import some libraries
import sys
import math

# define a dictionary with elements and their corresponding atomic mass
atomic_mass_dictionary = {
	"H":	{"mass": 1.00797},
 	"D":	{"mass": 2.014},  
	"HE":	{"mass": 4.00260},
	"LI":	{"mass": 6.941},
	"BE":	{"mass": 9.01218},
	"B":	{"mass": 10.81},
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
	"UUB":	{"mass": 277},
 
	"X":	{"mass": 13.53277},	
	"*":	{"mass": 13.53277}, 
 
	"TIP":  {"mass": 18},
 
 	"HOH O":  {"mass": 15.9994},
	"HOH H":  {"mass": 1.00797},
  
	"DNA P": {"mass": 30.97376},
	"DNA O": {"mass": 15.9994},
	"DNA C": {"mass": 12.011},
	"DNA N": {"mass": 14.0067},
	"DNA H": {"mass": 1.00797}
 
}


#create an empty list to store atom type
atom_type = []

#create an empty list to store x coordinates
x = []
#create an empty list to store y coordinates
y = []
#create an empty list to store z coordinates
z = []
#create am empty list to store molecule type

#create an empty list to store element types
element_type = []


#identify errors in parsing the PDB
try:
	#opens a pdb file given as 1st command line parameter
	with open(sys.argv[1], 'r') as file:
    
    	#for every line
		for line in file:
                        
			if( ( line.startswith("ATOM") or line.startswith("HETATM") ) and
      			( line[13:21] != 'H1  TIP3') and 
       			( line[13:21] != 'H2  TIP3') ):
                
				#creates a variable from the column of atom type
				atom = line[0:3]
				#appends it to a list
				atom_type.append(atom)
                 
                #creates a variable from the column of x coordinate
				coord_x = line[30:38]
                #appends it to a list
				x.append(float(coord_x))

                #creates a variable from the column of y coordinate
				coord_y = line[38:46]
                #appends it to a list
				y.append(float(coord_y))

                #creates a variable from the column of z coordinate
				coord_z = line[46:54]
                #apends it to a list
				z.append(float(coord_z))

                #creates a variable from the column of the element type
				element_id = line[76:78]
                 	
				#creates a variable from the column of residue/solvent type
				residue = line[17:20]
     

 				#if TIP water molecule defined in residue columns
				if residue == "TIP":
					element_type.append("TIP")
      
				#if crystallographic oxygen from water molecule				
				elif residue == "HOH" and element_id == " O":
					element_type.append("HOH O")

				#if crystallohraphic/obabel hydrogen from water molecule				
				elif residue == "HOH" and element_id == " H":
					element_type.append("HOH H")
      

				# for DNA molecules
				elif (residue == "DA "):
					element_type.append("DNA " + element_id[1].upper())
          
				elif (residue == "DT "): 
					element_type.append("DNA " + element_id[1].upper())
					
				elif (residue == "DG "):
					element_type.append("DNA " + element_id[1].upper())
					
				elif (residue == "DC "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "DU "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "DI "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "I  "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "A  "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "U  "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "C  "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "G  "):
					element_type.append("DNA " + element_id[1].upper())
      
				elif (residue == "N  "):
					element_type.append("DNA " + element_id[1].upper())


				#if non-water non-DNA element defined in 1 char in element column
				elif (element_id[0] == ' '):
					element_type.append(element_id[1].upper())
                #if non-water non-DNA element defined in 2 chars
				elif (element_id[0] != ' '):
					element_type.append(element_id[0:2].upper())

         
except:
    print('error in parsing')


#identify errors in density calculations
try:
	#creates an empty list to store all atomic weights
	atomic_weight_dist = []

	#radius in which we calculate weighting density
	#given as 2nd command line parameter
	radius = float( sys.argv[2] )

	#creates a loop with range as the counted atoms
	#which is the same as the counted x coordinates that we use
	for i in range(len(atom_type)):
    
		if( (atom_type[i] != "HET") and 
     		(element_type[i][0:3] != "HOH") and 
       		(element_type[i] != "TIP") and
			(element_type[i][0:3] != "DNA") and
         	(atomic_mass_dictionary[element_type[i]]["mass"] > 12) ):
            
       		#set count variable to 0 for the current atom i
			count = 0
    
    		#creates a loop to compare every atom i with every other j
			for j in range(len(atom_type)):
        
        		#counts the distance between atom i and atom j
				distance = (  math.sqrt(  (( x[i] - x[j] ) * ( x[i] - x[j])) + 
                            			  (( y[i] - y[j] ) * ( y[i] - y[j] )) + 
                            		      (( z[i] - z[j] ) * ( z[i] - z[j] ))  )  )
        				
				#call the corresponding element id from its list
				element_id = element_type[j] 
    
    			#if distance is smaller than given radius
				if distance < radius:

					count += 1
    
    		#add the sum of atomic numbers of current atom to a list
			atomic_weight_dist.append(count)


	#calculate the volume of the sphere we want to calculate atomic density
	#based on the radius we gave as parameter
	volume = ((4*math.pi*radius*radius*radius)/(3))

	#create an empty list to store all densities
	density_dist=[]

	#for every item in atomic weights list
	for i in atomic_weight_dist:

    #calculate its corresponding density by dividing with sphere volume
		atom_density = ( i / volume )
    	#add the calculated density to a list
		density_dist.append(atom_density)

	#print the list
	for density in density_dist:
		print(density)

except:
	print('error in calculating distance')
