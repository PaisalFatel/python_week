Numbers=[]
while True:
	num=int(input("Enter any number"))
	if num==0:
		break
	else:
		Numbers.append(num)
Highest=Numbers[0]
i=0
while i<len(Numbers):
	if Numbers[i]>Highest:
		Highest=Numbers[i]
	i+=1
print ("the Highest number is: ", Highest)