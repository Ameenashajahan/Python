def longest(list2):

    max=len(list2[0])
    temp=list2[0]

    for i in list2:
        if(len(i)>max):
            max=len(i)
            temp=i

    print("Word with longest length is",temp,"length",max)

list1=['Fine','Happy','Friends','Command']
longest(list1)