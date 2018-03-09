
# LOPEZ FERNANDEZ SERVANDO MIGUEL
# PACHECO FRANCO JESUS ENRIQUE
# RODRIGUEZ RUIZ JULIO RAUL
# ROMERO HURTADO EDUARDO DAVID


from random import randint

import os

def create_enviroment(rows,columns):
	
	''' Crea una lista de listas inicializadas en ceros
		la cual va a simular el ambiente de los agentes

		Parámetros:

		rows -> entero, número de filas del ambiente
		columns -> entero, número de columnas del ambiente

		Retorna: lista '''

	enviroment = ['0']*rows
	for row in range(rows):
		enviroment[row] = ['0']*columns
	return enviroment

def litter(fila,how_much_garbage):

	''' Inserta basura en posiciones aleatorias de una
		fila

		Parámetros:

		fila -> lista, fila a la que le voy a insertar basura
		how_much_garbage -> entero, cuanta basura quiero
							que genere

		Retorna: None '''

	for i in range(how_much_garbage):
		fila[randint(0,len(fila)-1)] = 'W'

def litter_the_enviroment(enviroment):

	''' Coloca basura en todo el ambiente

		Parámetros:

		enviroment -> lista, es una lista de listas que 
						representa el ambiente de los
						agentes

		Retorna: lista '''

	for row in enviroment:
		litter(row,randint(0,5))
	return enviroment

def print_enviroment(enviroment):

	''' Imprime en la terminal el ambiente

		Parámetros:

		enviroment -> lista, es una lista de listas que 
						representa el ambiente de los
						agentes

		Retorna: None '''

	for row in enviroment:
		print(row)

def main():
	rows = int(input('Filas: '))
	columns = int(input('Columnas: '))

	enviroment = litter_the_enviroment(create_enviroment(rows,columns))
	print_enviroment(enviroment)

#	os.system('clear')


if __name__ == '__main__':
	main()
