def linearSearch(li,serch_ele):
    for i in range(len(li)):
        if(li[i]==serch_ele):
            return i
    else:
        return-1
li=[10,30,50,67,37,89,34,90]
ele=int(input("enter the number for search:"))
res=linearSearch(li,ele)
if(res!=-1):
    print(f"{ele} is found at index {res}.")
else:
    print(f"{ele} is not found in the list.")

