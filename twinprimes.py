# author: akhileshcheguisthebestintheworld
total = 0
total2 = 0 
d = 0
p1 = 2
p2 = 3
for n in range(2,1001):
	tests = range(2,n-1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
			p1 = p2
			p2 = 