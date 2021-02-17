c=int(input("Enter the current Year:\n"))
f=int(input("Enter the Year you want To stop:\n"))
print("The Leap years are")
for c in range(c,f+1):
	if (c%4==0 and c%100!=0 or c%400==0):
		print(c)