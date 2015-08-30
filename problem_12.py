def dice(random_num):
	n = int(random_num * 6)
	return n+1
def main():
	result=[]
	n = int(input("Enter no of test cases: "))
	for i in range(0,n):
		random_num=float(input("Enter random number: "))
		result.append(dice(random_num))
	print("answer: ")
	for j in result:
		print(j,end=" ")
main()

