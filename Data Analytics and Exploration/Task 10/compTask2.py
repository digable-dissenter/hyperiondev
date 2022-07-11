import pandas as pd
import numpy as np

# Read in the file credit.csv
credit = pd.read_csv('credit.csv',delimiter = ' ')

# Print the first 10 rows of the DataFrame
result = credit.head(10)
print("First 10 rows of the DataFrame:\n")
print(result)

# Print the Age and Education columns of the DataFrames.
for col_name in credit.columns:
    if col_name == 'Age':
        print(credit['Age'].values)
    if col_name == 'Education':
        print(credit['Education'].values)

# Select users who are above the age of 30.
print(credit[credit.Age > 30])
    
