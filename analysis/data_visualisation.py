import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df):
    """
    Creates various plots to visualize the data in the DataFrame.
    
    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
    """
    
    # Set the aesthetic style of the plots
    sns.set(style='whitegrid')

    # Plot Age Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Age'], bins=20, kde=True, color='skyblue')
    median_age = df['Age'].median()
    plt.axvline(median_age, color='red', linestyle='--', label=f'Median Age: {median_age:.2f}')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Age')
    plt.legend()
    plt.show(block=False)  # Show plot in a non-blocking way

    # Plot Gender Distribution
    plt.figure(figsize=(10, 6))
    gender_counts = df['Gender'].value_counts()
    sns.barplot(x=gender_counts.index, y=gender_counts.values, palette='viridis')
    for i, value in enumerate(gender_counts.values):
        plt.text(i, value + 10, f'{value}', ha='center', va='bottom')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.title('Gender Distribution')
    plt.show(block=False)  # Show plot in a non-blocking way

    # Plot Country Distribution
    plt.figure(figsize=(10, 6))
    country_counts = df['Country'].value_counts().nlargest(10)
    sns.barplot(x=country_counts.index, y=country_counts.values, palette='coolwarm')
    for i, value in enumerate(country_counts.values):
        plt.text(i, value + 10, f'{value}', ha='center', va='bottom')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.title('Top 10 Countries Distribution')
    plt.xticks(rotation=45)
    plt.show(block=False)  # Show plot in a non-blocking way

    # Plot Mental Health Consequences
    plt.figure(figsize=(10, 6))
    mental_health_consequence_counts = df['mental_health_consequence'].value_counts()
    sns.barplot(x=mental_health_consequence_counts.index, y=mental_health_consequence_counts.values, palette='plasma')
    for i, value in enumerate(mental_health_consequence_counts.values):
        plt.text(i, value + 10, f'{value}', ha='center', va='bottom')
    plt.xlabel('Mental Health Consequence')
    plt.ylabel('Count')
    plt.title('Mental Health Consequences at Workplace')

    plt.show(block=False)  # Show plot in a non-blocking way

    # Keep the plot windows open
    plt.show()  # This will make sure all plots remain open if using a script
