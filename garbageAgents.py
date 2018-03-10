
# LOPEZ FERNANDEZ SERVANDO MIGUEL
# PACHECO FRANCO JESUS ENRIQUE
# RODRIGUEZ RUIZ JULIO RAUL
# ROMERO HURTADO EDUARDO DAVID


from random import randint

class Agent:

	directions = ('N','S','E','O')
	

	def __init__(self, symbol='*',name='Robotina', x_pos=0, y_pos=0, orientation=0):
		self.symbol = symbol 
		self.name = name
		self.x_pos = x_pos
		self.y_pos = y_pos
		orientation = 0 if orientation > 3 else orientation
		self.orientation = directions[orientation]


	def collision(self, environment):
		pass

	def take_garbage(self, )





if __name__ == '__main__':
	main()
