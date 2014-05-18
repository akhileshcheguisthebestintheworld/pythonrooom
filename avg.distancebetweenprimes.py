# author: akhileshcheguisthebestintheworld
# Find the average distance between prime numbers from 1 to 1000

total=0
LastPrime=2
total2=0
for n in range(3,998):
	tests=range(2,n-1)
	prime=True
	for t in tests:
		if n % t == 0:
			prime = False
	if prime == True:
		total = total + (n-LastPrime)
		LastPrime=n
		total2 = total2 + 1		
print total/total2	