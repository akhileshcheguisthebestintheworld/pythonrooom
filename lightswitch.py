# author: akhileshcheguisthebestintheworld

switch = False

prisoners = range(1,101)
rounds = range(1,101)

for r in rounds:
	for prisoner in prisoners:
		#Check if prisoner is supposed to switch light
		if prisoner % r == 0:
			#Flip the switch
			if switch == False:
				switch = True
			else:
				switch = False
if switch == True:
	print "The switch is on!"
if switch == False:
	print "The switch is off!"