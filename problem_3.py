
def main():
	n=int(input('Enter no of pairs: ' ))
	pair=[]
	sum=[]
	for i in range(0,n):
		for j in range(0,2):
			pair.append(int(input("Enter {} pair {} numbers : ".format(i+1,j+1))))
		sum.append(add_loop(pair))
		pair=[]
		j=0
	for i in sum:
		print("{} pair sum: ".format(j+1),i)
		j+=1

	

def add_loop(n):
	s=0
	for i in n:
		s+=i
	return s

if __name__=="__main__":
	main()