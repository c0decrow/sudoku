import time

def dis_board(sudoku):

        print('''
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[0][0],'''   |   ''',sudoku[0][1],'''   |   ''',sudoku[0][2],'''   ||   ''',sudoku[0][3],'''   |   ''',sudoku[0][4],'''   |   ''',sudoku[0][5],'''   ||   ''',sudoku[0][6],'''   |   ''',sudoku[0][7],'''   |   ''',sudoku[0][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[1][0],'''   |   ''',sudoku[1][1],'''   |   ''',sudoku[1][2],'''   ||   ''',sudoku[1][3],'''   |   ''',sudoku[1][4],'''   |   ''',sudoku[1][5],'''   ||   ''',sudoku[1][6],'''   |   ''',sudoku[1][7],'''   |   ''',sudoku[1][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[2][0],'''   |   ''',sudoku[2][1],'''   |   ''',sudoku[2][2],'''   ||   ''',sudoku[2][3],'''   |   ''',sudoku[2][4],'''   |   ''',sudoku[2][5],'''   ||   ''',sudoku[2][6],'''   |   ''',sudoku[2][7],'''   |   ''',sudoku[2][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[3][0],'''   |   ''',sudoku[3][1],'''   |   ''',sudoku[3][2],'''   ||   ''',sudoku[3][3],'''   |   ''',sudoku[3][4],'''   |   ''',sudoku[3][5],'''   ||   ''',sudoku[3][6],'''   |   ''',sudoku[3][7],'''   |   ''',sudoku[3][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[4][0],'''   |   ''',sudoku[4][1],'''   |   ''',sudoku[4][2],'''   ||   ''',sudoku[4][3],'''   |   ''',sudoku[4][4],'''   |   ''',sudoku[4][5],'''   ||   ''',sudoku[4][6],'''   |   ''',sudoku[4][7],'''   |   ''',sudoku[4][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[5][0],'''   |   ''',sudoku[5][1],'''   |   ''',sudoku[5][2],'''   ||   ''',sudoku[5][3],'''   |   ''',sudoku[5][4],'''   |   ''',sudoku[5][5],'''   ||   ''',sudoku[5][6],'''   |   ''',sudoku[5][7],'''   |   ''',sudoku[5][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[6][0],'''   |   ''',sudoku[6][1],'''   |   ''',sudoku[6][2],'''   ||   ''',sudoku[6][3],'''   |   ''',sudoku[6][4],'''   |   ''',sudoku[6][5],'''   ||   ''',sudoku[6][6],'''   |   ''',sudoku[6][7],'''   |   ''',sudoku[6][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[7][0],'''   |   ''',sudoku[7][1],'''   |   ''',sudoku[7][2],'''   ||   ''',sudoku[7][3],'''   |   ''',sudoku[7][4],'''   |   ''',sudoku[7][5],'''   ||   ''',sudoku[7][6],'''   |   ''',sudoku[7][7],'''   |   ''',sudoku[7][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ||       |       |       ||       |       |       ||       |       |       ||
        ||   ''',sudoku[8][0],'''   |   ''',sudoku[8][1],'''   |   ''',sudoku[8][2],'''   ||   ''',sudoku[8][3],'''   |   ''',sudoku[8][4],'''   |   ''',sudoku[8][5],'''   ||   ''',sudoku[8][6],'''   |   ''',sudoku[8][7],'''   |   ''',sudoku[8][8],'''   ||
        ||       |       |       ||       |       |       ||       |       |       ||
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ++-------+-------+-------++-------+-------+-------++-------+-------+-------++
        ''', sep = "")


def sudoku_transpose(sudoku):
	sudoku_trans = [[' ' for i in range(9)] for j in range(9)]
	# Iterate through rows
	for i in range(len(sudoku)):
		#Iterate through columns
		for j in range(len(sudoku[0])):
			sudoku_trans[j][i] = sudoku[i][j]
	return sudoku_trans

def check_duplicates(numbers):
	for n1 in range(len(numbers)):
		if numbers[n1] == '0':
			continue
		else:
			for n2 in range(len(numbers)):
				if numbers[n2] == '0' or n1 == n2:
					continue
				if numbers[n1] == numbers[n2]:
					return False
	return True

