def main():
	n=int(input('Enter no of test cases: '))
	result=[]
	for i in range(0,n):
		data=input('Enter weight height: ')
		data.strip(' ')
		data_list=data.split(' ')
		result.append(bmi(float(data_list[0]),float(data_list[1])))
	for j in result:
		print(j,end=" ")

def bmi(weight,height):
	BMI= weight / (height**2)
	if BMI < 18.5:
		return "Under"
	elif BMI >=18.5 and BMI < 25.0:
		return "Normal"
	elif BMI >=25.0 and BMI < 30.0:
		return "Over"
	else:
		return "Obesity"

main()