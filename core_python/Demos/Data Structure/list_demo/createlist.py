#WAP to create list acclording to user
num=int(input("how many elements you want to add in the list:"))
li=[]
for i in range(num):
    ele=int(input("enter the number:"))
    li.append(ele)
print("list:",li)