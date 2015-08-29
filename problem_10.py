def median():
	n=int(input("Enter no of test cases: "))
	i=0
	result=[]
	while i<n:
		numbers=[]
		num=input("Enter num: ")
		num=num.strip(" ")
		num=num.split(" ")
		for j in range(0,len(num)):
			numbers.append(int(num[j]))
		numbers=sorted(numbers)#sorting the number list
		median_item=int((len(numbers)+1)/2)
		result.append(numbers[median_item-1])#item index starts from 0
		i+=1
	print("Median:")
	for i in result:
		print(i,end=" ")

median()