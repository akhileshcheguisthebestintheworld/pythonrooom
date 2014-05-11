total = 0
LastPrime = 2
for n in range(2,1001):
	tests = range(2,n-1)
	prime = True
	for t in tests:
		if n % t == 0:
			prime = False
	if prime == True:		
		total = total + (n - LastPrime)
		LastPrime = n
print total	
		