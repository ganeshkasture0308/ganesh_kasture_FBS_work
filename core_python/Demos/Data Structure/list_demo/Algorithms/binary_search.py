def binarySearch(li,serach_ele):
    beg=0
    end=len(li)-1
    while(beg<=end):
        print("loop executed")
        mid=(beg+end)//2
        if(serach_ele==li[mid]):
            return mid
        elif(serach_ele<li[mid]):
            end=mid-1
        elif(serach_ele>li[mid]):
            beg=mid+1
    else:
        return-1
li=[10,20,30,40,50,60,70]
ele=int(input("enter the element for search:"))
res=binarySearch(li,ele)
if(res!=-1):
    print(f"{ele} is found at {res}.")
else:
    print(f"{ele} is not found in the list.")