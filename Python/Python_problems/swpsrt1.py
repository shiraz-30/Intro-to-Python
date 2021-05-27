def find_min_element_idx(arr, start):
	min_index = start

	start += 1

	while(start < len(arr)):
		if arr[start] < arr[min_index]:
			min_index = start

		start += 1

	return min_index

n = int(input())
a = list(map(int, input().split()))

no_of_swaps = 0
swapped_idx = []

for i in range(0, len(a)):
	j = find_min_element_idx(a, i)

	if i != j:
		a[i], a[j] = a[j], a[i]

		no_of_swaps += 1
		swapped_idx.append([i, j])

print(no_of_swaps)

for i in range(0, len(swapped_idx)):
	print(swapped_idx[i][0], swapped_idx[i][1])



