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


x1 = {
'Student' : ['David', 'Samuel', 'Terry', 'Evan'],
'Age': [27, 24, 22, 32],
'Country': ['UK', 'Canada', 'China', 'USA'],
'Course' : ['Pyhton', 'Data Structures', 'Machine Learning', 'Web Development'],
'Marks' : [85, 72, 89, 76]

}

df1 = pd.DataFrame(x1)

# Exercise 2: loc() and iloc() functions
# loc() is a label-based data selecting method which means that we have to pass the name of the row or column that we want to select. This method includes the last element of the range passed in it.

# Simple syntax for your understanding:

# loc[row_label, column_label]
# iloc() is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column. This method does not include the last element of the range passed in it.

# Simple syntax for your understanding:

# iloc[row_index, column_index]
# Let us see some examples on 

# Access the value on the first row and the first column

print('**********************************************************************')

print('***********firstvalue**************')
firstvalue = df1.iloc[0, 0]
print(firstvalue)

# Access the value on the first row and the third column
print('***********firstrow_thirdcolumn**************')
firstrow_thirdcolumn = df1.iloc[0,2]
print(firstrow_thirdcolumn)

# Access the column using the name
print('***********Marks**************')
Marks1 = df1.loc[0, 'Marks']

# Column labels
print(df1.columns)   # Index(['Name', 'Age', 'Salary'], dtype='object')

# Row labels (index)
print(df1.index)     # RangeIndex(start=0, stop=3, step=1)

#salary1 = df1.loc[1, 1]
print(Marks1)


print('***********new df**************')
df2=df
print(df2)

df2=df2.set_index("Name")
print(df2)

print('***********head**************')
#To display the first 5 rows of new dataframe
print(df2.head())

print('***********loc**************')
#Now, let us access the column using the name
print(df2.loc['Bob', 'Salary'])

#Use the loc() function,to get the Department of Jane in the newly created dataframe df2.
print('***********row lable and column name**************')
print(df2.loc['Charlie', 'Age'])

print('***********row position and column name**************')
#Use the iloc() function to get the Salary of Mary in the newly created dataframe df2.
print(df2.iloc[3,1])

# let us do the slicing using old dataframe df

print('***********df**************')
print('***********df**************')
print('***********df**************')
print('***********df**************')
print(df)
print('***********df**************')
print(df.iloc[0:2])
print('***********df1**************')
print(df.iloc[0:2, 0:3])

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
print(df.loc[0:2,'Name':'Age'])

#let us do the slicing using loc() function on new dataframe df2 where index column is Name having labels: Rose, John and Jane
print(df2.loc['Bob':'Charlie', 'Age':'Salary'])

# using loc() function, do slicing on old dataframe df to retrieve the Name, ID and department of index column having labels as 2,3
print(df.loc[2:3,'Name':'Age'])