from math import factorial
import numpy as np
x=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4]
y=[3.1,4.9,6.2,7.5,8.9,11.2,10.1,7.3]
s=0
quest=float(input("Enter the value of x: "))
for i in range(0,len(x)-1):
     if quest>=x[i] and quest<=x[i+1]:
         h=x[i+1]-x[i]
         m=(x[i-1]+x[i+2])/2
         
         m1=(x[i]+x[i+3])/2
         
         if abs(quest-m) <abs(quest-m1):
             s=(quest-x[i-1])/h
             y1=[]
             for t in range(0,4):
                 y1.append(y[i-1+t])    
         elif abs(quest-m) >abs(quest-m1):
             
             s=(quest-x[i])/h
             y1=[]
             for t in range(0,4):
				 
                 y1.append(y[i+t])
                 
         
		

def coef(y):
    n=len(y)
    a=[]
    
    for i in range(n):
        a.append(y[i])
        
    for j in range(1,n):
        
        for i in range(n-1,j-1,-1):
            a[i]=float(a[i]-a[i-1])
    return np.array(a)

def Eval(a,s):
    
    n=len(a)-1
    f=n
    
    temp=0
    
    
    for i in range(n,-1,-1):
        y0=1
        for j in range(0,f):
            
            y0=(s-j)*y0
            
            
            
            
        temp=(y0*(a[i]))/factorial(i)+temp 
        
        f=f-1
    return temp

print("f(x) = {:12.10f} at x ={:5.2}".format(Eval(coef(y1),s),quest))

