# NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices. NumPy stands for Numerical Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.

# NumPy is usually imported under the np alias.

# It's usually fixed in size and each element is of the same type. We can cast a list to a numpy array by first importing numpy:

# import numpy library

import numpy as np 

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

print(np.__version__)

# Check the type of the array

print(type(a))

print(a.dtype)

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])

# Enter your code here
print(type(b))

print(b.dtype)

# Create numpy array

c = np.array([20, 1, 2, 3, 4])
print(c)

# Assign the first element to 100

c[0] = 100
print(c)

# Assign the 5th element to 0

c[4] = 0
print(c)

a = np.array([10, 2, 30, 40,50])

# Enter your code here
a[1] = 20
print(a)

# Slicing the numpy array

d = c[1:4]
print(d)

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400
print(c)

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])

print(arr[:4])

print(arr[4:])

print(arr[1:5:])

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Enter your code here
print(arr[1:8:2])

# Create the index list

select = [0, 2, 3, 4]
print(select)

# Use List to select elements

d = c[select]
print(d)

# Assign the specified elements to new value

c[select] = 100000
print(c)

# Create a numpy array

a = np.array([0, 1, 2, 3, 4])
print(a)

# Get the size of numpy array

print(a.size)

# Get the number of dimensions of numpy array

print(a.ndim)

# Get the shape/size of numpy array

print(a.shape)

b = np.array([10, 20, 30, 40, 50, 60, 70])

# Enter your code here
print(b.size)

print(b.ndim)

print(b.shape)

#Numpy Statistical Functions

# Create a numpy array

a = np.array([1, -1, 1, -1])

print(a)
# Get the mean of numpy array

mean = a.mean()
print(mean)

# Get the standard deviation of numpy array

standard_deviation=a.std()
print(standard_deviation)

# Create a numpy array

b = np.array([-1, 2, 3, 4, 5])
print(b)

# Get the biggest value in the numpy array

max_b = b.max()
print(max_b)

# Get the smallest value in the numpy array

min_b = b.min()
print(min_b)

c = np.array([-10, 201, 43, 94, 502])

# Enter your code here
max_c = c.max()
print(max_c)
    
min_c = c.min()
print(min_c)
    
    
Sum = (max_c +min_c)
print(Sum)