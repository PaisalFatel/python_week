def countmsg(message,alpha):
	A=65
	a=97
	i=0
	Count=0
	if ord(message[i])>=65 and ord(message[i])<=90:
		while i<len(message):
			if message[i]==alpha:
				Count+=1
			i+=1
		if Count>0:
			print(alpha,"=",Count)
	else:
		if ord(message[i])>=97 and ord(message[i])<=122:
			while i<len(message):
				if message[i]==alpha:
					Count+=1
				i+=1
			if Count>0:
				print(alpha,"=",Count)

msg=input("Enter your message: ")
C=65
while C<=122:
	countmsg(msg,chr(C))
	C+=1