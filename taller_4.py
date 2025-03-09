import numpy as np

# 1) Create a One-Dimensional Array
# a. Create a one-dimensional array with numbers from 1 to 10.
array_1d = np.arange(1, 11)
# b. Print the array.
print("1) One-Dimensional Array:", array_1d)

# 2) Create a Multidimensional Array
# a. Create a 2D matrix with 3 rows and 3 columns, filled with numbers from 1 to 9.
matrix_2d = np.arange(1, 10).reshape(3, 3)
# b. Print the matrix.
print("\n2) Two-Dimensional Matrix:\n", matrix_2d)

# 3) Basic Operations with Arrays
# a. Create two one-dimensional arrays with numbers from 1 to 5.
array_1 = np.arange(1, 6)
array_2 = np.arange(1, 6)
# b. Sum the two arrays and store the result in a new array.
sum_array = array_1 + array_2
# c. Print the result.
print("\n3) Sum of Two Arrays:", sum_array)

# 4) Mathematical Functions
# a. Create an array with numbers from 1 to 5.
array_3 = np.arange(1, 6)
# b. Calculate the exponential of each element of the array and store the result in a new array.
exp_array = np.exp(array_3)
# c. Print the new array.
print("\n4) Exponential of Array:", exp_array)

# 5) Indexing and Slicing
# a. Create an array with numbers from 1 to 10.
array_4 = np.arange(1, 11)
# b. Select the even elements of the array and store the result in a new array.
even_array = array_4[array_4 % 2 == 0]
# c. Print the new array.
print("\n5) Even Elements of Array:", even_array)

# 6) Random Data Generation
# a. Generate an array of 10 random numbers between 0 and 1.
random_array = np.random.rand(10)
# b. Print the array.
print("\n6) Random Array:", random_array)

# 7) Aggregation Functions
# a. Create an array with numbers from 1 to 5.
array_5 = np.arange(1, 6)
# b. Calculate the mean of the elements of the array.
mean_value = np.mean(array_5)
# c. Print the mean.
print("\n7) Mean of Array:", mean_value)

# 8) Creating Arrays with Factory Functions
# a. Create an array of 5 elements, all initialized with the value 7.
array_6 = np.full(5, 7)
# b. Print the array.
print("\n8) Array with Constant Value:", array_6)

# 9) Alignment and Broadcasting Operations
# a. Create two arrays: one with numbers from 1 to 3 and another with numbers from 4 to 6.
array_7 = np.arange(1, 3+1)
array_8 = np.arange(4, 6+1)
# b. Add the two arrays using broadcasting and store the result in a new array.
sum_broadcast_array = array_7 + array_8
# c. Print the new array.
print("\n9) Sum with Broadcasting:", sum_broadcast_array)

# 10) Transformation and Resizing Functions
# No code provided for this section.
