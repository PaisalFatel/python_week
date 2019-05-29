Alpha=input("Enter any single character: ")
if ord(Alpha)>=65 and ord(Alpha)<=90:
	print("The character", Alpha, "is upper case")
else:
	if ord(Alpha)>=97 and ord(Alpha)<=122:
		print("The character is lower case")
	else:
		if ord(Alpha)>=48 and ord(Alpha)<=57:
			print("The character is a digit")
		else:
			print("The character is special")