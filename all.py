# Selection of Maths Operations
print "Math Operations"
a=int(input("What do you want the first number to be?"))
b = int(input("What do you want the second number to be?"))
c = int(input("What do you want the third number to be?"))

#add two digits
def add(a,b):
	d = a + b
	print d
# subtract two numbers
def subtract(a,b):
	if a > b:
		d = a-b
	if b > a:
		d = b-a
	print d
# divide two numbers
def divide(a,b):
	if a > b:
		d = a/b
	if b > a:
		d = b/a
	print d

# find if one number is divisible by the other or not
def divisible(a,b):
	if a % b == 0:
		print "Yes"
	if b % a == 0:
		print "Yes"
	
	else:
		print ""
	
#check if the number is greater than 100.
def greaterThan100(a):
	if a > 100:
		print "Yes"
	if a < 100:
		print "No"
	if a == 100:
		print "equal"
	
#multiply two digits
def multiply(a,b):
	d = a*b
	print d	

#power 2 numbers
def power(a,b):
	d = a**b
	print d

#determine which of two numbers that you enter is greater
def greater(a,b):
	if a > b:
		print a
	if b > a:
		print b
	
#determine which is least out of three numbers you give.
def least(a,b,c):
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
def greatest(a,b,c):
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
#find the absolute value of a number
def absoluteValue(a):
	if a >0:
		print a
	if a < 0:
		b = -a
		print b

#identify whether a number given is a palindrome or not
def palindrome(a):
	b=0
	c=0
	d=a
	while a > 0:
		b = a % 10
		a = a / 10
		c = c * 10 + b
	if c == d:
		print "palindrome"
	else:
		print "not a palindrome"		
#sum of digits in a number
def sumOfDigits(a):
	b=0
	c=0
	while a > 0:
		b = a % 10
		a = a / 10
		c = c + b
	print c	

print "Which operation do you want?"
print "1: Addition"
print "2: Subtraction"
print "3: Multiplication"
print "4: Division"
print "5: Power"
print "6: Greater of the two numbers"
print "7: Greatest of all of the numbers"
print "8: Least of all of the numbers"
print "9: Divisible by the other number"
print "10: Greater than 100"
print "11: Absolute value"
print "12: Palindrome"
print "13: Sum of Digits in a number"

x = int(input("What operation do you want to do?"))
if x == 1:
	add(a,b)
if x == 2:
	subtract(a,b)
if x == 3:
	multiply(a,b)
if x == 4:
	divide(a,b)
if x == 5:
	power(a,b)
if x == 6:
	greater(a,b)
if x == 7:
	greatest(a,b,c)
if x == 8:
	least(a,b,c)
if x == 9:
	divisible(a,b)
if x == 10:
	greaterThan100(a)
if x == 11:
	absoluteValue(a)
if x == 12:
	palindrome(a)
if x == 13:
	sumOfDigits(a)