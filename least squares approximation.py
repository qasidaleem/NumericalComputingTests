#Least Square's Approximation
#Qasid Ahmed Aleem
#23 April 2018
import matplotlib.pyplot as plt
import numpy as np

x=[2.1,3.5,4.6,5.2,6.3,7.3,9.1]
y=[11.2,14.5,17.3,15.2,12.5,11.0,9.3]

x2=[]
x3=[]
x4=[]
xiyi=[]
xiyi2=[]
print("{:^20}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}{:^15s}".\
format("i","x","y","xi^2","xi^3","xi^4","xiyi","xi^2yi"))
for i in range(0,len(x)):
	xt=x[i]**2
	x2.append(xt)
	xt=x[i]**3
	x3.append(xt)
	xt=x[i]**4
	x4.append(xt)
	xt=x[i]*y[i]
	xiyi.append(xt)
for i in range(0,len(x)):
	xt=x2[i]*y[i]
	xiyi2.append(xt)	

for i in range(0,len(x)):
	print("{:^20d}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}\
{:^15.5f}".format(i,x[i],y[i],x2[i],x3[i],x4[i],xiyi[i],xiyi2[i]))
print("{:<20s}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}{:^15.5f}\
{:^15.5f}".format("Total",sum(x),sum(y),sum(x2),sum(x3),sum(x4)\
,sum(xiyi),sum(xiyi2)))
k1=[sum(x4),sum(x3),sum(x2),sum(xiyi2)]
k2=[sum(x3),sum(x2),sum(x),sum(xiyi)]
k3=[sum(x2),sum(x),len(x),sum(y)]

print("the matrix of the series of equations is thus")
for i in k1:
	print("{:10.5f}".format(i),end=" ")
print("\n")

for i in k2:
	print("{:10.5f}".format(i),end=" ")
print("\n")
for i in k3:
	print("{:10.5f}".format(i),end=" ")
print("\n")
def gauss_j(x,y,z):
	nr1=[1,1,1,1]
	nr2=[1,1,1,1]
	nr3=[1,1,1,1]
	nr4=[1,1,1,1]
	r1=[1,1,1,1]
	r2=[1,1,1,1]
	r3=[1,1,1,1]
	for i in range(0,len(x)):
		
		hit=x[0]
		nr2y=y[i]*hit-(x[i]*y[i-i])
		nr2[i]=nr2y
		
		nr3y=z[i]*hit-(x[i]*z[i-i])
		nr3[i]=nr3y
	y=nr2
	
	
	
	for i in range(0,len(x)):
		hit=y[1]
		nr1y=x[i]*hit-(x[i-i+1]*y[i])
		nr1[i]=nr1y
		
		
		
		nr4y=nr3[i]*hit-(nr2[i]*nr3[1])
		z[i]=nr4y
	
	for i in range(0,len(x)):
		hit=z[2]
		nr1y=nr1[i]*hit-(nr1[2]*z[i])
		r1[i]=nr1y
		
		nr2y=nr2[i]*hit-(nr2[2]*z[i])
		r2[i]=nr2y
	
	for i in range(0,len(x)):
		nr1y=r1[i]/r1[0]
		nr1[i]=nr1y
		nr2y=r2[i]/r2[1]
		nr2[i]=nr2y
		nr3y=z[i]/z[2]
		nr3[i]=nr3y
	
		
	
	
	return nr1,nr2,nr3 #returns 3 lists of the reduced echeleon matrix

a=gauss_j(k1,k2,k3)[0][3]
b=gauss_j(k1,k2,k3)[1][3]
c=gauss_j(k1,k2,k3)[2][3]
print("Applying Gauss Jordan Elimination....")
for i in gauss_j(k1,k2,k3)[0]:
	print("{:10.5f}".format(i),end=" ")
print("\n")
for i in gauss_j(k1,k2,k3)[1]:
	print("{:10.5f}".format(i),end=" ")
print("\n")
for i in gauss_j(k1,k2,k3)[2]:
	print("{:10.5f}".format(i),end=" ")
print("\n")

print("thus a={} b={} c={}".format(a,b,c))
def parabola(xi,x,y,z):
	para1=np.arange(0.0,len(xi),1)
	for i in range(0,len(xi)):
		para1[i]=float((x*(xi[i]**2)) +( y*xi[i]) + z)
	return para1


plt.plot(x,y,'o',label="The Data points")
plt.plot(x,parabola(x,a,b,c),'-', label="The generated Curve")
plt.legend(loc="upper right")
plt.title("Least Squares Approximation")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.grid
plt.show()
