# ----------------- DAY 9 -------------------------------\
# Day 9: NumPy missing-value handling with NaN, detecting and counting missing values, 
# NaN-aware statistical functions, copy vs view, checking array data types, 
# and converting data types using astype().

import numpy as np

marks = np.array([85, 92, np.nan, 76, np.nan, 88])
print(np.isnan(marks))
print(np.sum(np.isnan(marks)))

sales = np.array([100, 200, np.nan, 300, 400, np.nan])
print(np.nanmean(sales))

sales = np.array([
    [100, 200, np.nan],
    [150, np.nan, 300],
    [200, 250, 350]
])
print(np.sum(np.isnan(sales)))
print(np.nanmean(sales))
print(np.nanmax(sales))
print(sales.dtype)

a = np.array([10, 20, 30])

b = a.copy()

b[1] = 99

print(a)
print(b)

a = np.array([10, 20, 30])

b = a.view()

b[1] = 99

print(a)
print(b)

a = np.array([10, 20, 30, 40])

print(a.dtype)
a = a.astype(float)
print(a.dtype)


ages = np.array(["18", "19", "20", "21", "22"])
ages = ages.astype(int)
print(np.nanmean(ages))
print(np.nanmax(ages))
print(np.nanmin(ages))

salary = np.array([
    25000,
    32000,
    np.nan,
    45000,
    38000,
    np.nan,
    52000,
    29000
])

print(np.sum(np.isnan(salary)))
print(np.nanmean(salary))
print(np.nanmax(salary))
print(np.nanmin(salary))

new_salary = salary[salary>35000]
print(new_salary)