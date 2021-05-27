n = int(input())
intersection_points = {}

for k in range(0, n):
	street = input()
	result = []

	for i in range(0, len(street)):
		if street[i] == " ":
			result.append(i)

	point_1 = street[0 : result[0]]
	point_2 = street[result[0] + 1 : result[1]]
	notation = street[result[1] + 1 : result[2]]
	direction = street[len(street) - 1]

	x = [int(point_1), int(point_2), notation, direction]

	if x[0] in intersection_points.keys():
		intersection_points[x[0]].append(x[2])
	else:
		intersection_points[x[0]] = [x[2]]

	if x[1] in intersection_points.keys():
		intersection_points[x[1]].append(x[2])
	else:
		intersection_points[x[1]] = [x[2]]


crossing = 0

for m in intersection_points.keys():
	if len(intersection_points[m]) == 4:
		s = []
		count = 0

		for j in intersection_points[m]:
			if j not in s:
				s.append(j)
				count += 1

		if count == 2:
			crossing += 1

print(crossing)

	