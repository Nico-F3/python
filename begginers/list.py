#list

a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
c=[]
x=int(input('number: '))
for i in range(len(a)):
	if a[i]<x:
		c.append(a[i]) #no hace falta sobre escribir c=c.append()
		
print (c)