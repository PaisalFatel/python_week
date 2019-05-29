F=0
msg=input("Enter your word: ")
find=input("What you looking for: ")
i=0
while i<len(msg):
	if msg[i]==find[0]:
		if msg[i: i+len(find)]==find:
			F=F+1
			i=i+len(find)-1
	i=i+1
print(F)