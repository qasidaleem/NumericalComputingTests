print("the given Equations...")
print(" 6x-2y+z=11")
print("-2x+7y+2z=5")
print(" x+2y-5z=-1\n")

x1=0
x2=0
x3=0

print("First Method")
print("{:^15s}{:^15s}{:^15s}".format("x1","x2","x3"))
for i in range(0,10):
	print("{: 15.12f}{: 15.12f}{: 15.12f}".format(x1,x2,x3))
	a=(11+(2*x2)-x3)/6
	b=(5+(2*x1)-(2*x3))/7
	c=(1+x1+(2*x2))/5
	
	x1=a
	x2=b
	x3=c

print("x1={} x2={} x3={} after {} iterations".format(x1,x2,x3,i))

x1=0
x2=0
x3=0

print("\n\n\nSecond method")
print("{:^15s}{:^15s}{:^15s}".format("x1","x2","x3"))
for i in range(0,10):
	print("{: 15.12f}{: 15.12f}{: 15.12f}".format(x1,x2,x3))
	x1=(11+(2*x2)-x3)/6
	x2=(5+(2*x1)-(2*x3))/7
	x3=(1+x1+(2*x2))/5

	
	
print("\nx1={} x2={} x3={} after {} iterations".format(x1,x2,x3,i))
