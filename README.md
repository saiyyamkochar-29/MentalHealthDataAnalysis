# Mental Health Study Analysis

## Project Overview

This project analyzes a dataset related to mental health from the [Mental Health in Tech Survey](https://www.kaggle.com/osmi/mental-health-in-tech-survey). The analysis includes downloading the dataset, cleaning it, storing it in a SQLite database, querying the database, and visualizing the results.

## Project Structure

mental_health_project/

├── data/  

│   └── download_data.py         # Script to download and load dataset

├── database/  

│   └── database_operations.py    # Script for database operations

├── analysis/  

│   ├── data_cleaning.py          # Script for data cleaning  

│   └── data_visualization.py     # Script for data visualization

├── main.py                      # Main script to run the analysis  

└── requirements.txt             # Dependencies for the project

## Usage

### Running the Analysis

#### Download the Dataset

The dataset is automatically downloaded when you run the `main.py` script if it is not already present in the `data` directory.

#### Run the Main Script

`python main.py`

This script performs the following tasks:

- Downloads the dataset (if not already present).

- Cleans the dataset.

- Stores the cleaned data in a SQLite database.

- Queries the database to retrieve the data.

- Visualizes the data using matplotlib and seaborn.

## File Descriptions

- **data/download_data.py**: Contains a function to download the dataset from a given URL if it is not already present in the local directory. If the dataset is already present, it reads the dataset from the local file.

- **database/database_operations.py**: Contains functions to create and populate the SQLite database, and to query the database.

- **analysis/data_cleaning.py**: Contains functions to clean the dataset by handling missing values, correcting data types, and standardizing categorical columns.

- **analysis/data_visualization.py**: Contains functions to visualize the data using various plots.

- **main.py**: The main script that orchestrates the entire workflow.

## Data Cleaning

The data cleaning process includes:

- **Handling Missing Values**: Missing values in the 'Age' column are filled with the median age. Missing values in categorical columns are filled with 'Unknown'.

- **Correcting Data Types**: The 'Age' column is converted to numeric, and categorical columns are standardized.

- **Standardizing Categorical Columns**: Categorical columns are cleaned by stripping whitespace, converting to lowercase, capitalizing the first letter, and correcting common spelling mistakes.

- **Removing Outliers**: Ages outside the range of 18 to 100 are removed.

- **Handling Categorical Values**: Gender values are corrected for common spelling mistakes and standardized. Any gender value not specifically handled is replaced with 'Other'.

## Visualization

The following visualizations are generated:

- **Distribution of Age**: A histogram showing the distribution of participant ages, including a kernel density estimate (KDE) and median line.

- **Gender Distribution**: A bar plot displaying the distribution of genders with count labels.

- **Top 10 Countries Distribution**: A bar plot showing the count of participants from the top 10 countries, with labels and rotated x-axis ticks.

- **Mental Health Consequences at Workplace**: A bar plot showing the frequency of mental health consequences reported at the workplace.

## Dependencies

To run this project, you will need the following Python libraries:

- **pandas**
- **numpy**
- **matplotlib**
- **seaborn**
- **sqlite3 (part of the Python standard library)**
