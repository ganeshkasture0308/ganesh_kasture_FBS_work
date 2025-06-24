### Variable length / numbers of argument / parameter
#1.Mention astrick (*) symbol before the parameter in function defination.
#2.Where we can pass multiple vlaues to the function.
#3.store data in tuple.
#4.use for loop to iterate element.

def add(*data):
    sum=0
    for ele in data:
        sum=sum+ele
    return sum
res=add(10,20,30,40,50)
print("Addition is:",res)


