import pandas as pd

#Read the csv file into DataFrame

df = pd.read_csv('basic-data.csv')

print(df)

# Create a Series from a list
data = [10, 20, 30, 40, 50]

s1 = pd.Series(data)
print(s1)


print(s1[2]) # Access the element with label 2 (value 30)

print(s1.iloc[3]) # Access the element at position 3 (value 40)

print(s1[1:4])   # Access a range of elements by label

s = pd.Series([10, 20, 30, 40, None], index=['a', 'b', 'c', 'd', 'e'])

# Key Takeaways
# values gives raw data as a NumPy array.

# index shows labels.

# shape and size describe dimensions.

# mean, sum, min, max provide quick stats.

# unique and nunique help with distinct values.

# sort_values vs sort_index: one sorts by data, the other by labels.

# isnull and notnull are essential for missing data handling.

# apply lets you run custom functions element-wise.

# values: NumPy array of data
print(s.values)

# index: labels of the Series
print(s.index)

# shape: dimensions
print(s.shape)

# size: number of elements
print(s.size)

# mean, sum, min, max
print(s.mean())
print(s.sum())
print(s.min())
print(s.max())

# unique and nunique
print(s.unique())      # [10. 20. 30. 40. nan]
print(s.nunique())     # 4 (NaN not counted)

print('*******************************')

# sort_values and sort_index
print(s.sort_index())
print(s.sort_values())

# isnull and notnull
print('*******************************')
print(s.isnull())
print(s.notnull())

# apply: custom function
print('5*******************************')
print(s.apply(lambda x: x*2 if pd.notnull(x) else x))
# [20.0, 40.0, 60.0, 80.0, nan]

print('6*******************************')
# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, None]
}
df = pd.DataFrame(data)
print(df)

print(df['Name'])

print('7*******************************')
print(df.iloc[3]) # Access the third row by position
print(df.loc[1])    # Access the second row by label

print('8*******************************')

print(df[['Name','Age']])
print(df[1:3])             # Select specific rows
print('9*******************************')
unique_dates = df['Age'].unique()
print(unique_dates)

high_above_102 = df[df['Age'] > 30]
print(high_above_102)

df.to_csv('trading_data.csv', index=False)
print('10*******************************')
# shape: dimensions (rows, columns)
print(df.shape)

# info(): summary of DataFrame
print(df.info())
# Shows column names, data types, non-null counts

# describe(): summary statistics
print(df.describe())

# Gives mean, std, min, max for numerical columns
# head() and tail()
print(df.head(2)) # First 2 rows
print(df.tail(2)) # Last 2 rows

print('11*******************************')
# mean, sum, min, max
print(df['Age'].mean())   # 32.5
print(df['Salary'].sum()) # 180000.0
print(df['Age'].min())    # 25
print(df['Age'].max())    # 40



print('12*******************************')
# sort_values
print(df.sort_values(by='Age'))

# groupby
print(df.groupby('Age')['Salary'].mean())
# Groups by Age and calculates mean Salary

# fillna, drop, rename
print(df.fillna(0))      # Replace NaN with 0
print(df.drop(columns='Salary')) # Drop Salary column

print(df.rename(columns={'Salary':'Income'}))   


# apply: custom function
print(df['Age'].apply(lambda x: x*2))

# DataFrame Attributes and Methods
# DataFrames provide numerous attributes and methods for data manipulation and analysis, including:

# shape: Returns the dimensions (number of rows and columns) of the DataFrame.

# info(): Provides a summary of the DataFrame, including data types and non-null counts.

# describe(): Generates summary statistics for numerical columns.

# head(), tail(): Displays the first or last n rows of the DataFrame.

# mean(), sum(), min(), max(): Calculate summary statistics for columns.

# sort_values(): Sort the DataFrame by one or more columns.

# groupby(): Group data based on specific columns for aggregation.

# fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.

# apply(): Apply a function to each element, row, or column of the DataFrame.