### keyword length/number of argument /parameter. 
#1.we assign multiple values with parameter in function call.
#2.Mention two astrick(**) symbols before parameter name in function defination.
#3.Data stored in dictionary.

def employee(**data):
    for i ,j in data.items():
        print(i,":",j)
employee(id=101,name="Ganesh",sal=55000)
