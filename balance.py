Itemprice=int(input("Enter your Item price: "))
Given=int(input("Enter amount given: "))
Balance=Given-Itemprice

print("The Balance is therefore: ",Balance)
if Balance%50:
	print("No. of £50",int((Balance - Balance%50)/50))
if Balance%20:
	print("No. of £20",int((Balance%50-Balance%20)/20))
if Balance%10:
	print("No. of £10",int(((Balance%20-Balance%10)/10)))
if Balance%5:
	print("No. of £5",int((Balance%10-Balance%5)/5))
if Balance%2:
	print("No. of £2",int(((Balance%5-Balance%2)/2)))
if Balance%1:
	print("No. of £1",int(((Balance%2-Balance%1)/1)))

print("This is your Balance")