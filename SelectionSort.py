def Selection_Sort(mylist):
    for i in range(len(mylist)-1):
        min_index = i
        for j in range(i+1,len(mylist)):
            if mylist[j]<mylist[min_index]:
                min_index = j
        if i!= min_index:
            temp = mylist[i]
            mylist[i] = mylist[min_index]
            mylist[min_index] = temp
    return mylist

A = [2,7,3,1,5]
print(Selection_Sort(A))

