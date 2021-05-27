import math

n = int(input())
data = {}
fare = 0

for i in range(n):
	event = input()
	if event == 'entry':
		license_number = input()
		data[license_number] = int(input())

	elif event == 'exit':
		license_number = input()
		time = int(input())

		time_elapsed = time - data[license_number]
		payable = time_elapsed / 60

		payable = ( math.ceil(time_elapsed / 60) - 1 )

		if payable >= 0:
			fare += (60 + 30*payable)

print(fare)
