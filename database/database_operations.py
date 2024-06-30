import sqlite3
import pandas as pd

def create_database(df, db_name='mental_health_study.db'):
    """
    Creates an SQLite database and saves a DataFrame to it as a table.
    
    Parameters:
        df (pd.DataFrame): The DataFrame to be saved in the database.
        db_name (str): The name of the SQLite database file. Defaults to 'mental_health_study.db'.
    """
    
    # Establish a connection to the SQLite database (creates the database file if it does not exist)
    conn = sqlite3.connect(db_name)
    
    # Save the DataFrame to the database as a new table named 'mental_health_survey'
    # If the table already exists, it will be replaced
    df.to_sql('mental_health_survey', conn, if_exists='replace', index=False)
    
    # Close the connection to the database
    conn.close()

def query_database(query, db_name='mental_health_study.db'):
    """
    Executes a SQL query on an SQLite database and returns the result as a DataFrame.
    
    Parameters:
        query (str): The SQL query to be executed.
        db_name (str): The name of the SQLite database file. Default will be 'mental_health_study.db'.
    
    Returns:
        pd.DataFrame: The result of the REQUIRED SQL query (as written on main-py) as a DataFrame.
    """
    
    # Establish a connection to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Execute the SQL query and load the result into a DataFrame
    result_df = pd.read_sql(query, conn)
    
    # Close the connection to the database
    conn.close()
    
    return result_df
