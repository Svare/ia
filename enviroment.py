class Enviroment:
	enviroment_area = []
	rows = 0
	columns = 0

	def __init__(self,rows,columns):
		self.rows = rows
		self.columns = columns
		self.enviroment_area = [0]*columns

		for column in range(columns):
			self.enviroment_area[column] = [0]*rows


