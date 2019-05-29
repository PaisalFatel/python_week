word=0
msg=input("Enter the message: ")
char=input("What character: ")
letter=0
i=0
while i<len(msg):
	if msg[i]==char:
		letter=letter+1
	i=i+1
if letter>1:
	print("There are", letter, char, "characters")
else:
	print("There is",letter, char, "character")
