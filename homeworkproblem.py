word = input("Speak, human.")
length = len(word)
for i in range(0,(length/2)):
	if word[i] == word [-i-1]:
		return True
		palindrome = 1
	
	else:
		return False
		palindrome = 0
if palindrome == 0:
	print "Not a palindrome"
else:
	print "palindrome"