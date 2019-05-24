Name=input("Enter your name:")
Salary=int(input("Enter your Salary:"))
if Salary>2000:
	Tax=Salary*(25/100)
else:
	Tax=Salary*(15/100)
Netsalary=Salary - Tax
print("Your name",Name)
print("Your Salary",Salary)
print("your Netsalary",Netsalary)
