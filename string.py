# author: akhileshcheguisthebestintheworld
word = input("HI,ZOMBIE.")
word = word.lower()
output = ""
vowels = [ "a", "e", "i", "o", "u"]
if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u":
	output += word + "yay"
else:
	word[0] = word[-1]
	del word[0]
print output	