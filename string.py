# author: akhileshcheguisthebestintheworld
word = input("HI ZOMBIE.")
word = word.lower()
output = ""
vowels = [ "a", "e", "i", "o", "u"]
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
	output = output+ word + "yay"
else:
	output = output + word[1:] + word[0] + "ay"
print output	