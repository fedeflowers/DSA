
import random
from collections import deque

class Cell:
	#can be hidden or not
	def __init__(self, value):
		self.value = value
		self.hidden = True

	def unhide(self):
		self.hidden = False

	def plusone(self):
		self.value += 1

class MineSweeper:
	# get better at placing mines:
	#  Steps
	# 	Create a list of all possible cell coordinates.
	# 	Use random.shuffle() to randomly order them.
	# 	Take the first k elements of that list as the mine positions.

	def __init__(self, row, col, mines):
		'''
		row : row number
		col : col number
		mines : number of mines in the field
		'''
		#assume that input is already checked
	def click(self, row, col):
		if self.field[row][col].value == 9:
			print("LOST")
			return

		#bfs uncover free cells
		directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		q = deque([(row, col)])
		self.unhidden.add((row, col))
		self.field[row][col].unhide()
		while q:
			r, c = q.popleft()
			for x, y in directions:
				new_x = x + r
				new_y = y + c
				if 0 <= new_x < self.row and 0 <= new_y < self.col and (new_x, new_y) not in self.unhidden and self.field[new_x][new_y].value != 9:
					self.unhidden.add((new_x, new_y))
					self.field[new_x][new_y].unhide()
					if self.field[new_x][new_y].value == 0:
						q.append((new_x, new_y))




	def _add_1_adj(self, r, c):
		directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
		for x, y in directions:
			new_x = x + r
			new_y = y + c
			if 0 <= new_x < self.row and 0 <= new_y < self.col:
				if self.field[new_x][new_y].value != 9:
					self.field[new_x][new_y].plusone()
	
	def debug_printMatrix(self):
		matrix = []
		for i in range(self.row):
			print_row = []
			for j in range(self.col):
				print_row.append(self.field[i][j].value)
			matrix.append(print_row)

		for row in matrix:
			print(row)

	def printMatrix(self):
		matrix = []
		for i in range(self.row):
			print_row = []
			for j in range(self.col):
				if self.field[i][j].hidden:
					print_row.append("?")
				elif self.field[i][j].value == 0:
					print_row.append("-")
				else:
					print_row.append(str(self.field[i][j].value))
			matrix.append(print_row)

		for row in matrix:
			print(row)


ms = MineSweeper(7, 5, 2)
ms.click(1,1)

ms.debug_printMatrix()
print("__________________________")
ms.printMatrix()