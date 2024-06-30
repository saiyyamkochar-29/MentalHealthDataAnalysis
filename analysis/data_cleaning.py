import pandas as pd
def clean_data(df):
    """
    Cleans the DataFrame by handling missing values, correcting data types, and standardizing categorical columns.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be cleaned.
    
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """

    # Printing initial state of the DataFrame
    print("Initial data shape:", df.shape)
    print("Initial missing values:\n", df.isnull().sum())
    print("Column names in the dataset:")
    print(df.columns)  # Printing column names to verify (test purposes)

    # Clean 'Age' column if it exists
    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert Age to numeric and coerce errors
        df['Age'].fillna(df['Age'].median(), inplace=True)    # Fill missing Age values with median
    else:
        print("'Age' column is not present in the dataset")

    # List of categorical columns to clean
    categorical_columns = ['Gender', 'self_employed', 'work_interfere']
    for column in categorical_columns:
        if column in df.columns:
            # Fill missing values with 'Unknown'
            df[column].fillna('Unknown', inplace=True)
           
            # Standardize text values by stripping whitespace and converting to lowercase
            df[column] = df[column].str.strip().str.lower()
            
            # Capitalize the first letter of each entry
            df[column] = df[column].str.capitalize()
            df[column] = df[column].astype('category')

            # Noticed issue: Correct common spelling mistakes for Gender
            if column == 'Gender':
                df[column] = df[column].replace({
                    'male': 'Male',
                    'female': 'Female',
                    'F': 'Female',  # Handling specific spelling mistakes I noticed
                    'M': 'Male',
                    'Maile': 'Male',
                    'Cis male': 'Male',
                    'Cis man': 'Male',
                    'Femaile': 'Female',
                    'Malr': 'Male',
                    'Mail': 'Male',
                    'Female (cis)': 'Female',
                    'Msle': 'Male',
                    'Man' : 'Male',
                    'Make' : 'Male',
                    'Femake' : 'Female',
                    'Male (cis)' : 'Male',
                    'Mal' : 'Male',
                    'Woman' : 'Female',
                    'Femail' : 'Female',
                    'Cis female' : 'Female'
                })
                # Replace any Gender values not specifically handled already for participant data privacy and ease of visualisation
                df[column] = df[column].apply(lambda x: x if x in ['Male', 'Female'] else 'Other')
        else:
            print(f"'{column}' column is not present in the dataset")

    # Remove rows with unreasonable values in Age (less than 18 or more than 100)
    if 'Age' in df.columns:
        df = df[(df['Age'] >= 18) & (df['Age'] <= 100)]

    # Remove rows with any remaining null values in critical columns
    df.dropna(subset=categorical_columns, inplace=True)

    # Log the shape and missing values after cleaning for analysis purposes
    print("Data shape after cleaning:", df.shape)
    print("Missing values after cleaning:\n", df.isnull().sum())
    
    return df