def polulate_line(line):
	not_valid = True
	while not_valid:
		print("\nLine:", line+1)
		numbers = input("Enter numbers:")
		if len(numbers) == 9 and numbers.isdigit() and check_duplicates(numbers):
			not_valid = False
		else:
			print("Not 9 digits or non-digit input or duplicated numbers!")
			continue
	numbers_list = []
	for number in numbers:
		if number ==  '0':
			numbers_list.append(' ')
		else:
			numbers_list.append(int(number))
	sudoku[line] = numbers_list

def empty_cells(list):
	i = 0
	empty_list = []
	for n in list:
		if n == ' ':
			empty_list.append(i)
		i += 1
	return empty_list

def empty_cells_sqr(sqr):
	empty_list_sqr = []
	for i in range(3):
		for j in range(3):
			if sqr[i][j] == ' ':
				empty_list_sqr.append((i,j))
	return empty_list_sqr

def all_empty_cells(sudoku):
	all_empty = 0
	# Iterate through rows
	for i in range(len(sudoku)):
		#Iterate through columns
		for j in range(len(sudoku[0])):
			if sudoku[i][j] == ' ':
				all_empty += 1
	return all_empty

def n_in_3x3sq_row(sudoku,i,j,n):
	list = []
	if i < 3:
		if j < 3:
			for i in range(3):
				for j in range(3):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		elif j > 2 and j < 6:
			for i in range(3):
				for j in range(3,6):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		else:
			for i in range(3):
				for j in range(6,9):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False

	elif i > 2 and i < 6:
		if j < 3:
			for i in range(3,6):
				for j in range(3):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		elif j > 2 and j < 6:
			for i in range(3,6):
				for j in range(3,6):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		else:
			for i in range(3,6):
				for j in range(6,9):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False

	else:
		if j < 3:
			for i in range(6,9):
				for j in range(3):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		elif j > 2 and j < 6:
			for i in range(6,9):
				for j in range(3,6):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False
		else:
			for i in range(6,9):
				for j in range(6,9):
					list.append(sudoku[i][j])
			if n in list:
				return True
			else:
				return False

def sqr3_to_sqr9(sqr):
	if sqr < 3:
		i = 0
	elif sqr > 2 and sqr < 6:
		i = 3
	else:
		i = 6
	j = sqr%3*3
	return (i,j)

def get_sudoku_3x3_sq(sqr):
	sqr_3x3 = []
	# coef. k = 0 if sqr <3, k = 3, if sqr < 6 and k =6 if sqr < 9
	k = sqr//3*3
	for i in range(3):
		sqr_3x3.append(sudoku[i+k][(sqr-k)*3:(sqr-k)*3+3])
	return sqr_3x3

def row_col_valid(row_num, col_num):
	row_num -= 1
	col_num -= 1
	if row_num not in range(9) or col_num not in range(9):
		return False
	if sudoku[row_num][col_num] != ' ':
		return False
	else:
		return True

def sudoku_valid(sudoku):
	result = True
	for row in sudoku:
		for n1 in range(len(row)):
			if row[n1] == ' ':
				continue
		else:
			for n2 in range(len(row)):
				if row[n2] == ' ' or n1 == n2:
					continue
				if row[n1] == row[n2]:
					result = False
	return result

sudoku = [[' ' for i in range(9)] for j in range(9)]
sudoku = [[int((j+i)/2) for i in range(9)] for j in range(9)]

for line in range(9):
	polulate_line(line)

#temm. hardcode:
# solved
#sudoku = [[' ', ' ', ' ', ' ', 9, 2, ' ', ' ', ' '], [4, ' ', 9, 8, ' ', ' ', 7, ' ', 6], [5, ' ', ' ', 4, ' ', 6, 3, ' ', ' '], [9, 6, ' ', 2, 4, ' ', ' ', 8, ' '], [' ', 5, ' ', 7, ' ', ' ', ' ', 9, ' '], [' ', 1, 8, ' ', 6, 9, ' ', 3, ' '], [' ', ' ', 5, 9, ' ', 8, ' ', 6, 3], [1, ' ', 6, ' ', 2, 7, ' ', ' ', 8], [8, 3, ' ', ' ', 5, ' ', 9, ' ', ' ']]
#sudoku = [[' ', 2, 3, ' ', ' ', 5, ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', 3, ' ', 9, 6], [' ', ' ', ' ', ' ', ' ', 4, ' ', 8, 2], [4, ' ', ' ', ' ', ' ', ' ', 1, ' ', 9], [' ', 9, ' ', ' ', ' ', ' ', ' ', 3, ' '], [' ', ' ', ' ', ' ', 1, ' ', 4, 7, ' '], [9, ' ', ' ', ' ', ' ', 1, 6, ' ', ' '], [' ', ' ', 8, 3, ' ', ' ', ' ', ' ', ' '], [' ', ' ', 5, ' ', 6, 2, ' ', ' ', 3]]

