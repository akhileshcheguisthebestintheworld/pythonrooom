# pig latin strings
words = input("HI ZOMBIE.")
words = words.lower()
words = words.split(" ")
output = ""
vowels = [ "a", "e", "i", "o", "u"]
for word in words:	
	if word[0] in vowels:
		output = output+ word + "yay "
	else:
		start = 0
		for letter in list(word):
			if letter in vowels:
				break
			else:
				if letter is "y":
					break
				else:	
					start += 1
		output += word[start:] + word[:start] + "ay "
print output