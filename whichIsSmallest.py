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