# Newton's Divided Difference Interpolation
# Qasid Ahmed Aleem
# Date: 27 March 2018
import numpy as np

def calculate_coefficients(x, y):
    """
    Calculate the coefficients for Newton's Divided Difference Interpolation.

    Parameters:
    - x: array of data points
    - y: array of f(x)

    Returns:
    - array of coefficients
    """
    n = len(x)
    a = [y[i] for i in range(n)]

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i] - a[i-1]) / float(x[i] - x[i-j])

    return np.array(a)

def evaluate_interpolation(coefficients, x, r):
    """
    Evaluate the Newton's Divided Difference Interpolation.

    Parameters:
    - coefficients: array of coefficients
    - x: array of data points
    - r: value of x for interpolation

    Returns:
    - interpolated y value
    """
    n = len(coefficients) - 1
    temp = coefficients[n]

    for i in range(n - 1, -1, -1):
        temp = temp * (r - x[i]) + coefficients[i]

    return temp

# Given data points
x = [1.0, 1.3, 1.6, 1.9, 2.2]
y = [0.7661977, 0.6200860, 0.4554022, 0.2818186, 0.1103623]

# User input for the value of x to be interpolated
quest = float(input("Enter the value of x: "))

# Calculate coefficients and evaluate interpolation
coefficients = calculate_coefficients(x, y)
result = evaluate_interpolation(coefficients, x, quest)

# Display the interpolated result
print("f(x) = {:12.10f} at x = {:12.10f}".format(result, quest))
