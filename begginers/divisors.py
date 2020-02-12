#all divisors

def prime(x):
	x=int(input('number: '))

	c=[]

	for d in range(1,x+1):#el +1 es para que considere a el mismo
		if x % d == 0:
			c.append(d)
			#print(d) para imprimir a medida que va recorriendo
			d=d+1

	print(c)




#---------------------------------------------------------------

num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)