#paperscissorrock

x='yes'
y='yes'

#player1=input('select your weapon player1 ')
#player2=input('select your weapon player2 ')

while x=='yes' and y=='yes':
	player1=input('select your weapon player1 ')
	player2=input('select your weapon player2 ')

	if player1=='scissors' and player2=='paper' or player1=='paper' and player2=='rock' or player1=='rock' and player2=='scissors':
		print('gano player1')
		
		x=input('player1 queres jugar otra vez? ')
		y=input('player2 queres jugar otra vez? ')

	elif player2=='scissors' and player1=='paper' or player2=='paper' and player1=='rock' or player2=='rock' and player1=='scissors':
		print('gano player2')
		x=input('player1 queres jugar otra vez? ')
		y=input('player2 queres jugar otra vez? ')

else:
	print('gracias por participar')