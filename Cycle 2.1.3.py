                  # The sum of all items in a list 
 
total = 0
 #creating a list
list1=[]
n=int(input("Enter no of items:"))
for i in range(0,n):
    list1.append(int(input("Enter items")))
print("List is :",list1)
print("Length of list",len(list1))
for i in range(0,len(list1)):
    total = total + list1[i]
#main
print("Sum of all items in a list is",total)