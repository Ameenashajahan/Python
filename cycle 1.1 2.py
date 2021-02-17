list=[]
n=int(input("enter the no of element:\t"))
print("enter the nos:")
for i in range(0,n):
	no=int(input())
	list.append(no)
print("The elements are \n",list)
print("the positive nos are\n")
for i in list:
	if(0<i):
		print(i)