
def stringreplace(str1):
    firstchar = str1[0]
    str2 = str1[1:].replace(firstchar, "$")
    print(firstchar + str2)
str1=input("Enter a String: ")
stringreplace(str1)