x=[3.2,2.7,1.0,4.8,5.6]
y=[22.0,17.8,14.2,38.3,51.7]

#x=[1.2,1.6,2.1,2.9]
#y=[1.46,2.52,4.4,8.8]
z=0
q=input("Is the data linear: ")
quest=float(input("Enter the x value to be found: "))
n=int(input("Enter the degree of the interpolating polynomial: "))

if q=="y" or q=="Y" or q=="yes":
	x.sort()
	y.sort()
print(x,y)
for i in range(0,len(x)-1):
	if quest > x[i] and quest <x[i+1]:
		m=(x[i] +x[i+1])/2
		
		if (quest-m)<0:
			x.pop()
			y.pop()
			
			for i in range(0,n+1):
				p=1
					
				for j in range(0,n+1):
					if j!=i:
						p *= (quest-x[j])/(x[i]-x[j])
						
				z+=y[i]*p
							
		else:
			x.reverse()
			y.reverse()
			x.pop()
			y.pop()
			x.reverse()
			y.reverse()
			
			for i in range(0,n+1):
				p=1
				
				
				for j in range(0,n+1):
					if j!=i:
						p *= (quest-x[j])/(x[i]-x[j])
		
				z+=y[i]*p
print("f(x)={: 12.10f} at x={:12.10f}".format(z,quest)) 
