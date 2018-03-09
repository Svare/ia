class Lapiz:
	color = 'amarillo'

	def color(self):
		print('soy lapiz')
	def laPolla(self):
		return self.color


def main():
	bic = Lapiz()
	bic.color()
	halo = bic.laPolla()
	print(halo)

if __name__ == '__main__':
	main()