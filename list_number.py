ones=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
num=int(input("Enter any number"))
answer=""
if num>=1000 and num<=9999:
	answer+=ones[int(num/1000)]+"Thousand"
	num=num%1000
if num>=100:
	answer+=ones[int(num/100)]+"Hundred"
	num=num%100
if num>=20:
	answer+=tens(int(num/10))
if num>0 and num<=19:
	answer+=ones(num)

print(answer)