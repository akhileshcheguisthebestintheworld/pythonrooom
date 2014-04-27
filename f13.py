# author: akhileshcheguisthebestintheworld
total = 0

date = 1
month = 1
year = 1900
while year < 2015:
	total = total + 1
	if month == 12 and date = 31:
		year = year + 1
		month = 1
		date = 1
	else:
		if date == 30:
			month = month + 1
			date = 1
		else:
			date = date + 1
		
print total		