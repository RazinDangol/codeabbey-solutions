def main():
	answer=[]
	n=int(input('Enter no of test cases: '))
	for i in range(0,n):
		data=input("Enter data: ")
		data=data.strip(' ')
		data=data.split(' ')
		answer.append(digit_sum(int(data[0]),int(data[1]),int(data[2])))
	print('Answer: ')
	for j in answer:
		print(j, end=" ")

def digit_sum(a,b,c):
	s=a*b+c
	result=0
	while s >= 1:
		result+=s%10
		s=int(s/10)
	return result

main()