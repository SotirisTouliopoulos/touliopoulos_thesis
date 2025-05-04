
from prody import parsePDBHeader
import pandas as pd
from pypdb import *
import os


def classifications_per_cluster(pdb_files_dir, ids, clusters):
    """
    This function reads the PDB files from a specified directory, extracts the classification information from the headers,
    and counts the occurrences of each classification per cluster.
    """
    
    dataframe = []
    for pdb in os.listdir(pdb_files_dir):
        pdb_id = pdb[-8:-4]

        if pdb_id in ids:
            pdb = pdb_files_dir + "/" + pdb
            cluster = clusters[ids.index(pdb_id)]
            
            try:
                pdb_id = pdb[-8:-4]
                        
                header = parsePDBHeader(pdb)
                pattern = r'[^a-zA-Z0-9]+'
                classification = header['classification'].lower()
                split_classification = re.split(pattern, classification)
                classification = ' '.join(split_classification)
                                            
                dataframe.append( { 'id': pdb_id, 
                                    'classification': classification,
                                    'cluster': cluster} )        
            except:
                pass

    dataframe = pd.DataFrame(dataframe)

    classification_counts = dataframe.assign(classification = dataframe['classification'].str.split()).explode('classification')
    classification_counts = classification_counts.groupby('cluster')['classification'].value_counts()

    return classification_counts


cluster_df = pd.read_csv("cluster_all_df")

ids = cluster_df["id"].tolist()
clusters = cluster_df["cluster"].tolist()
pdb_files_dir = '/home/touliopoulos/project/ptixiaki/filter_pdb_format_obabel/1_AMINOACID_CUTOFF/PDB_FORMATS'

classification_counts = classifications_per_cluster(pdb_files_dir, ids, clusters)
classification_counts.to_csv("classification_counts_all.csv")