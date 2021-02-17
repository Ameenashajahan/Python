list=[]
vowel=['a','e','i','o','u']
string=input("enter a string:\t")
for i in string:
	if (i in vowel) and (i not in list):
		list.append(i)
print("vowels present in the string ",list)