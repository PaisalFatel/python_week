def operation(day):
	if day==1:
		def func(A,B):
			C=A+B
			print("The grand total is: ", C)
	if day==2:
		def func(A,B):
			C=A-B
			print("The grand total is: ", C)
	return func

Daynumber=input("Pick either 1 or 2: ")
Calc1=float(input("1st number: "))
Calc2=float(input("2nd number: "))


if Daynumber=="1":
	Maths=operation(1)
	Maths(Calc1,Calc2)
	print("The total is: ", Maths)
	

if Daynumber=="2":
	Maths=operation(2)
	Maths(Calc1,Calc2)
	print("The total is: ", Maths)