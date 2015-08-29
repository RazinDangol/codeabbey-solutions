def tempConvert():
	celsius=[]
	temp=input("Enter temp: ")
	fahrenheit=temp.strip(" ")
	fahrenheit=fahrenheit.split(" ")
	amount=int(temp[0])
	for i in range(0,amount):
		celsius.append(round((int(fahrenheit[i+1])-32)/1.8))
	#printing on same line
	print("Celsius:",end=" ")
	for i in celsius:
		print(i,end="\t")
tempConvert()
