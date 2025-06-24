#swapping  of two numbers using third variable
x=10
y=20

z=x
x=y
y=z

#display output
print("x is:",x,"y is:",y)

#swapping of two numbers without using third variable
#take input
x=40
y=80

#perform operation
y=y+x
x=y-x
y=y-x
#display output
print("x is:",x,"y is:",y)


#swap two numbers using python 
x=20
y=40
x,y=y,x
print("x is:",x,"y is:",y)
