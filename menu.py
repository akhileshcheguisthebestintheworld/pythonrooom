# author: akhileshcheguisthebestintheworld

menu = ["pizza","pasta","cake"]

for thing in menu:
	answer = input("Do you like " + thing +"?")
	if answer == "yes":
		print "Have it" + "."
	elif answer == "no":
		print "Okay."
	else:
		print "I do not understand what that was" + "."