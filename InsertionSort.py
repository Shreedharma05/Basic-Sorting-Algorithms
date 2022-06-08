def Insertion_Sort(mylist):
    for i in range(1,len(mylist)):
        temp = mylist[i]
        j = i-1
        while temp < mylist[j] and j>-1:
            mylist[j+1] = mylist[j]
            mylist[j] = temp
            j -= 1
    return mylist

print(Insertion_Sort([2,7,3,1,5]))

            
