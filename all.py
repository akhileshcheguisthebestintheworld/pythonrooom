# Selection of Maths Operations
a=int(input("What do you want the first number to be?"))
b = int(input("What do you want the second number to be?"))
c = int(input("What do you want the third number to be?"))

#add two digits
def add(a,b):
	d = a + b
	print d

# divide two numbers

if a > b:
	d = a/b
if b > a:
	d = b/a
print d

# find if one number is divisible by the other or not
if a % b == 0:
	print "Yes"
if b % a == 0:
	print "Yes"

else:
	print ""
	
#check if the number is greater than 100.
if a > 100:
	print "Yes"
if a < 100:
	print "No"
if a == 100:
	print "equal"
	
#multiply two digits

d = a*b
print c	

#power 2 numbers

d = a**b
print answer3

#determine which of two numbers that you enter is greater
if a > b:
	print a
if b > a:
	print b
	
#determine which is least out of three numbers you give.
if a < b < c:
	print a
if a < c < b:
	print a
if b < a < c:
	print b
if b < c < a:
	print b
if c < a < b:
	print c
if c < b < a:
	print c	
	
#determine which is greatest out of three numbers you give.
if a > b > c:
	print a
if a > c > b:
	print a
if b > a > c:
	print b
if b > c > a:
	print b
if c > a > b:
	print c
if c > b > a:
	print c	