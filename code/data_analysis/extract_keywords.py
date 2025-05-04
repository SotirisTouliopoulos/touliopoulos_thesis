
import sys


"""
for file in ./1_AMINOACID_CUTOFF/PDB_FORMATS/* ; do python3 extract_keywords.py ''$file''  >>  keywords_1_4  ;  done
"""


def extract_keywords(pdb_file, hierarchical_clusters_file):
    """
    This function reads a PDB file and extracts keywords from the header.
    It cleans the keywords by removing unwanted characters and prints them.
    """

    pdb_id = pdb_file[-8:-4]
    selected_ids = []
    with open(hierarchical_clusters_file, "r") as file:
        for line in file:
            parts = line.split()
            id_str = parts[0].strip('"')
            cluster_id = int(parts[1])
            
            if cluster_id in (1, 4):
                selected_ids.append(id_str)

    keywords = []
    if pdb_id in selected_ids:
        with open(pdb_file, "r") as input:
            for line in input:
                if line.startswith("KEYWDS"):
                    split = line.split()
                    for item in split:
                        if item != "KEYWDS":
                            try:
                                float(item)
                            except:
                                keywords.append(item)
                            finally:
                                pass
                        
        remove_chars = "\"()+!@?.:\{\}[]|`#$%^&*~,-;'/\\"
        translation_table = str.maketrans('', '', remove_chars)
        cleaned_list = [s.translate(translation_table) for s in keywords]

        print(sys.argv[1][-8:-4], end=" ")
        for i in cleaned_list:
            print(i, end=" ")
        print("")


hierarchical_clusters_file = "hierarchical_clusters_6A_df"
extract_keywords(sys.argv[1], hierarchical_clusters_file)