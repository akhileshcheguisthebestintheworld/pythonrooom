# author: akhileshcheguisthebestintheworld
n=int(input("What do you want a to be?"))
t=0
r=0
n1=n
while n > 0:
	t = n % 10
	n = n / 10
	r = r * 10 + t
if r == n1:
	print "palindrome"
else:
	print "not a palindrome"