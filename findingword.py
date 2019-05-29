msg=input("Enter any message: ")
msg=msg+" "
what=input("what you looking for mate: ")
counter=0
word=""
i=0
while i<len(msg):
	if msg[i]==" ":
		if word ==what:
			counter=counter+1
		word=""
	else:
		word=word + msg[i]
	i=i+1
print(counter)