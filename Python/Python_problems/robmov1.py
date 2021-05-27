t = int(input())

for i in range(0, t):
	x1, y1, x2, y2 = map(int, input().split())

	no_of_moves_in_x = abs(x1 - x2)
	no_of_moves_in_y = abs(y1 - y2)

	print(no_of_moves_in_x + no_of_moves_in_y)

	if (x1 >= x2 and y1 >= y2):
		print("W" * no_of_moves_in_x, end = "")
		print("S" * no_of_moves_in_y, end = "")

	elif (x1 >= x2 and y1 <= y2):
		print("W" * no_of_moves_in_x, end = "")
		print("N" * no_of_moves_in_y, end = "")

	elif (x1 <= x2 and y1 >= y2):
		print("E" * no_of_moves_in_x, end = "")
		print("S" * no_of_moves_in_y, end = "")

	elif (x1 <= x2 and y1 <= y2):
		print("E" * no_of_moves_in_x, end = "")
		print("N" * no_of_moves_in_y, end = "")

	print("")


