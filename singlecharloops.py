Char=0
msg=input("Enter the message: ")
Char=input("Enter character: ")
i=0
while i<len(msg):
	if msg[i]=="Char":
		word=word+1
	i=i+1
print("There are",word+1, "words")
