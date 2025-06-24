#Keyword argument/parameter:
#1.Assign value to parameter in function call.
#2.Flow in right to left.
#3.Skip positional parameter concept.


def employee(id,name,add,sal):
    eData=f'ID:{id}\nNAME:{name}\nADDRESS:{add}\nSALARY:{sal}'
    return eData

print(employee(name="Ganesh kasture",id=1001,add="latur",sal=50000))
print("#############################################################")
print(employee(102,"omkar kasture",sal=45000,add="pune"))
