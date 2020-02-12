#List 

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



c=[]
for i in range(len(a)-1):#If i do not add the -1 the variable i is going out of range
	if a.count(a[i]) >= 2: 
		a.remove(a[i])

	else:
		i+1
	
print(a)


for j in range(len(b)-1):
	if b.count(b[j]) >= 2: 
		b.remove(b[j])

	else:
		j+1


print (b)
i=0
j=0


if len (a) < len (b):

	while a[i] in b:
		c.append(a[i])
		i=i+1
	else:
		i=i+1

elif len (b) < len (a):
	while b[j] in a:
		c.append(b[j])
		j=j+1
	else:
		j=j+1

elif len (b) == len (a):
	while b[j] in a:
		c.append(b[j])
		j=j+1
	else:
		j=j+1

print(c)


#Python | set() method to generate randmon numbers

