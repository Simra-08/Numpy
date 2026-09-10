#-------------------- DAY 2 PRACTICE ----------------------------
# Description : Practiced NumPy array creation using zeros, ones, arange, 
# linspace, and random number generation, with hands-on exercises.


#np.zeroes

import numpy as np

array1 = np.zeros(5)
array2 = np.zeros((2,3))
print(array1)
print(array2)


# np.ones

array1 = np.ones(5)
array2 = np.ones((3,3))
print(array1)
print(array2)

# np.arange

array1 = np.arange(5)
array2 = np.arange(2,8)
array3 = np.arange(2,8,2)
print(array1)
print(array2)
print(array3)

# np.linspace


array1 = np.linspace(0,100,5)
print(array1)




# np.random

array1 = np.random.rand(5)
print(array1)
array2 = np.random.randint(1,10,5)
print(array2)

# 1
array1 = np.zeros(10)
print(array1)
# 2
array1 = np.ones((3,4))
print(array1)
# 3
array1 = np.arange(5,13)
print(array1)
# 4
array1 = np.linspace(0,20,5)
print(array1)
# 5
array1 = np.random.randint(1,51,10)
print(array1)
# 6
array1 = np.random.randint(10,100,(4,4))
print(array1)
#  
array1 = np.arange(2,21,2)
print(array1)
array2 = np.linspace(2,20,10)
print(array2)
