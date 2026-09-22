# ------------- DAY 7 ---------------------------------
# Practiced NumPy array reshaping, flattening, and transposing.
# Learned how to use reshape() with -1, convert multidimensional arrays into 1D using 
# flatten(), and swap rows and columns using .T. Also practiced 
# understanding how array shapes change during different transformations.



import numpy as np

a = np.arange(1, 13)
b = a.reshape(3,4)
print(b)

b = a.reshape(4,-1)
print(b)


sales = np.array([
    [120, 150, 180],
    [200, 220, 250],
    [300, 320, 350]
])
print(sales.flatten())

scores = np.array([
    [80, 85, 90],
    [70, 75, 88]
])
print(scores.T)


a = np.arange(1, 25)
print(a.reshape(6,-1))

sales = np.array([
    [120, 150, 180, 200],
    [100, 130, 160, 190],
    [200, 220, 250, 280],
    [90, 110, 140, 170]
])
print(np.shape(sales))
print(sales.reshape(2,8))
print(sales.flatten())
print(sales.T)
print(np.shape(sales))
print(sales.flatten())