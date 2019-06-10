AlphaU=[0]*26
AlphaL=[0]*26

message=input("Enter any message: ")

i=0
while i<len(message):
	Ascii=ord(message[i])
	if Ascii>=65 and Ascii<=90:
		AlphaU[ord(message[i])-65]+=1

	if Ascii>=97 and Ascii<=122:
		AlphaL[ord(message[i])-97]+=1
	i+=1

i=0
while i<=25:
	if AlphaU[i]>0:
		print(chr(i+65),"=",AlphaU[i])
	if AlphaL[i]>0:
		print(chr(i+97),"=",AlphaL[i])
	i+=1