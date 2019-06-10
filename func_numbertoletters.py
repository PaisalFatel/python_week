def ones(message):
	word=""
	if message== 1:
		word = "One"
	if message==2:
		word = "Two"
	if message==3:
		word ="Three"
	if message==4:
		word ="Four"
	if message==5:
		word = "Five"
	if message==6:
		word = "Six"
	if message==7:
		word = "Seven "
	if message==8:
		word = "Eight"
	if message==9:
		word ="Nine"
	if message==10:
		word = "Ten"
	if message==11:
		word = "Eleven"
	if message==12:
		word = "Twelve"
	if message==13:
		word ="Thirteen"
	if message==14:
		word = "Fourteen"
	if message==15:
		word ="Fifteen"
	if message==16:
		word ="Sixteen"
	if message==17:
		word ="Seventeen"
	if message==18:
		word ="Eighteen"
	if message==19:
		word = "Nineteen"
	return word

def Tens(Num):
	Result=""
	if Num==20:
		Result="Twenty"
	if Num==30:
		Result="Thirty"
	if Num==40:
		Result="Forty"
	if Num==50:
		Result="Fifty"
	if Num==60:
		Result="Sixty"
	if Num==70:
		Result="Seventy "
	if Num==80:
		Result="Eighty"
	if Num==90:
		Result="Ninety"
	return Result

Num=int(input("Enter any number: "))
Answer=""
if Num>=1000 and Num<=9999:
	Answer+=ones(int(Num/1000))+ "Thousand "
	Num%=1000
if Num>=100:
	Answer+=ones(int(Num/100))+ "Hundred "
	Num%=100
if Num>=20:
	Answer+=Tens(int(Num/10)*10)
if Num>0 and Num<=19:
	Answer+=ones(Num)

print(Answer)