import pandas as pd
import os

def download_data():
    """
    Downloads a dataset from a given URL if it is not already present
    in the local directory. If the dataset is already present, it reads
    the dataset from the local file.
    
    Returns:
        pd.DataFrame: The dataset as a Pandas DataFrame.
    """
    
    # URL where the dataset is hosted
    url = 'https://raw.githubusercontent.com/saiyyamkochar-29/tech_survey_data/main/survey.csv'
    
    # Path to save the dataset locally
    dataset_path = os.path.join(os.path.dirname(__file__), 'survey.csv')
    
    # Check if the dataset file already exists locally
    if not os.path.exists(dataset_path):
        # Download the dataset from the URL and load it into a DataFrame
        df = pd.read_csv(url)
        # Save the DataFrame to a local CSV file
        df.to_csv(dataset_path, index=False)
    else:
        # If the file already exists, read the DataFrame from the local CSV file
        df = pd.read_csv(dataset_path)
    
    return df
