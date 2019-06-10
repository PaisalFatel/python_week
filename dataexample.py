file_read=open("Data.txt","r")
file_write=open("Data2.txt","w")

for Data in file_read:
	for char in Data:
		if char=="o":
			print("*",end="",file=file_write)
		else:
			print(char,end="",file=file_write)
file_write.close()
file_write_read=open("Data2.txt","r")
for Data2 in file_write_read:
	print(Data2)