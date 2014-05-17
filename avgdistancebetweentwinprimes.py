# author: akhileshcheguisthebestintheworld
# Total number of twin primes from 1 to 1000
total = 0
LastPrime = 2
total2 = 0
total3 = 0
total4 = 0
d = 0
p1 = 2
p2 = 3
for n in range(2,1001):
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