
#you can take the input as integers also this'
#will work for that also for eg:{1:2,3:4,4:3,2:1,0:0}
y={'alex':1,'xavier':2,'nancy':3,'danny':4} 
                                         
l=list(y.items())   #convet the given dict. into list
#In Python Dictionary, items() method is used to return the list
#with all dictionary keys with values.
l.sort()            #sort the list
print('Ascending order is',l) #this print the sorted list 

l=list(y.items())
l.sort(reverse=True) #sort in reverse order
print('Descending order is',l)

dict=dict(l) # convert the list in dictionary 

print("Dictionary",dict) #the desired output is this sorted dictionary
