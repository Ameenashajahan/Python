list=['ameena','devika','vrindha','haritha']
count=0
for i in list:
    for j in i:
        if(j=='a'):
            count=count+1
print("The total number of 'a' in list is ",count)