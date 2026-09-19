# ------------------------------ DAY 6 ---------------------------------------------
# Description :Practiced Boolean indexing and conditional operations in NumPy. 
# Learned how to create Boolean masks using comparison operators, 
# filter 1D and 2D arrays based on conditions,
#  combine multiple conditions using & and |, and use np.where() for 
# conditional value replacement and classification.
#  Also practiced applying aggregation functions such as sum, 
# average, max, and min to filtered data using a larger sales dataset.


import numpy as np

sales = np.array([
    [120, 250, 180, 300],
    [150, 220, 310, 170],
    [90, 140, 200, 280]
])
print(sales[sales>200])
print(sales[sales<150])
print((np.sum(sales>200)))
print(sales[(sales>150) & (sales<300)])
print(sales[(sales<120) | (sales>280)])

final_sales = np.where(sales>250,"High","Normal")
print(final_sales)

final_sales = sales[sales>200]
print(np.sum(final_sales))


final_sales = sales[sales>200]
print(np.average(final_sales))

import numpy as np

sales = np.array([
    [120, 250, 180, 300],
    [150, 220, 310, 170],
    [90, 140, 200, 280]
])

print(np.sum(sales<200))
print(np.sum(sales[sales<200]))

final_sales = sales[sales>=200]
print(np.average(final_sales))

print(sales[(sales>=150) & (sales<=250)])

print(sales[(sales>250)|(sales==250)])

print(np.where(sales<150,0,sales))

print(np.where(sales>=250,"High","Normal"))

print(np.where(sales>250,sales*0.9,sales))

final_sales = (sales[sales>200])
print(np.max(final_sales))

final_sales = sales[(sales>150) & (sales<300)]
print(np.average(final_sales))

import numpy as np

sales = np.array([
    [1250, 1840, 920, 2310, 1560, 2890, 1340, 1750, 2100, 980],
    [1620, 2450, 1180, 3050, 1920, 2210, 870, 2640, 1530, 1990],
    [980, 1340, 2750, 1890, 3120, 1450, 1680, 2290, 940, 2570],
    [2140, 1760, 1230, 2980, 1850, 3420, 1560, 2070, 1190, 2710],
    [1480, 2360, 910, 2640, 1970, 3180, 1320, 1840, 2510, 1430],
    [1890, 2750, 1540, 2210, 960, 3070, 1680, 2450, 1390, 2860],
    [1120, 1980, 2670, 1450, 2340, 3190, 1780, 920, 2560, 2010],
    [2410, 1530, 1870, 2980, 1260, 2760, 1640, 2190, 1030, 3350],
    [1360, 2290, 1740, 3100, 890, 2480, 1950, 1420, 2870, 2180],
    [2050, 1180, 2630, 1760, 3240, 1510, 2320, 970, 2790, 1860],
    [1570, 2890, 1320, 2450, 1990, 3060, 1140, 2210, 2680, 1750],
    [930, 2140, 2860, 1630, 2380, 2970, 1450, 1820, 3150, 1270]
])

final_sales = [sales>2000]
print(np.sum(final_sales))

final_sales = sales[sales>2000]
print(np.sum(final_sales))

final_sales = sales[sales>2000]
print(np.average(final_sales))

print(np.where(sales>2000,"successful","unsuccessful"))


print(np.where(sales>2000,sales,0))


final_sales = sales[sales>2000]
print(np.max(final_sales))

final_sales = sales[sales>2000]
print(np.min(final_sales))

final_sales = [sales<2000]
print(np.sum(final_sales))

final_sales = [sales>2000]
suc = (np.sum(final_sales))
tot = np.sum(sales>0)


print((suc/tot)*100)

final_sales = sales[sales<2000]
print(np.sum(final_sales))