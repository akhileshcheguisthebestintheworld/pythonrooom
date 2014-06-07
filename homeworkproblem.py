#figure if a word is a palindrome or not

word = input("Speak, human.")
length = len(word)
counter = 0
for i in range(0,(length/2)):
	if word[i] == word [-i-1]:
		counter = counter + 1
		
	else:
		print "Not a palindrome"
		counter = counter - length
		break		
if counter > 0:
	print "palindrome"