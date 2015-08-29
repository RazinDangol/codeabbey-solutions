def vowelCount():
	n=int(input("Enter no of test cases: "))
	vowel=['a','e','i','o','u']
	data=[]
	count=[]
	for i in range(0,n):
		data.append(input("Enter data: "))
	i=0
	for words in data:
		count.append(0)#initializing the count list for respective counting of the given test cases
		for word in words:
			if word in vowel:
				count[i]+=1
		i+=1
	print("answer:")
	for i in count:
		print(i,end=" ")#for printing in same line separated by space
vowelCount()

