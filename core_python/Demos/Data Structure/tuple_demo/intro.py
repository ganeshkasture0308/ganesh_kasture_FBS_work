#1.structure-denoted by (, )
#tu=(10,)
#print(type(tu))


#2.Heterogenous
tu=(101,'Ganesh kastue','python developer',60000)
print(type(tu))

#3.Ordered
print(tu)

#4.Immutable
#tu[0]=102 #Gives typeerror:item assignment does not support

#5.Faster than list

li=[10,20,30,40]
tu=(10,20,30,40)
import sys
print(sys.getsizeof(li))#bigger blocks of memory
print(sys.getsizeof(tu))#smaller blocks of memory

li=[]
tu=(10,)
print(sys.getsizeof(li))#bigger blocks of memory
print(sys.getsizeof(tu))#smaller blocks of memory
