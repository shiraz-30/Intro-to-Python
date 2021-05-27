N, H, x = list(map(int, input().split()))
T = list(map(int, input().split()))

time_zone = max(T)

if (time_zone + x) >= H:
	print("YES")
else:
	print("NO")

