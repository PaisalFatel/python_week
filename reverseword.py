def reverseword(word):
	newword=""
	i=len(word)-1
	while i>=0:
		newword=newword+word[i]
		i+=1
	return word

message =input("Enter your word: ")
newmessage=""
word=""

for ch in message:
	if ch=="":
		newmessage+=(reverse(word))+""
		word=""
	else:
		word+=ch

print(newmessage)