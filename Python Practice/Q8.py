# 8) Create your own Pandas dataframe df with three columns and a dozen rows. Do the following operations:
import numpy as np
# Creating Pandas Dataframe df

import pandas as pd

data = {
    'Temp': [30, 25, 27, 15, 13, 16, np.NAN, 45, 9, np.NAN, 11, np.NAN],
    'Date': ['01/01/2023', '01/02/2023', '01/03/2023', '01/04/2023', '01/05/2023', '01/06/2023', '01/07/2023',
             '01/08/2023', '01/09/2023', '01/10/2023', '01/11/2023', '01/12/2023'],
    'Day': ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday',
            'Wednesday', 'Thursday']
}

df = pd.DataFrame(data)
print(f'\nMy Pandas DataFrame:\n{df}')

# Insert a new column to df.

location = ['Mumbai', 'Delhi', 'Chennai', 'Kolkata', 'Pune', 'Hyderabad', 'Gujarat', 'Nagpur', 'Bangalore',
            'Rajasthan', 'Nashik', 'Jalandhar']
df['Location'] = location
print(f'\nDataframe after adding Location column:\n{df}')

# Add a new tuple to df.

df.loc[len(df.index)] = (35, '04/05/2022', 'Sunday', 'Manali')
print(f'\nDataframe after adding a tuple:\n{df}\n')

# Iterate over the rows of df and display.
for index, row in df.iterrows():
    print(f'Iterating the row {index} of df: {row["Day"], row["Location"]}')

# Display the column names of df.

print(f'\nColumn names of df are: {list(df.columns)}')

# Drop a list of rows based on some criterion applied to the first column
# (e.g., if the first column is an integer column then all rows with values of the first column greater than 25).

index_names = df[df["Temp"] > 20].index
df.drop(index_names, inplace=True)
print(f'\nDataFrame after dropping rows having temperature greater than 20:\n{df}\n')

# Export df into an Excel file and then import from the same.

df.to_excel("export-df-to-excel.xlsx")
print("DataFrame is exported successfully to 'export-df-to-excel.xlsx' Excel File.\n")
df = pd.read_excel('export-df-to-excel.xlsx')
print(f'Imported data from Excel: \n{df}')

# Replace all the NaN values with zeros in a column of df.
df = df.fillna(0)
print(f'\nAfter replacing NaN with 0:\n {df}')

# Set a given value for a particular cell in df.
df.at[5, 'Temp'] = 10
print(f'\nUpdated Dataframe:\n {df}')

# Divide df into in a given ratio.
ratio_50 = df.sample(frac=0.5)
print(f"\n50%  DataFrame: \n{ratio_50}")

# Rename a specific column name.
df.rename(columns={"Temp": "Temperature"},
          inplace=True)

print(f'\nUpdated Column names: {list(df.columns)}')

# Display the last three rows of df.

df_last_rows = df.tail(3)
print(f'\nLast three rows of Dataframe are: \n{df_last_rows}')
