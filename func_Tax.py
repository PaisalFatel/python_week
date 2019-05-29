def Tax(Salary):
	if Salary>1500:
		T=Salary*(21/100)
	else:
		T=Salary*(15/100)
	return T
Salary1=int(input("Enter your Salary: "))
print("Your Tax: ", Tax(Salary1))
print("Net",(Salary1-(Tax(Salary1))))