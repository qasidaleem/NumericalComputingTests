#Qasid Ahmed Aleem
#Secant Method
def func(f):					#given function 
	return(f**3)+(f**2)-(3*f)-3

def msec(xi,xi1):				#secant function
	return (func(xi1)-func(xi))/(xi1-xi)
	
def newx(xi,xi1):				#new x function
	return xi-(func(xi)/msec(xi,xi1))

xi =1.0 #a
xi1=2.0	
print("{:^10s} {:^18s} {:^18s} {:^19s}{:^18s} {:^19s} {:^21s}".format(
"Counter","x","xi+1","f(x)","f(xi+1)","msec","newx"))
for x in range(0,30):
	
	if xi-xi1==0:
		print("the root is ",xi)
		break
	print("{:^10d} {: 18.16f} {: 18.16f} {: 18.16f} {: 18.16f}\
{: 19.15f} {:21.20f}".format(x,xi,
	xi1,func(xi),func(xi1),msec(xi,xi1),newx(xi,xi1)))
	
	
	xn=xi
	xi=xi1
	
	xi1=newx(xn,xi)