# unsolved:
#sudoku = [[' ', ' ', ' ', 1, 3, ' ', ' ', 2, ' '], [7, 2, ' ', 4, ' ', ' ', 8, ' ', ' '], [' ', ' ', 8, ' ', 9, ' ', ' ', ' ', ' '], [' ', ' ', ' ', 6, 5, 4, 9, ' ', ' '], [' ', ' ', ' ', ' ', ' ', 9, ' ', ' ', 2], [6, 4, ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', 2, ' ', 1, ' ', ' ', 4, 5], [' ', ' ', 7, ' ', ' ', 3, ' ', ' ', ' '], [1, ' ', ' ', ' ', ' ', ' ', ' ', ' ', 3]]
#sudoku = [[9, 8, ' ', ' ', 6, 7, ' ', 3, ' '], [5, ' ', ' ', ' ', ' ', 8, ' ', ' ', ' '], [' ', ' ', ' ', 3, ' ', ' ', ' ', ' ', ' '], [6, ' ', ' ', ' ', 1, ' ', ' ', ' ', ' '], [' ', ' ', ' ', 5, ' ', ' ', ' ', ' ', 3], [4, 2, ' ', ' ', ' ', ' ', ' ', 6, 8], [' ', ' ', 7, ' ', 2, ' ', 6, 9, ' '], [' ', 9, ' ', ' ', ' ', ' ', 5, ' ', ' '], [' ', 6, ' ', ' ', ' ', 5, ' ', ' ', 7]]



dis_board(sudoku)
print(sudoku)
all_found = 0
all_empty = all_empty_cells(sudoku)
found_digits = 81 - all_empty

