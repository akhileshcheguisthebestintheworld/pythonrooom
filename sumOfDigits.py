#sum of digits in a number
n=int(input("What do you want a to be?"))
t=0
s=0
while n > 0:
	t = n % 10
	n = n / 10
	s = s + t
print s	