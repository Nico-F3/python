#for x in range(0, 3):
 #   print("We're on time %d" % (x))

#for x in range(1, 11):
 #   for y in range(1, 11):
  #      print('%d * %d = %d' % (x, y, x*y))

#for x in range(3):
 #   print(x)
#else:
 #   print('Final x = %d' % (x))

#collection = ['hey', 5, 'd']
#for x in collection:
 #   print(x)

#list_of_lists = [ [1, 2, 3], [4, 5, 6], [7, 8, 9]]
#for list in list_of_lists:
#    for x in list:
#        print(x)


#for y in range(10):
#	print ('y')

#mydata = input('Prompt :')# interacts with the user, you run and then write something and print it
#print (mydata)


#n = input("Please enter 'hello':")
#while n.strip() != 'hello':
#    n = input("Please enter 'hello':")


#while True:#les waisteful
#	n = input("Please enter 'hello':")
#	if n.strip() == 'hello':
#			break

list = []
length = 4
while len(list) < length:
	number=input('enter a number :')
	try: #The try block lets you test a block of code for errors.                
		n=float(number)		
		list.append(n)
		print (list)
	except ValueError: #The except block lets you handle the error.
		n=str(number)
		print(n,'is not a number')
print ('thank you')
print (list)
	
	
