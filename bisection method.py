def fun_c(f):
	return  (f**3)+f-5
d=int(input("How many iterations are needed?: "))
a=1
b=2
for x in range(0,d):
	 if fun_c(a)*fun_c(b)<0:
		 m=(a+b)/2
		 print(x,a,b,fun_c(a),fun_c(b), m)
		 if fun_c(a)*fun_c(m)<0:
			 b=m
		 else:
			 a=m
