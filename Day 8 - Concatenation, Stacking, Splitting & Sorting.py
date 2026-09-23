# ---------------------- DAY 8 ----------------------------------


import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])
print(np.concatenate((a,b)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.vstack((a,b)))

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(np.hstack((a,b)))

sales = np.array([100, 200, 300, 400, 500, 600])
print(np.split(sales,3))

scores = np.array([72, 91, 45, 88, 63, 95])
print(np.sort(scores))

sales = np.array([120, 250, 180, 310, 150, 400])
sales_final = sales[sales>200]
print(sales_final)

products = np.array([
    101, 102, 101, 103, 102,
    104, 103, 101, 105, 104
])
print(np.unique(products))

products = np.array([
    101, 102, 101, 103, 102,
    104, 103, 101, 105, 104
])

sales, values = np.unique(products, return_counts=True)
print(sales)
print(values)

week1 = np.array([120, 150, 200, 180, 220])
week2 = np.array([190, 250, 210, 300, 170])
week3 = (np.concatenate((week1,week2)))
print(np.sort(week3))

final_values = week3[week3>200]
print(final_values)
sales, values = np.unique(week3, return_counts=True)
print(sales)
print(values)

print(np.average(week3))