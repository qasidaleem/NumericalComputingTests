quest=int(input("what is the highest power of x: "))
coefficents=[]
qs=[]
es=[]
qsn=[]
esn=[]
for i in range(0,quest+1):
	
	coefficent=float(input("Enter the coefficent of x^{}: ".format(i)))
	coefficents.append(coefficent)
coefficents.reverse()
d=int(input("How many iterations are required: "))
for s in range(0,quest+1):
	print("{:^14s}".format("e"+str(s),"q"+str(s)),end=" ")
	if s==4:
		break
	print("{:^14s}".format("q"+str(s)),end=" ")
print(" ")
for i in range(0,quest):
	if i==0:
		qsi=(-coefficents[1]/coefficents[0])
		qs.append(qsi)
	else:
		qsi=0
		qs.append(qsi)
for s in range(0,quest):
	print("{:15s}{: 14.12f}".format(" ",qs[s]),end=" ")
print(" ")
			
	
for i in range(0,quest+1):
	if i==0 or i==quest:
		esi=0
		es.append(esi)
	else:
		esi=coefficents[i+1]/coefficents[i]
		es.append(esi)
for s in range(0,quest+1):
	print("{: 14.12f}{:15s}".format(es[s]," "),end=" ")
print(" ")

for i in range(0,d):
	for s in range(0,quest):
		qsi=es[s+1]-es[s] +qs[s]
		if i ==0:
			qsn.append(qsi)
		else:
			qsn[s]=qsi
			#qs=qsn
	for s in range(0,quest+1):
		if s==0 or s==quest:
			esi=0
			if i==0:
				esn.append(esi)
			else:
				esn[s]=esi
				
		else:
			esi=(qsn[s]/qsn[s-1])*(es[s])
			if i==0:
				esn.append(esi)
			else:
				esn[s]=esi
				
	es=esn
	qs=qsn
	for s in range(0,quest):
		print("{:15s}{: 14.12f}".format(" ",qsn[s]),end=" ")
	print(" ")
			
	for s in range(0,quest+1):
		print("{: 14.12f}{:15s}".format(esn[s]," "),end=" ")
	print(" ")	
print("The {:2d} approximate roots of the function are".format(quest))
for s in range(0,quest):
	print("{: 18.16}".format(qsn[s]))
