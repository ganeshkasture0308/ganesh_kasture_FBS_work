#WAP to add element in tuple

tu=(10,20,30,40)
ele=50

li=list(tu)#convert the tuple into list

li.append(50)

tu=tuple(li)#then convert the list into tuple
print(tu)

