
import sys


"""
First run STRIDE from command line:
for file in ./*.pdb ; do ./stride ''$file'' >> stride_outputs/"$file".stride ; done

Then run this script from bash with: 
for file in stride_outputs/* ; do python3 stride_analysis.py ''$file'' >> secondary_structure_percentage_stride ; done 
"""


def stride_analysis(stride_output_file):
	"""
	This function reads file containing the STRIDE output and extracts secondary structure elements. 
 	It counts the occurrences of each secondary structure type and calculates the percentage of each type.
	"""

	with open(stride_output_file , "r") as input:
		elements = []
		for line in input:
			if line.startswith("ASG"):
				split = line.split()
										
				element = split[-5]         
				elements.append(element)
	
	# List of all possible structure types we want to include in the output
	all_structures = ["AlphaHelix", "Strand", "Turn", "Coil", "310Helix", "Bridge"]

	# Initialize counts for all possible structures with zero
	structure_counts = {structure: 0 for structure in all_structures}

	# Count occurrences in the input data
	for structure in elements:
		if structure in structure_counts:
			structure_counts[structure] += 1

	# Calculate total count of structures in input data
	total_count = len(elements)

	# Calculate percentages, ensuring all structures are included
	structure_percentages = {structure: (count / total_count) * 100 for structure, count in structure_counts.items()}

	# Display results
	print(sys.argv[1][-15:-11],  end = " ")
	for structure in all_structures:
		print(round(structure_percentages[structure], 3) , end = " ")
	print("")
 

stride_analysis(sys.argv[1])