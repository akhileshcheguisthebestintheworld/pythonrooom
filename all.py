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