# author: akhileshcheguisthebestintheworld
import random
pictures = 1
flies = int(input("How many flies are in the room?"))
for n in random.randint(1,10):
	while flies > n:
		print "Nobody is blinking."
	while flies < n:
		print "Somebody is blinking."
		pictures = pictures + 1
		
print pictures		