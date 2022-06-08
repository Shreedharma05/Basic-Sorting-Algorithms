def Bubble_Sort(mylist):
    for i in range(len(mylist)-1,0,-1):
        for j in range(i):
            if mylist[j]>mylist[j+1] :
                temp = mylist[j]
                mylist[j] = mylist[j+1]
                mylist[j+1] = temp
    return mylist

A = [2,7,3,1,5]
print(Bubble_Sort(A))
print(len(A))