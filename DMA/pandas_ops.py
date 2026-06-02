# Dependency needed to install file 

# %pip install xlrd openpyxl

# Import required library

import pandas as pd

# Read data from CSV file

# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv'
# df = pd.read_csv(csv_path)

#from pyodide.http import pyfetch --not needed since running code form VS code
import pandas as pd
import requests

# filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"

# async def download(url, filename):
#     response = await pyfetch(url)
#     if response.status == 200:
#         with open(filename, "wb") as f:
#             f.write(await response.bytes())


# await download(filename, "Product-sales.csv")
# df = pd.read_csv("Product-sales.csv")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
filename = "Product-sales.csv"

response = requests.get(url)
with open(filename, "wb") as f:
    f.write(response.content)

df = pd.read_csv(filename)
print(df.head())

#filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/LXjSAttmoxJfEG6il1Bqfw/Product-sales.csv"
#df = pd.read_csv(filename)

# Read data from Excel File and print the first five rows

# Correct URL
xlsx_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx"

# Local filename
xlfilename = "Product-sales.xlsx"

# Download the file
response = requests.get(xlsx_path)
with open(xlfilename, "wb") as f:
    f.write(response.content)

# Read Excel file into DataFrame
df = pd.read_excel(xlfilename)
print(df.head())

#xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n9LOuKI9SlUa1b5zkaCMeg/Product-sales.xlsx'
#df = pd.read_excel(xlsx_path)
#df.head()

print('**********************')
print(df.iloc[0,1] )
# Access to the column Length

x = df[['Quantity']]
print(x)

# Get the column as a series

x = df['Product']
print(x)

# Get the column as a dataframe

x = df[['Quantity']]
print(type(x))

# Access to multiple columns

y = df[['Product','Category', 'Quantity']]
print(y)

# Access the value on the first row and the first column

df.iloc[0, 0]

# Access the value on the second row and the first column

df.iloc[1,0]

# Access the value on the first row and the third column

df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Slicing the dataframe

df.iloc[0:2, 0:3]

# Slicing the dataframe using name

df.loc[0:2, 'OrderID':'Category']


#Use the following list to convert the dataframe index df to characters and assign it to df_new; find the element corresponding to the row index a and column 'CustomerCity'. Then select the rows a through d for the column 'CustomerCity'

new_index=['a','b','c','d','e']
df_new=df
df_new.index=new_index
df_new.loc['a', 'CustomerCity']
df_new.loc['a':'d', 'CustomerCity']