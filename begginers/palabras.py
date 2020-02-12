#strings

a=input('give me a sentence: ')

a=a.split()

opposite=a[::-1]

#for i in opposite:
#	print(i,  end=' ')


print (' '.join(i for i in opposite))# this let me print the string as a sentence