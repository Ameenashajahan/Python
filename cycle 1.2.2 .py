
list=[]
n=int(input("Enter the number of elements: "))
for i in range(0,n):
    v=int(input("Enter the integer: "))
    if(v>100):
        list.append('over')
    else:
        list.append(v)
print (list)
