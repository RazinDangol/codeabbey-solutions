def main():
	n=int(input('Enter no of pairs: ' ))
	pair=[]
	num=[]
	for i in range(0,n):
		for j in range(0,3):
			pair.append(int(input("Enter {} pair {} numbers : ".format(i+1,j+1))))
		num.append(min_loop(pair))
		pair=[]
	j=0
	for i in num:
		print("{} pair min: ".format(j+1),i)
		j+=1

def min_loop(n):
	min=0
	if n[0]<n[1] and n[0]<n[2]:
		min=n[0]
	elif n[1]<n[0] and n[1]<n[2]:
		min=n[1]
	else:
		min=n[2]
	return min

if __name__=="__main__":
	main()