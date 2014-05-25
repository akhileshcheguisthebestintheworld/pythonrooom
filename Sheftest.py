# testing functions

print "Maths Operations"
a=int(input("What do you want your first number to be?"))
b=int(input("What do you want your second number to be?"))


def add(a,b):
	c = a+b
	print c

def subtract(a,b):
	if a > b:
		c = a-b
		print c
	if b > a:
		c = b-a
		print c
	
print "Which operation do you want?"
print "1: Addition"
print "2: Subtraction"
d=int(input("Which operation do you want to do?"))

if d == 1:
	add(a,b)
if d == 2:
	subtract(a,b)
	

