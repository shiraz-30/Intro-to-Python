def maximum_overlap(start, end, n):
	ongoing_classes, max_intersect = 1, 1
	i, j = 1, 0

	while (i < n and j < n):
		if start[i] > end[j]:
			ongoing_classes -= 1
			j += 1
		else:
			ongoing_classes += 1

			if ongoing_classes > max_intersect:
				max_intersect = ongoing_classes

			i += 1
	print(max_intersect)

t = int(input())

for k in range(0, t):
	n = int(input())
	m = int(input())
	start, end = [], []

	for i in range(0, n):
		l, r = map(int, input().split())
		start.append(l)
		end.append(r)

	maximum_overlap(sorted(start), sorted(end), n)
