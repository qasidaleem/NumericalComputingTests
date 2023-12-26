import numpy as np

def coef(x, y):
    #x : array of data points
    #y : array of f(x)
    
    n = len(x)
    a = []
    for i in range(n):
        a.append(y[i])

    for j in range(1, n):

        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(x[i]-x[i-j])

    return np.array(a) # return an array of coefficient

def Eval(a, x, r):


   
   n = len( a ) - 1
   temp = a[n]
   for i in range( n - 1, -1, -1 ):
        temp = temp * ( r - x[i] ) + a[i]
   return temp # return the y_value interpolation


x=[1.0,1.3,1.6,1.9,2.2]
y=[0.7661977,0.6200860,0.4554022,0.2818186,0.1103623]
quest=float(input("Enter the value of x: "))

print("f(x)={: 12.10f} at x={:12.10f}".format(Eval(coef(x,y),x,quest)\
,quest))
