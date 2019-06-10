def wordcheck(message):
	i=0
	word=""
	word2=""

	while i<len(message):
		if message[i]==" ":
			if len(word)>len(word2):
				word2=word
			word=""
		else:
			word=word+message[i]
			
		i+=1
	if len(word)>len(word2):
				word2=word
	return word2

msg=input("Enter your message: ")
print(wordcheck(msg))