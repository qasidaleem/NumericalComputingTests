from math import sin,exp

def func(f):
	#return (3*f) + sin(f) - exp(f)
	return (f**3) -(2*(f**2)) -5
x0=float(input("Enter the first approximation of x:"))
x1=float(input("Enter the second approximation of x: "))
x2=float(input("Enter the third approximation of x: "))

approx1=[x0,x1,x2]
approx1.sort()
x4=0
def a1(g,f0,f1,f2,h1):
	return ((g*f2)+(f0)-(f1*(1+g)))/((g*(h1**2))*(1+g))

def b1(f1,f2,h1,a1):
	return (f2-f1-(a1*(h1**2)))/h1

def x_newm(a,b,c,x1):
	return x1-((2*c)/(b -(((b**2)-(4*a*c))**0.5)))
def x_newp(a,b,c,x1):
	return x1-((2*c)/(b +(((b**2)-(4*a*c))**0.5)))	

print("{:^13s} {:^13s} {:^13s} {:^13s} {:^13s} {:^13s} {:^13s} {:^13s} \
{:^13s} {:^13s} {:^13s} {:^13s}".format("x2","x0","x1","f2","f0","f1",\
"h1","h2","gamma","a","b","x_new"))
for i in range(0,100):
	h1=approx1[2]-approx1[1]
	h2=approx1[1]-approx1[0]
	
	g=h2/h1
	
	a=a1(g,func(approx1[0]),func(approx1[1]),func(approx1[2]),h1)
	b=b1(func(approx1[1]),func(approx1[2]),h1,a)
	c=func(approx1[1])
	
	if b>0:
		x3=x_newp(a,b,c,approx1[1])
	else:
		x3=x_newm(a,b,c,approx1[1])
	
	if x4==x3:
		break
	#print(x3)
	approx1.append(x3)
	approx1.sort()
	del approx1[3]
	#print (approx1)
	x4=x3
	print("{:13.10f} {: 13.10f} {: 13.10f} {: 13.10f} {: 13.10f} \
{: 13.10f} {: 13.10f} {: 13.10f} {: 14.10f} {: 13.10f} {: 13.10f} \
{: 13.10f}".format(approx1[0],approx1[1],approx1[2],func(approx1[0]),\
func(approx1[1]),func(approx1[2]),h1,h2,g,a,b,x3))
	#print(x4)
	
print("the approximate root after {:1d} iterations is {:36.34f} ".\
format(i,x3))
