from data.download_data import download_data
from database.database_operations import create_database, query_database
from analysis.data_cleaning import clean_data
from analysis.data_visualisation import plot_data

# Download the data
df = download_data()

# Clean the data
cleaned_data = clean_data(df)

# Create, connect to and populate the database
create_database(cleaned_data)

# Step 4: Query the database AS REQUIRED (changeable)
query = '''
SELECT *
FROM mental_health_survey 
'''
result_df = query_database(query)
print(result_df)

# Step 5: Visualize the data using matplotlib for easier understanding of the data
plot_data(cleaned_data)
