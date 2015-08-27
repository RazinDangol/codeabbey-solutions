
def main():
	n=int(input('Enter no of inputs: ' ))
	num=[]
	for i in range(0,n):
		num.append(int(input("Enter {} number: ".format(i+1))))
	print("Sum: ",add_loop(num))

def add_loop(n):
	s=0
	for i in n:
		s+=i
	return s

if __name__=="__main__":
	main()