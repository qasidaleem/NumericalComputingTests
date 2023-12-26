# Qasdi Ahmed Aleem
# Date: 3 April 2018
# Newton's Forward Difference Interpolation

# Importing necessary libraries
from math import factorial
import numpy as np

# Given data points
x = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
y = [3.1, 4.9, 6.2, 7.5, 8.9, 11.2, 10.1, 7.3]

# Initializing variables
s = 0

# User input for the value of x
quest = float(input("Enter the value of x: "))

# Finding the interval for the input value
for i in range(0, len(x)-1):
    if quest >= x[i] and quest <= x[i+1]:
        # Calculating interval width, midpoints, and selecting interpolation points
        h = x[i+1] - x[i]
        m = (x[i-1] + x[i+2]) / 2
        m1 = (x[i] + x[i+3]) / 2
        if abs(quest - m) < abs(quest - m1):
            s = (quest - x[i-1]) / h
            y1 = [y[i-1+t] for t in range(0, 4)]
        elif abs(quest - m) > abs(quest - m1):
            s = (quest - x[i]) / h
            y1 = [y[i+t] for t in range(0, 4)]

# Function to calculate divided differences
def coef(y):
    n = len(y)
    a = [y[i] for i in range(n)]
    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1])
    return np.array(a)

# Function to evaluate the interpolated polynomial
def Eval(a, s):
    n = len(a) - 1
    f = n
    temp = 0
    for i in range(n, -1, -1):
        # Calculating interpolated polynomial using Newton-Gregory forward difference formula
        y0 = 1
        for j in range(0, f):
            y0 = (s - j) * y0

        temp = (y0 * (a[i])) / factorial(i) + temp

        f = f - 1

    return temp

# Displaying the result
print("f(x) = {:12.10f} at x ={:5.2}".format(Eval(coef(y1), s), quest))
