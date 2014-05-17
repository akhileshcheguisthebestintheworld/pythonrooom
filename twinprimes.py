# author: akhileshcheguisthebestintheworld
total = 0
LastPrime = 2
total2 = 0 
d = 0
p1 = 2
p2 = 3
for n in range(2,50):
	tests = range(2,n-1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
	if prime == True:
		total = n - LastPrime
		if total == 2:
			total2 = total2 + 1
		LastPrime = n
print total2		