def matrix_is_symmetric(matrix, n):
	
	for i in range(0, n):
		for j in range(0, n):
			if (matrix[i][j] != matrix[j][i]):
				return 0
	return 1

def matrix_is_upper_triangular(matrix, n):
	
	for i in range(1, n):
		for j in range(0, i):
			if (matrix[i][j] != 0):
				return 0
	return 1

def matrix_is_lower_triangular(matrix, n):
	
	for i in range(0, n):
		for j in range(i + 1, n):
			if (matrix[i][j] != 0):
				return 0
	return 1

def matrix_is_diagonal(matrix, n):
		
	for i in range(0, n):
		for j in range(0, n):
			if ((i != j) and (matrix[i][j] != 0)):
				return 0
	return 1

t_ = int(input())

for k in range(0, t_):
	n = int(input())
	matrix = []

	for i in range(0, n):
		rows = list(map(int, input().split()))
		matrix.append(rows)

	s,T, d = 0, 0, 0

	s = matrix_is_symmetric(matrix, n)

	t1 = matrix_is_upper_triangular(matrix, n)

	t2 = matrix_is_lower_triangular(matrix, n)

	if (t1 == 1 or t2 == 1):
		T = 1
	else:
		T = 0

	d = matrix_is_diagonal(matrix, n)

	answer = (s + (T * 2) + (d * 4))

	print(answer)
