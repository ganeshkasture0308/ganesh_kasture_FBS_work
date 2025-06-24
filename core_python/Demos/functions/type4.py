#with passing parameter with returing values.

def greet(name):
    str=f'welcome,{name}!'
    return str

nm=input("enter the name:")
output=greet(nm)
print(output)