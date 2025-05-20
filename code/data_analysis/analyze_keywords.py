
import pandas as pd


def analyze_keywords(keywords_file):
    
    """
    This function reads a file containing keywords associated with PDB IDs,
    processes the keywords, and creates a DataFrame with the keywords as columns.
    Each row corresponds to a PDB ID, and the values are binary indicators of
    whether the keyword is present (1) or absent (0).
    """
        
    # Read the file line by line
    with open(keywords_file, "r") as f:
        data = [line.strip().split(maxsplit=1) for line in f]

    # Get unique keywords across all lines
    keywords = set()
    for _, words in data:
        keywords.update(words.split())

    # Create a sorted list of keywords for consistent column ordering
    keywords = sorted(keywords)

    # Initialize list for processed data
    processed_data = []

    # Process each line
    for pdb_id, words in data:
        word_list = words.split()
        row = {keyword: 1 if keyword in word_list else 0 for keyword in keywords}
        row["ID"] = pdb_id
        processed_data.append(row)

    # Create a DataFrame and reorder columns
    keywords_df = pd.DataFrame(processed_data)
    keywords_df = keywords_df[["ID"] + keywords]
    
    return keywords_df


keywords_df = analyze_keywords(keywords_file="keywords_4_6_new_space")
keywords_df.to_csv("keywords_4_6_new_space_df.csv", index=False)
