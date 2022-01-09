#list is collection of varying data types

a = ['banana', 10, 1.111, "super banana", 'strange', 5050]
a[1] = a[1] + 1
print(a[1])
a[0:2] = [20, 'banana'] # replace element
print(a)
a[1:1] = ['dream banana', 'dats a banana'] #insert element
print(a)
a[4:] = [] #remove elemnts
print(a) 
a[:0] = a #insert itslef 
print(a) 

print(len(a)) #lenth applies to lists as well as strings

print(a)

a[:] = [] #empty list
print(a)