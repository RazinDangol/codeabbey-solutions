def main():
	n=int(input('Enter no of pairs: ' ))
	pair=[]
	num=[]
	for i in range(0,n):
		for j in range(0,2):
			pair.append(int(input("Enter {} pair {} numbers : ".format(i+1,j+1))))
		num.append(min_loop(pair))
		pair=[]
	j=0
	for i in num:
		print("{} pair min: ".format(j+1),i)
		j+=1

def min_loop(n):
	min=0
	if n[0]<n[1]:
		min=n[0]
	else:
		min=n[1]
	return min

if __name__=="__main__":
	main()