word = input("Speak, human.")
length = len(word) + 1
for i in range(0,length):
	if word [i] == word [-i-1]: 
		print "Palindrome."
	else:
		print "Not a palindrome."