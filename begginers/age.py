#In this excersice I will ask the users the name and age
age = 0

n = input('Hello, how should I call you ? ' )

x = input('hello {} how old are you? '. format(n)) #place the variable n where the {} are

#(or, if you want to be more compact with your code)

#x = int(input("Enter your age: "))


#x = input('hello', n ,'how old are you? ') no funciona porque input toma un argumento

y=int(x) #change the variable from str() to int()
 
c=y #keep the initial value of y

while y < 100:
	y=y+1
	age= y-c-1
print ('you will turn 100 in', age+2020)

#print ('you look younger than', x)

#----------------------------------------------------------------------

solution:

name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2020 - age)+100)
print(name + " will be 100 years old in the year " + year)

