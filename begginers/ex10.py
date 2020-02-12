#combine exercise 5 and 7
#[EXPRESSION FOR_LOOPS CONDITIONALS]
#A set object is an unordered collection of distinct hashable objects. 
#Common uses include membership testing, removing duplicates from a sequence, 
#and computing mathematical operations such as intersection, union, difference, 
#and symmetric difference.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


#a=set(a)#elimino los duplicados
#b=set(b)#elimino los duplicados
#las de above nohacen falta

c=[i for i in set(a) for k in set(b) if i==k]

print(c)