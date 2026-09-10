import numpy as np
# print(np.__version__)


# ---- INTRO -----
# array = np.array([1,2,3])
# array = array * 2
# print(array)

# ----- DIMENSIONS -----

# array = np.array('a')  --- 0D
# array = np.array([1,2,3]) ---- 1D
# array = np.array([ [1,2,3],[4,5,6] ]) --- 3D
# array = np.array([ [[1,2,3],[4,5,6]],
#                   [[1,2,3],[4,5,6]],
#                   [[1,2,3],[4,5,6]] ])
# print(array.ndim)


# ---- ACCESSING ------
# array = np.array([ [['A','B','C'],['D','E','F'],['G','H','I']],
#                     [['J','K','L'],['M','N','O'],['P','Q','R']],
#                     [['S','T','U'],['V','W','X'],['Y','Z',' ']] ])
# print(array.shape)
# word = array[0,0,0] + array[2,0,0] + array[2,0,0]
# print(word)


# ------ SLICING ----------------
# array = np.array([ [1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16] ])
# # print(array[1:2])
# print(array[:,-1])


# ---------- DAY 1 PRACTICE -----------------------------------------------
# import numpy as np
# array = np.array([1,2,3,4,5])
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)


# array = np.array([   [1,2,3],
#                      [4,5,6]   ])
# print(array.ndim)
# print(array.shape)
# print(array.dtype)


# array = np.array([ [[1,2,3],[4,5,6]],
#                     [[1,2,3],[4,5,6]] 
#                 ])
# print(array.ndim)
# print(array.shape)
# print(array.size)
# print(array.dtype)

# array = np.array([1.5,2,5,3,5])
# print(array.dtype)

# array = np.array([ [10, 20], [30, 40], [50, 60] ])
# print(array.ndim)
# print(array.shape)
# print(array.size)

# array = np.array([1.0,2,3,4,5,6,7,8,9,10])

# print(array.dtype)


# array = np.array([  [1,2,3,4],[5,6,7,8],[9,10,11,12]    ])
# print(array.ndim)
# print(array.shape)
# print(array.size)

# my_list = [1,2,3,4,5]
# my_array = np.array(my_list)
# print(type(my_array))
# print(my_array.ndim)


# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])
# print(array[:,1:])
# print(array[:,::2])
# print(array[0:2,0:2])
# print(array[2:,0:2])


# array = np.array([1,2,3])

# area = np.pi * array **2
# print(area)

#broadcasting

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]])
print(array1.shape)
print(array2.shape)
print(array1*array2)