#1.using slicing method
str='Hello word!'
print(str[::-1])
print(str[-12:-4:-1])
print(str[-12::-1])


#2.reverse the word without using slicing
str="Hello world"
str2=' '
for i in str:
    str2=i+str2
print(str2)