
import sys
from Bio.PDB import PDBParser
import numpy as np


"""
for file in 1_AMINOACID_CUTOFF/PDB_FORMATS/* ; do python3 alpha_carbons_bfactors_water_mass.py ''$file'' >> alpha_carbons_bfactors_water_mass.counts ; done
"""


def total_alpha_carbons(pdb_file):
    parser = PDBParser(QUIET=True) 
    structure = parser.get_structure("structure", pdb_file)
    all_models_alpha_carbons = sum(1 for atom in structure.get_atoms() if atom.get_id() == 'CA')
        
    return all_models_alpha_carbons


def median_bfactor(pdb_file):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("structure", pdb_file)
    
    # Initialize list to store all B-factors from all models
    b_factors = []
    
    for model in structure:
        for chain in model:
            for residue in chain:
                for atom in residue:
                    # Append B-factor to the list
                    b_factors.append(atom.get_bfactor())
    
    # Convert to numpy array for statistical calculations
    b_factors = np.array(b_factors)
    median_bfactor = np.median(b_factors)
    
    return round(median_bfactor, 4)
    

def total_water_mass(pdb_file):
    water_mass = 18.01528

    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("structure", pdb_file)
    
    total_waters = 0

    for model in structure:
        for chain in model:
            for residue in chain:
                # Check if it's a water molecule (usually residue name 'HOH')
                if residue.get_resname() == 'HOH':
                    total_waters += 1

    total_mass = total_waters * water_mass
    
    return total_mass
    
    

all_models_alpha_carbons = total_alpha_carbons(sys.argv[1])
median_of_bfactors = median_bfactor(sys.argv[1])
total_mass_of_water = total_water_mass(sys.argv[1])
normalized_water_mass = round(( total_mass_of_water / all_models_alpha_carbons), 4)


print(sys.argv[1][-8:-4], end = " ")
print(all_models_alpha_carbons, median_of_bfactors, normalized_water_mass, end=" ")
print("")
