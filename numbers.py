# author: akhileshcheguisthebestintheworld
numbers = range(1,501)
total = 0
for number in numbers:
	if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
		total = total + number
print total
