T = int(input())

for i in range(0, T):
	n = int(input())
	a = input()
	arr = list(a.split(" "))

	for i in range(0, n):
		arr[i] = int(arr[i])

	b = input()
	brr = list(b.split(" "))

	for j in range(0, n):
		brr[j] = int(brr[j])

	if sorted(arr) == brr:
		print("yes")
	else:
		print("no")


