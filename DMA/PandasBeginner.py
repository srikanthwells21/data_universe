import pandas as pd

#Read the csv file into DataFrame

df = pd.read_csv('basic-data.csv')

print(df)

# Create a Series from a list
data = [10, 20, 30, 40, 50]

s = pd.Series(data)
print(s)


print(s[2]) # Access the element with label 2 (value 30)

print(s.iloc[3]) # Access the element at position 3 (value 40)

print(s[1:4])   # Access a range of elements by label

