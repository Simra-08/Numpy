# # # -------------------- DAY 4 ----------------------


import numpy as np

a = np.array([10, 20, 30, 40, 50])
print(a+5)
print(a*3)

a = np.array([2, 4, 6, 8])
b = np.array([1, 2, 3, 4])
print(a+b)
print(a-b)
print(a*b)
print(a/b)

marks = np.array([45, 60, 72, 81, 90])
print(marks+5)

prices = np.array([100, 250, 500, 750, 1000])
new_prices = prices * 1 + 15/100
print(new_prices)

celsius = np.array([0, 10, 20, 30, 40])
fahrenheit = celsius * 9/5 + 32
print(fahrenheit)

numbers = np.array([2, 5, 8, 10])
print(np.sqrt(numbers))

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr.shape)
print(arr+5)

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

bonus = np.array([1, 2, 3])
print(arr.shape)
print(bonus.shape)
print(arr+bonus)

marks = np.array([
    [80, 70, 90],
    [60, 85, 75],
    [95, 88, 92]
])

bonus = np.array([5, 2, 3])
print(marks+bonus)

height = np.array([150, 160, 165, 170, 180])
metres = height/100
print(metres)

salary = np.array([30000, 40000, 50000, 60000])
new_salary = salary * 1 + 10 / 100
print(new_salary)

sales = np.array([
    [100, 200, 300],
    [150, 250, 350],
    [200, 300, 400]
])
fee = np.array([10, 20, 30])
print(sales.shape)
print(fee.shape)
print(sales+fee)

temperatures = np.array([25, 30, 35, 40, 45])
new_temp = temperatures>35
print(temperatures[temperatures>35])
print(new_temp)

prices = np.array([100, 200, 300, 400, 500])
new_prices = prices * 1 + 10 /100
new_prices = new_prices + 50
new = new_prices>300
print(new_prices)
print(new)


import numpy as np

prices = np.array([250, 400, 550, 800, 1200])
new_prices = prices * 1 - (20/100)
print(new_prices)

marks = np.array([45, 62, 78, 81, 95])
print((marks+5)*1.05)

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 78]
])
bonus = np.array([5, 3, 10])
print(marks+bonus)

sales = np.array([
    [1000, 1200, 1500, 1800],
    [800,  900,  1100, 1300],
    [1500, 1700, 1900, 2200]
])
rate = np.array([[0.10], [0.15], [0.20]])
print(sales.shape)
print(rate.shape)

broadcasting
(2,2) and (2,) - yes
(2,3) and (3,)  - no
(2,3) and (1,3) - yes
(2,) - means 2 elements eg - [1,4]
