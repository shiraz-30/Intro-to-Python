def lessthan(x, y):
    return x[0] < y[0]

def choose_pivot(arr):
	pivot_index = {}

	for j in range(0, len(arr)):
		if arr[j][0] in pivot_index:
			continue
		pivot_index[arr[j][0]] = j

	possible_index = list(pivot_index.values())
	possible_index = sorted(possible_index)
	return(possible_index)

n = int(input())
arr_strip = list(map(int, input().split()))
arr = []
for i in range(0, 2*n, 2):
    arr.append((arr_strip[i], arr_strip[i+1]))
 
candidates = choose_pivot(arr)
 
print(len(candidates))
print(*candidates)

