# ---------------------- DAY 1 PRACTICE -------------------------------------
# Description : Practiced NumPy array creation and explored array properties 
# such as dimensions, shape, size, and data type using 1D, 2D, and 3D arrays.

import numpy as np
array = np.array([1,2,3,4,5])
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)


array = np.array([   [1,2,3],
                     [4,5,6]   ])
print(array.ndim)
print(array.shape)
print(array.dtype)


array = np.array([ [[1,2,3],[4,5,6]],
                    [[1,2,3],[4,5,6]] 
                ])
print(array.ndim)
print(array.shape)
print(array.size)
print(array.dtype)

array = np.array([1.5,2,5,3,5])
print(array.dtype)

array = np.array([ [10, 20], [30, 40], [50, 60] ])
print(array.ndim)
print(array.shape)
print(array.size)

array = np.array([1.0,2,3,4,5,6,7,8,9,10])

print(array.dtype)


array = np.array([  [1,2,3,4],[5,6,7,8],[9,10,11,12]    ])
print(array.ndim)
print(array.shape)
print(array.size)

my_list = [1,2,3,4,5]
my_array = np.array(my_list)
print(type(my_array))
print(my_array.ndim)


array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
print(array[:,1:])
print(array[:,::2])