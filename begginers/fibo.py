#fibonacci sequence


a=int(input('how many fibonacci round would you like ? '))

def rib(a):

	i=0
 
	j, y=0, 1

	c=[]
	while i < a:
		#print(j)
		c.append(j) 
		j, y = y, j+y
		i=i+1

	return c
	
	



print (rib(a))
	

