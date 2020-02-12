# cow or bull

if __name__=="__main__":


	import random
	#a = random.randint(1000, 9999)
	
	
	a=random.sample(range(1, 10), 4) 
	#for i in range(1000,9999):
	#print (a)
	b=input('give a four digit number: ')
		
	
	i=0
	l = [int(x) for x in str(b)]



	#print(l)
	#print(len(a))
	
	#j=0
	#i=0
	n=1
	while a!=l:
		c=0
		d=0
		for i in range(len(a)):

	#while i <len(a):
			for j in range(len(l)):
				if a[i]==l[j] and i==j:
					c=c+1

				elif a[i]==l[j] and i!=j:
					d=d+1

				elif l.count(l[j])>2:
					d=d-1

		print(c,'cows',d,'bulls')
		b=input('try again: ')
		l = [int(x) for x in str(b)]	
		n=n+1
	
		

	print('you did it in your',n,'time')	
	
		
