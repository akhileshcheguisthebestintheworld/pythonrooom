# author: akhileshcheguisthebestintheworld
a=0
b=1
c=0
total=0

while b < 1000000:
	c=b
	b = a + b
	a=c
	if a % 2 == 0:
		total = total + a
print total