def Wordcount(message):
	word=1
	i=0
	while i<len(message):
		if message[i]==" ":
			word+=1
		i+=1
	return word
print("The number of words are: ", Wordcount("Hello my friends"))
print("words: ", Wordcount("I am back"))