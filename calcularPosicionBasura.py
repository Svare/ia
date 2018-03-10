
def left_distance(cadenas,pos_x,pos_y):
	i = pos_y-1
	if pos_y == 0:
			return -1 # No puedo ir a la izquierda
	while True:
		if cadenas[pos_x][i] == 'B':
			return -(pos_y-i) # Sumo este numero en X y encuentro basura
		if i == 0:
			return -2 # Puedo ir a la izquierda pero no hay basura
		i = i -1

def right_distance(cadenas,pos_x,pos_y):
	i = pos_y+1
	if pos_y == len(cadenas[0])-1:
			return -1 # No puedo ir a la derecha
	while True:
		if cadenas[pos_x][i] == 'B':
			return i-pos_y
		if i == len(cadenas[0])-1:
			return -2
		i = i +1


def up_distance(cadenas,pos_x,pos_y):
	i = pos_x-1
	if pos_x == 0:
			return -1 # No puedo ir arriba
	while True:
		if cadenas[i][pos_y] == 'B':
			return -(pos_x-i)
		if i == 0:
			return -2
		i = i -1

def down_distance(cadenas,pos_x,pos_y):
	i = pos_x+1
	if pos_x == len(cadenas)-1:
			return -1 # No puedo ir abajo
	while True:
		if cadenas[i][pos_y] == 'B':
			return i-pos_x
		if i == len(cadenas)-1:
			return -2
		i = i +1

def main():
	cadenas = [['0','0','B','*'],['B','B','0','0'],['B','0','0','B'],['B','0','0','0']]
	left = down_distance(cadenas,3,3)

	print(left)
	


if __name__ == '__main__':
	main()
