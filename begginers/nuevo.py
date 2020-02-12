#new list with the first and last element of a list

#a = [5, 10, 15, 20, 25]
a=input('me a list: ' )


def nueva(a):
	a=a.split()	#Split a string into a list where each word is a list item
	new=[]

	new.append(a[0])
	new.append(a[len(a)-1])
	return new


print(nueva(a))