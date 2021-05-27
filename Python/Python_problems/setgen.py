def subset(li, index, output, set_of_subsets):
	if index == len(li):
		set_of_subsets += str(output)
		print(set_of_subsets)
		return

	subset(li, index + 1, output, set_of_subsets)
	output = str(len(li) - index)+ " "+output
	subset(li, index + 1, output, set_of_subsets)
	output = output[3:]
	return

T = int(input())

for i in range(0, T):
	n = int(input())
	li = []

	for j in range(1, n + 1):
		li.append(j)

	out = " "
	set_of_subsets = " "
	subset(li, 0, out, set_of_subsets)


