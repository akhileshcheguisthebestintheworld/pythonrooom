#add two digits

answer = int(input("What do you want a to be?"))
answer2 = int(input("What do you want b to be?"))
answer3 = answer + answer2
print answer3

# divide two numbers
answer = int(input("What do you want a to be?"))
answer2 = int(input("What do you want b to be?"))
if answer > answer2:
	answer3 = answer/answer2
if answer2 > answer:
	answer3 = answer2/answer
print answer3

# find if one number is divisible by the other or not
a = int(input("What do you want a to be?"))
b = int(input("What do you want b to be?"))
if a % b == 0:
	print "Yes"
if b % a == 0:
	print "Yes"

else:
	print ""
	
#check if the number is greater than 100.
answer = int(input("What do you want n to be?"))
if answer > 100:
	print "Yes"
if answer < 100:
	print "No"
if answer == 100:
	print "equal"
	
#multiply two digits

answer = int(input("What do you want a to be?"))
answer2 = int(input("What do you want b to be?"))
answer3 = answer*answer2
print answer3	

#power 2 numbers

answer = int(input("What do you want a to be?"))
answer2 = int(input("What do you want b to be?"))
answer3 = answer**answer2
print answer3

#determine which of two numbers that you enter is greater
answer = int(input("What do you want a to be?"))
answer2 = int(input("What do you want b to be?"))
if answer > answer2:
	print answer
if answer2 > answer:
	print answer2
	
#determine which is least out of three numbers you give.
a = int(input("What do you want a to be?"))
b = int(input("What do you want b to be?"))
c = int(input("What do you want c to be?"))
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
a = int(input("What do you want a to be?"))
b = int(input("What do you want b to be?"))
c = int(input("What do you want c to be?"))
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