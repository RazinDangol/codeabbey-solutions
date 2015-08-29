def MinMax():
	array=list(input("Enter numbers separated by space: "))
	num=[]
	for n in array: #Removing the blank spaces and appending to list num
		if n != " ":
			num.append(n)
	#Assuming the minimum and maximum to be the first element/item of the list num
	max=int(num[0])
	min=int(num[0])
	print(num)
	for  i in range(0,len(num)):
		for j in range(i+1,len(num)):
			if max < int(num[j]):
				max=int(num[j])
			elif min > int(num[j]):
				min=int(num[j])
			else:
				pass
	print("Max: ",max)
	print("min: ",min)


MinMax()