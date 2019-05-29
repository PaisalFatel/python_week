def change(message):
	i=0
	word=""
	while i<len(message):
		if ord(message[i])>=65 and ord(message[i])<=90:
			word = word + (chr(ord(message[i])+32))
		else:
			if ord(message[i])>=97 and ord(message[i])<=122:
				word = word + (chr(ord(message[i])-32))
			else:
				if ord(message[i])>=48 and ord(message[i])<=57:
					word = word + ((message[i])*2)
		i+=1
	return word
msg=input("Enter your message: ")
print(change(msg))
