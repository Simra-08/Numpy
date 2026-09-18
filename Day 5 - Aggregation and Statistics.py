# -------------------------- DAY 5 -----------------------------------------
# Description Practiced NumPy aggregation and statistical operations including sum(),
# mean(), average(), min(), max(), median(), std(), and argmax().
# Learned how to use axis=0 and axis=1 to perform calculations across rows and columns, 
# and applied these concepts to analyze product-wise and quarter-wise sales data.

import numpy as np



sales = np.array([120, 250, 180, 300, 150])
print(np.sum(sales))
print(np.average(sales))
print(np.max(sales))
print(np.min(sales))
print(np.median(sales))

sales = np.array([120, 250, 180, 300, 150])
print(np.argmax(sales))

sales = np.array([
    [100, 200, 300],
    [400, 500, 600],
    [700, 800, 900]
])

print(np.sum(sales))
print(np.sum(sales,axis=1))
print(np.sum(sales,axis=0))

marks = np.array([
    [80, 90, 70],
    [60, 75, 85],
    [95, 80, 90]
])
print(np.average(marks))
print(np.sum(marks,axis=0))

data = np.array([10, 20, 30, 40, 50])
print(np.mean(data))
print(np.median(data))
print(np.min(data))
print(np.max(data))
print(np.std(data))

sales = np.array([
    [100, 120, 150, 130],
    [200, 180, 220, 250],
    [80,  90,  100, 110]
])

print(np.sum(sales))

print(np.sum(sales,axis=1))
print(np.sum(sales,axis=0))
print(np.average(sales,axis=1))
print(np.argmax(sales))


sales = np.array([
    [1200, 1500, 1100],
    [1800, 1700, 1900],
    [900,  1200, 1000],
    [2200, 2100, 2300]
])
print(np.sum(sales,axis=1))
print(np.average(sales,axis=1))
print(np.sum(sales,axis=0))
print(np.average(sales,axis=0))
prod_totals = np.sum(sales,axis=1)
print(np.argmax(prod_totals))





