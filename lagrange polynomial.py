# Lagrange Polynomial Interpolation
# Qasid Ahmed Aleem
# Date: 27 March 2018

# Given data points
x = [3.2, 2.7, 1.0, 4.8, 5.6]
y = [22.0, 17.8, 14.2, 38.3, 51.7]

# Additional data points (commented out)
# x = [1.2, 1.6, 2.1, 2.9]
# y = [1.46, 2.52, 4.4, 8.8]

# Initialize the result variable
z = 0

# User input for linearity and interpolation parameters
q = input("Is the data linear: ")
quest = float(input("Enter the x value to be found: "))
n = int(input("Enter the degree of the interpolating polynomial: "))

# Sort the data if linear
if q.lower() in ["y", "yes"]:
    x.sort()
    y.sort()

# Display the sorted data
print(x, y)

# Iterate through the data points to find the interval for interpolation
for i in range(0, len(x)-1):
    if quest > x[i] and quest < x[i+1]:
        m = (x[i] + x[i+1]) / 2

        # Check whether to perform forward or backward interpolation
        if (quest - m) < 0:
            x.pop()
            y.pop()

            # Perform forward interpolation
            for i in range(0, n+1):
                p = 1
                for j in range(0, n+1):
                    if j != i:
                        p *= (quest - x[j]) / (x[i] - x[j])
                z += y[i] * p

        else:
            x.reverse()
            y.reverse()
            x.pop()
            y.pop()
            x.reverse()
            y.reverse()

            # Perform backward interpolation
            for i in range(0, n+1):
                p = 1
                for j in range(0, n+1):
                    if j != i:
                        p *= (quest - x[j]) / (x[i] - x[j])
                z += y[i] * p

# Display the interpolated result
print("f(x) = {:12.10f} at x = {:12.10f}".format(z, quest))
