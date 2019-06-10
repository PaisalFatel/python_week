Find=input("What are you looking for?: ")
replace=input("Replace with what?: ")

file_read=open("Data.txt","r")
file_write=open("Data2.txt","w")

for Data in file_read:
	i=0
	while i<len(Data):
		if Data[i]==Find[0]:
			if Data[i:len(Find)+i]==Find:
				print(replace,end="",file=file_write)
				i+=len(Find)-1
			else:
				print(Data[i],end="",file=file_write)
		else:
			print(Data[i],end="",file=file_write)
		i+=1

file_write.close()
file_write_read=open("Data2.txt","r")
for Data2 in file_write_read:
	print(Data2)