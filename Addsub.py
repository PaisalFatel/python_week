def subtraction(x,y):
	C=x-y
	print("The grand total is: ", C)

def addition(A,B):
	C=A+B
	print("The grand total is: ", C)

def operation(Func,A,B):
	Func(A,B)

operation(addition,10,20)
operation(subtraction,50,10)