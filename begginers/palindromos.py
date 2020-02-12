#Ask the user for a string and print out whether 
#this string is a palindrome or not. 
#(A palindrome is a string that reads the same forwards and backwards.)


x=str(input('give a word: '))

x=list(x)

#x[:len(x)//2]#from the first position to the half of the list

y=x[:len(x)//2]

a=x[::-1]#reverse the list

b=a[:len(a)//2]
i=0
c=0
for i in range(len(y)):
	if y[i]==a[i]:
		c=i+1


	else:	
		print ('not palindrome')	
		break


if c==len(y):
	print('palindrome')
print (x,a,b,y)


#---------------------------------------
#wrd=input("Please enter a word")
#wrd=str(wrd)
#rvs=wrd[::-1]
#print(rvs)
#if wrd == rvs:
#    print("This word is a palindrome")
#else:
#    print("This word is not a palindrome")

#---------------------------------------

#def reverse(word):
#	x = ''
#	for i in range(len(word)):
#		x += word[len(word)-1-i]
#		return x

#word = input('give me a word:\n')
#x = reverse(word)
#if x == word:
#	print('This is a Palindrome')
#else:
#	print('This is NOT a Palindrome')
