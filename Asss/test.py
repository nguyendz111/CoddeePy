import pandas as pd

# Load the CSV file
df = pd.read_csv('filename.csv')

# Display the first few rows of the data
print(df.head())



import pandas as pd
# Load the CSV file
df = pd.read_csv('filename.csv')

# Display the first few rows
print(df.head())

# Display the data types of each column
print(df.info())

# Get basic statistical summary
print(df.describe())



import pandas as pd

# Load the CSV file
df = pd.read_csv('filename.csv')

# Check for missing data
print(df.isnull().sum())



import pandas as pd

# Load the CSV file
df = pd.read_csv('filename.csv')

# Remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save the cleaned DataFrame back to a CSV file
df_cleaned.to_csv('filename_cleaned.csv', index=False)

# Optional: Display the number of duplicates removed
duplicates_removed = len(df) - len(df_cleaned)
print(f"{duplicates_removed} duplicates removed.")



import pandas as pd

# Load the CSV file
df = pd.read_csv('filename.csv')

# Check for negative values in the entire DataFrame
negative_values = df[df < 0]

# Display rows with negative values
print(df[negative_values.any(axis=1)])




import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('filename.csv')

# Define a function to remove special characters
def remove_special_characters(text):
    # Replace any character that is not a letter, digit, or space with an empty string
    return re.sub(r'[^A-Za-z0-9\s]+', '', str(text))

# Apply the function to the entire DataFrame
df_cleaned = df.applymap(remove_special_characters)

# Save the cleaned DataFrame back to a CSV file
df_cleaned.to_csv('filename_cleaned.csv', index=False)

# Optional: Display the cleaned DataFrame
print(df_cleaned.head())
