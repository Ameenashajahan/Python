list=[]
n=int(input("enter the limit:\t"))
print("enter the nos:")
for i in range(0,n):
	no=int(input())
	list.append(no)
for i in list:
	a=i*i
	print("the square of ",i," =",a)