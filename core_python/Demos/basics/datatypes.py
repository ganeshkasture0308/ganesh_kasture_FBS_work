#data types:
#1.Numeric 

# 1.int(interger)
# x=10
# print(type(x))

# 2.float(floating point)
# x=3.14
# print(type(x))
# 3.complex .(it is used for scientific purpose )
# x=10+5j
#print(type(x))

#2.Text
#1.str(string)
# str1='Firstbit solutions 1234@.'
# str2="Firstbit solutions"
# str3="student's data"
# str4='Quote:"This is money"'
# str5='''this is first line.
# this is second line.'''
# str6="""This is first line.
# This is second line."""
# print(type(str1))
# print(str1)
# print(type(str2))
# print(str2)
# print(type(str3))
# print(str3)
# print(type(str4))
# print(str4)
# print(type(str5))
# print(str5)
# print(type(str6))
# print(str6)


#3.Sequential 
#1.list
# li=[10,20,30,40,50]
# print(type(li))
# print(li)

#2.tuple
# tu=(10,20,30,40,50,60)
# print(type(tu))
# print(tu)

#3.range()
# obj=range(1,10)
# print(type(obj))
# print(obj)


#4.mapping

#1.dict(dictionary)
dict={
    1:"python",2:"java",3:"web programming",4:"php"
}
print(type(dict))
print(dict)

#5.set

#1.set
s1={10,20,30,40}
print(type(s1))
print(s1)

#2.frozenset
s1=frozenset({10,20,30,40})
print(type(s1))
print(s1)

#6.Boolean

#1.True
a=True
print(type(a))
print(a)

#2.Flase
a=False
print(type(a))
print(a)

#7.None

x=None
print(type(x))
print(x)

#8.Binary

#1.bytes
x=b'firstbit'
print(type(x))
print(x)

#2.bytearray
x=bytearray(b'firstbit')
print(type(x))
print(x)



#3.memoryview
x=memoryview(b'firstbit')
print(type(x))
print(x)
