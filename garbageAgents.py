
# LOPEZ FERNANDEZ SERVANDO MIGUEL
# PACHECO FRANCO JESUS ENRIQUE
# RODRIGUEZ RUIZ JULIO RAUL
# ROMERO HURTADO EDUARDO DAVID


from random import randint

def create_enviroment(rows,columns):
	enviroment = ['0']*rows
	for row in range(rows):
		enviroment[row] = ['0']*columns
	return enviroment

def litter(fila,howMuchGarbage):
	for i in range(howMuchGarbage):
		fila[randint(0,len(fila)-1)] = 'W'

def litter_the_enviroment(enviroment):
	for row in enviroment:
		litter(row,randint(0,5))
	return enviroment

def print_enviroment(enviroment):
	for row in enviroment:
		print(row)

class agent_01:
	def __init__(self,x_pos,y_pos):
		self.x_pos = x_pos
		self.y_pos = y_pos

	def next_move():
		return randint(0,3)

	def move_agent(enviroment):
		enviroment[self.x_pos,self.y_pos] = '*'
		return enviroment

def main():
	rows = int(input('Filas: '))
	columns = int(input('Columnas: '))

	agent = agent_01(0,0)

	enviroment = litter_the_enviroment(create_enviroment(rows,columns))
	print_enviroment(enviroment)

	enviroment = agent.move_agent(enviroment)


if __name__ == '__main__':
	main()
