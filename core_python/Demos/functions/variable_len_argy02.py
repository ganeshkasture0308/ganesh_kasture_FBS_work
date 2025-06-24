### Variable length / numbers of argument / parameter
#1.Mention astrick (*) symbol before the parameter in function defination.
#2.Where we can pass multiple vlaues to the function.
#3.store data in tuple.
#4.use for loop to iterate element.


#Wap for multiplication with multiple values.
def multi(*data):
    multip=1
    for ele in data:
        multip=multip*ele
    return multip
res=multi(1,2,3,4,5)
print("multiplication:",res)        
