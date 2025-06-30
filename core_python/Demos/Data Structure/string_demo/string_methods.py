str='FirstBit Solutions'
#str='123'
#str='
print(str.capitalize())#captitalize only first letter of the string.
print(str.count('Bit'))#count how many time its occur.
print(str.endswith('ions'))#does it ends with these letters.
print(str.find('x'))#find the index of the letter .if it is not found it return -1.
print(str.find('t')*5)#index of t is 4 so 4*5 =20
print(str.index('Bit'))#return the starting index ony. is b=5 so it rreturn 5.
#print(str.index('Bits'))
print(str.isalnum())#there is the space in the word so it is showing flase alphanumeric or numeric.
print(str.isalpha())
print(str.isdigit())
print(str.islower())
print(str.isspace())
print(str.isupper())
print(",".join(['a','b','c']))# , is a separator
print(str.lower())
print(str.replace('Bit',"Bytes"))
print(str.replace(" ","_"))
print(str.split(" "))#seperate the values in list format
print(str.startswith("Firs"))#starting values are correct or not
str2='   FirstBit Solutions  '
print(str2.strip(' '))#reoves the extra space in the string . and also remove the world or letter in the sting
print(str.strip("FirstBit"))
print(str.swapcase())#it covert upper letter in to lower and lower letters into upper.
print(str.title())
print(str.upper())
