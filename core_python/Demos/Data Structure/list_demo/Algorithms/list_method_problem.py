#nested list problem, Wap to calculate addition of nested list.
li=[[10,20,30],[40],[50],[60]]
add=0
for sub_li in li:
    for ele in sub_li:
        print(ele)
        add+=ele
print("the addition of all elements is:",add)
