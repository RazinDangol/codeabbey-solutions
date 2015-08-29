def rounding():
	n=int(input("Enter no of test cases: "))
	dividend=[]
	divisor=[]
	for i in range(0,n):
		dividend.append(int(input("Enter dividend: ")))
		divisor.append(int(input("Enter divisor: ")))
	for i in range(0,n):
		print(round(dividend[i]/divisor[i]))

rounding()
