def wsd(num):
	result=0
	while num >= 1:
		result+=num % 10 *len(str(num))
		num=int(num/10)
	return result
def main():
	answer=[]
	n=int(input('Enter no of test cases: '))
	values=input("Enter values: ")
	values=values.strip(" ")
	values=values.split(" ")
	for i in range(0,n):
		answer.append(wsd(int(values[i])))
	print("answer: ")
	for j in answer:
		print(j,end=" ")
if __name__=="__main__":
	main()