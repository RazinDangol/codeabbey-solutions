seed=113
limit=10000007

def main():
	num_list=[]
	n=int(input('Enter no of test cases: '))
	data=input("Enter data: ")
	data=data.strip(' ')
	data=data.split(' ')
	for i in range(0,n):
		num_list.append(int(data[i]))
	print('Answer:')
	print(checksum(num_list))

def checksum(num_list):
	result=0
	for i in num_list:
		result=(result+i)*seed
		result=result%limit
	return result

main()