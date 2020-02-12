#primality check

def prime(x):
	#x=int(input('number: '))

	c=[]

	for d in range(1,x+1):#el +1 es para que considere a el mismo
		if x % d == 0:
			c.append(d)
			#print(d) para imprimir a medida que va recorriendo
			d=d+1

	return len(c)

x=int(input('number: '))


if prime(x) > 2 or prime(x)==1:
	print('no es primo')

else:
	print('es primo')
