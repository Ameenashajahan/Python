
#pyramid with step numbers accepted from user

n=int(input("Enter no: of steps:"))
for i in range(1,n+1):
    for j in range(1,1+i):
        print(i*j,end=" ")
    print()