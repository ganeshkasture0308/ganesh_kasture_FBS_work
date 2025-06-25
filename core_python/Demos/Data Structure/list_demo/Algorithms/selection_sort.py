def selectionSort(li):
    size=len(li)
    for i in range(0,size-1):
        index=i
        for j in range(i+1,size):
            if(li[j]<li[index]):
                index=j
        li[i],li[index]=li[index],li[i]
    return li
li=[60,40,70,80,10,50,20,30]
li=selectionSort(li)
print("Selection list:",li)