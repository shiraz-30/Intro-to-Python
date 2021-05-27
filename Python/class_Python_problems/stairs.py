# Q=> From any step, you can eiher jump by 1 step or 2 steps.
# In how many different ways, you can reach the last step?


def ways(n, i, path):
	# i(int) represents where you are currently standing
	# path(string) stores the paths
    if (i > n):
    	 return
    if (i == n):
    	 print(path)
    	 return

    ways(n, i + 1, "1" + path)
    ways(n, i + 2, "2" + path)

n = int(input())
ways(n, 0, "")

