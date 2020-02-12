#guess the number
#The user will search for a number and try to guess it
#random list

import random

a = random.randint(1, 9)



x=input('which number do you think I choiche between 1 and 9: ')
c=1
while x!='exit':
	x=int(x)
	if x==a:
		print ('you are damn right, in your {} attempt'. format(c))
		c=c+1

		break

	else:
		x=input('try again ')
		c=c+1

else:	
	print('loser')



	#elif x>=a:
	#	print('to high, it was', a)
	#	break

	#elif x<=a:
	#	print('to low, it was', a)
	#	break

	


