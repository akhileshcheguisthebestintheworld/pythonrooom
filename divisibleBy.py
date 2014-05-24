# find if one number is divisible by the other or not
a = int(input("What do you want a to be?"))
b = int(input("What do you want b to be?"))
if a % b == 0:
	print "Yes"
if b % a == 0:
	print "Yes"
else:
	print "No"