from math import factorial as fac
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
deg=int(input("Input the order of the curve:"))
for i in range(0,deg+1):
	xu=int(input("Enter the {:2s} cordinate:".format("x"+str(i))))
	yu=int(input("Enter the {:2s} cordinate:".format("y"+str(i))))
	y.append(yu)
	x.append(xu)
def comb(n,k):
	y=fac(n)/(fac(n-k)*fac(k))
	return y

def binom(x,y,n):
	mat=[]
	for i in range(0,n+1):
		
		d=comb(n,i)*(x**(n-i))*(y**i)
		
		mat.append(d)
	return mat

def bezier(point,n):
	bez=[]
	m=0
	for i in np.linspace(0.0,1.0,num=100):
		
		m=0
		for r in range(0,n+1):
			k=binom(1-i,i,n)
			
			
			m+=k[r]*point[r]
			
		bez.append(m)
			
		
	return bez

b1=(bezier(x,deg))
b2=(bezier(y,deg))


plt.plot(b1,b2,'-')
plt.gca().invert_yaxis()
plt.grid(1)
plt.show()
