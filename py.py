import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_excel('3247869.xlsx')

# Create a list of years to split the data by
years = range(1970, 2024, 10)

# Loop through the years and create a new sheet for each one
for i in range(len(years) - 1):
    start_year = years[i]
    end_year = years[i + 1] - 1
    sheet_name = f'{start_year}-{end_year}'
    df_slice = df[(df['DATE'] >= start_year) & (df['DATE'] <= end_year)]
    df_slice.to_excel('3247869.xlsx', sheet_name=sheet_name)

print('Done!')