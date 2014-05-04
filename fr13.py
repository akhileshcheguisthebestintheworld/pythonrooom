# author: akhileshcheguisthebestintheworld
years = range(1900,2015)
count = 0
months = range(1,13)

for year in years:
	for month in months:
		if month == 2:
			days = range(1,29)
		if month == 4 or month == 6 or month == 9 or month == 11:
			days = range(1,31)
		else:
			days = range(1,32)
		for day in days:
			count = count + 1
		
print count	
	