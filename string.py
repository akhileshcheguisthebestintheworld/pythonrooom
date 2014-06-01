# pig latin strings
word = input("HI ZOMBIE.")
word = word.lower()
output = ""
vowels = [ "a", "e", "i", "o", "u"]
if word[0] in vowels:
	output = output+ word + "yay"
else:
	start = 0
	for letter in list(word):
		if letter in vowels:
			break
		else:
			start += 1
			
	output += word[start:] + word[:start] + "ay"
print output																																																																					