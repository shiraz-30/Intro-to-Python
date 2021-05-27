def no_of_profitable_matches(arr):
	if len(arr) == 2:
		if arr[0] != arr[1]:
			return 1
		else:
			return 0

	mid = (len(arr) // 2)

	left_of_profitable_matches = no_of_profitable_matches(arr[:mid])
	right_of_profitable_matches = no_of_profitable_matches(arr[mid:])

	matches_played_A = set(arr[:mid])
	matches_played_B = set(arr[mid:])

	if (matches_played_A & matches_played_B):
		return left_of_profitable_matches + right_of_profitable_matches
	else:
		return left_of_profitable_matches + right_of_profitable_matches + 1

n = int(input())
arr = list(map(int, input().split()))

print(no_of_profitable_matches(arr))



