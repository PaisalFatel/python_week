try:
	no1=float(input("Enter 1st Number: "))
	no2=float(input("Enter 2nd Number: "))
	result=no1/no2
	print("The result is: ", result)

except ValueError:
	print("404 error")
except ZeroDivisionError:
	print("Can't divide a number by 0")
except Exception:
	print("Try again next year")
finally:
	print("Execute code again m8")