
# Print number of pictures till noone is blinking in a room full of flies

import random
pictures = 1
flies = int(input("How many flies are in the room?"))
x = random.randint(1,1000)

while x < flies:
	pictures = pictures + 1
	x = random.randint(1,1000)
		
print pictures