while True:
	found_digits = 0

	# for each row in the sudoku
	for row in range(len(sudoku)):
		sudoku_trans = sudoku_transpose(sudoku)
		#dis_board(sudoku_trans)

		sudoku_row = sudoku[row]

		missing_digits = []
		for n in range(1,10):
			if n not in sudoku_row:
				missing_digits.append(n)
		#print("Missing digits for row", row, ":", missing_digits)
	
		# for each missing digit in given row:
		for digit in missing_digits:
			empty_list = empty_cells(sudoku_row)
			#print("Empty list for digit", digit, "on row", row, ":", empty_list)

			# cells to be removed as not possible
			# if digit is in 3x3 square
			removed_cells = []
			for cell in empty_list:
				if n_in_3x3sq_row(sudoku,row,cell,digit):
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)
	
			#print("Empty cells list:", empty_list)

			if len(empty_list) == 1:
				print("   * Digit", digit, "is at cell", empty_list[0]+1, "on row", row+1) 
				sudoku[row][empty_list[0]] = digit
				found_digits += 1
				continue

			# if digit is contained in a column
			removed_cells = []
			for cell in empty_list:
				if digit in sudoku_trans[cell]:
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)
			
			#print("Empty cells list:", empty_list)
	
			if len(empty_list) == 1:
				print("  ** Digit", digit, "is at cell", empty_list[0]+1, "on row", row+1) 
				sudoku[row][empty_list[0]] = digit
				found_digits += 1

	# for each column in the sudoku
	for row in range(len(sudoku_trans)):
		sudoku_trans = sudoku_transpose(sudoku)
		#dis_board(sudoku_trans)

		sudoku_row = sudoku_trans[row]

		missing_digits = []
		for n in range(1,10):
			if n not in sudoku_row:
				missing_digits.append(n)
		#print("Missing digits for row", row, ":", missing_digits)
	
		# for each missing digit in given row:
		for digit in missing_digits:
			empty_list = empty_cells(sudoku_row)
			#print("Empty list for digit", digit, "on row", row, ":", empty_list)

			# cells to be removed as not possible
			# if digit is in 3x3 square
			removed_cells = []
			for cell in empty_list:
				if n_in_3x3sq_row(sudoku_trans,row,cell,digit):
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)
	
			#print("Empty cells list:", empty_list)

			if len(empty_list) == 1:
				print(" *** Digit", digit, "is at cell", empty_list[0]+1, "on column", row+1) 
				sudoku[empty_list[0]][row] = digit
				found_digits += 1
				continue

			# if digit is contained in a row
			removed_cells = []
			for cell in empty_list:
				if digit in sudoku[cell]:
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)
			
			#print("Empty cells list:", empty_list)
	
			if len(empty_list) == 1:
				print("**** Digit", digit, "is at cell", empty_list[0]+1, "on column", row+1) 
				sudoku[empty_list[0]][row] = digit
				found_digits += 1

	# for each 3x3 square in the sudoku
	for square in range(len(sudoku)):
		sudoku_trans = sudoku_transpose(sudoku)
		#dis_board(sudoku_trans)

		sqr_3x3 = get_sudoku_3x3_sq(square)

		missing_digits = []
		for n in range(1,10):
			#for i in range(3):
			if n not in sqr_3x3[0] and n not in sqr_3x3[1] and n not in sqr_3x3[2]:
				missing_digits.append(n)
		#print("Missing digits for 3x3 square", square+1, ":", missing_digits)
	
		# for each missing digit in given square:
		for digit in missing_digits:
			empty_list = empty_cells_sqr(sqr_3x3)
			#print("Empty list for digit", digit, "on row", row, ":", empty_list)
			
			#print(empty_list)
		
			dev = sqr3_to_sqr9(square)

			# if digit is contained in a row
			removed_cells = []
			for cell in empty_list:
				if digit in sudoku[cell[0]+dev[0]]:
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)
			
			#print("Empty cells list:", empty_list)
	
			if len(empty_list) == 1:
				print("  !* Digit", digit, "is at cell", empty_list[0], "on square", square+1) 
				sudoku[empty_list[0][0]+dev[0]][empty_list[0][1]+dev[1]] = digit
				found_digits += 1
				continue

			# if digit is contained in a column
			removed_cells = []
			for cell in empty_list:
				if digit in sudoku_trans[cell[1]+dev[1]]:
					removed_cells.append(cell)
			for cell in removed_cells:
				empty_list.remove(cell)

			#print("Empty cells list:", empty_list)
	
			if len(empty_list) == 1:
				print(" !!* Digit", digit, "is at cell", empty_list[0], "on square", square+1) 
				sudoku[empty_list[0][0]+dev[0]][empty_list[0][1]+dev[1]] = digit
				found_digits += 1

	all_found += found_digits

	if found_digits:
		print("Found digits:", found_digits)
	else:
		dis_board(sudoku)
		if all_empty_cells(sudoku):
			print("From all", all_empty, "empty cells, I found", all_found)
			if sudoku_valid(sudoku) and sudoku_valid(sudoku_trans):
				answer = input("Do you want to help if you know some digit positions? (Y/n)")
			else:
				print("Hm, something is wrong! I'm done.")
				break
			if answer.lower() == 'n':
				break
			else:
				print("Great!")
				try:
					row_num = int(input("Give me the row number: "))
					col_num = int(input("Give me the column number: "))
					if row_col_valid(row_num, col_num):
						digit = int(input("Give me the digit: "))
						if digit in range(1,10):
							print("Allright, let's try that!")
							sudoku[row_num-1][col_num-1] = digit
						else:
							print("Sorry, this is not a valid digit!")
					else:
						print("Sorry, not valid possition or not empty! Please try again!")
				except ValueError:
					print("Sorry, this is not a digit!")
				time.sleep(3)	
		else:
			sudoku_trans = sudoku_transpose(sudoku)
			if sudoku_valid(sudoku) and sudoku_valid(sudoku_trans):
				print("Hooray! I solved this sudoku!")
				print("From all", all_empty, "empty cells, I found", all_found)
			else:
				print("Hm, something is wrong! I'm done.")
			break
