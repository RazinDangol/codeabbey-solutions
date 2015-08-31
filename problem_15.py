def main():
	answer=[]
	n=int(input('Enter no of test cases: '))
	for i in range(0,n):
		num_list=[]
		data=input("Enter data: ")
		data=data.strip(' ')
		data=data.split(' ')
		for i in data:
			if i== "0":
				break
			else:
				num_list.append(int(i))
		answer.append(round(avg(num_list)))
	print('Answer:')
	for i in answer:
		print(i,end=" ")

def avg(num_list):
	return sum(num_list)/len(num_list)

main()