
def left_distance(cadenas,pos_x):
	i = pos_x-1
	if pos_x == 0:
			return -1
	while True:
		if cadenas[i] == 'B':
			return -(pos_x-i)
		if i == 0:
			return -2
		i = i -1

def right_distance(cadenas,pos_x):
	i = pos_x+1
	if pos_x == len(cadenas)-1:
			return -1 # No puedo ir a la derecha
	while True:
		if cadenas[i] == 'B':
			return i-pos_x
		if i == len(cadenas)-1:
			return -2
		i = i +1


def up_distance(cadenas,pos_y):
	i = pos_y-1
	if pos_y == 0:
			return -1
	while True:
		if cadenas[i] == 'B':
			return -(pos_y-i)
		if i == 0:
			return -2
		i = i -1

def down_distance(cadenas,pos_y):
	i = pos_y+1
	if pos_y == len(cadenas)-1:
			return -1 # No puedo ir a la derecha
	while True:
		if cadenas[i] == 'B':
			return i-pos_x
		if i == len(cadenas)-1:
			return -2
		i = i +1

def main():
	cadenas = ['B','0','*','B','B']
	pos = left_distance(cadenas,2)
	adelante = right_distance(cadenas,2)
	print(pos)
	print(adelante)


if __name__ == '__main__':
	main()
