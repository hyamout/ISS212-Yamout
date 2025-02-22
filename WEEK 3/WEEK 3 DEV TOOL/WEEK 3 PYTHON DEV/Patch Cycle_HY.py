#ISS 212
#Week 3 Dev Tool - Patch Cycle

year = int(input("Enter the year to check the patch cycle: "))
if year < 2019:
	print("Not within the managed patch period.")
else:
	if year % 4 != 0:
		print("Standard Year")
	elif year % 100 != 0:
		print("Patch Year")
	elif year % 400 != 0:
		print("Standard Year")
	else:
		print("Patch Year")
