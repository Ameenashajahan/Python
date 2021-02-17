
# Python program to find the greatest of three numbers using if-else statement
num1 = int (input("Enter the number1:"))
num2 = int (input("Enter the number2:"))
num3 = int (input("Enter the number3:"))
if (num1 >= num2) and (num1 >= num3):
 largest = num1
elif (num2 >= num1) and (num2 >= num3):
 largest = num2
else:
 largest = num3
print("The largest number is",largest )