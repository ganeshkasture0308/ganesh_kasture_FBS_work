for i in range(5,0,-1):
    for j in range(1,i+1):
        if(i==5 or j==1 or i==j):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    #or

    

for i in range(1,6):
    for j in range(1,7-i):
        if(i==1 or j==1 or j==6-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()