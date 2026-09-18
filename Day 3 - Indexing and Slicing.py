#------------------------- DAY 3 -------------------------
# Description : Practiced accessing and manipulating specific elements and 
# sections of NumPy arrays using indexing and slicing. 
# Covered positive and negative indexing, 1D and 2D array slicing, selecting 
# specific rows and columns, step slicing, reversing arrays, and extracting subsets of 
# data from real-world style datasets. Practiced using start:stop:step and row,
# column notation for efficient array manipulation. 


import numpy as np

arr = np.array([15, 25, 35, 45, 55, 65])
print(arr[3])

print(arr[-2])

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr[2:5])

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[1:5])

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[0::2])

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[::-1])

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[2,1])
print(arr[1])
print(arr[:,2])

arr = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

print(arr[1:3,1:3])

import numpy as np


scores = np.array([
    [78, 85, 92],
    [65, 70, 75],
    [88, 91, 95],
    [55, 60, 68],
    [90, 87, 93]
])
# print(scores[2])
# print(scores[:,1])

print(scores[1:4,0:2])

import numpy as np
temperatures = np.array([
    [28, 30, 31, 29],
    [25, 27, 26, 28],
    [32, 34, 33, 35],
    [24, 26, 25, 27],
    [30, 31, 32, 33],
    [22, 23, 24, 25]
])
print(temperatures[0::2])


import numpy as np
sales = np.array([
    [101, 2500, 3],
    [102, 1800, 2],
    [103, 3200, 5],
    [104, 2100, 4],
    [105, 4500, 7],
    [106, 1700, 2]
])
print(sales[2:5,1:])