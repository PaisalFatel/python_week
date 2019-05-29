Alpha=input("Enter any alphabet: ")
if ord(Alpha)>=97 and ord(Alpha)<=122:
	print(chr(ord(Alpha)-32))
else:
	print(chr(ord(Alpha)+32))