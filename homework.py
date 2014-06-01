# author: akhileshcheguisthebestintheworld
import random
pictures = 1
flies = int(input("How many flies are in the room?"))
for n in random.randint(1,1000):
	while n < flies:
		print "Nobody is blinking."
	while n > flies:
		print "Somebody is blinking."
		pictures = pictures + 1
print pictures		