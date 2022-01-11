#Formatting like C 

# %s specifier 
name = "Aayush"
print("Hello, %s!" % name)

#double specifier

age = 18 
print("Hi, I am %s, I am %d year old" % (name, age))  
# (name, age) - this is a tuple containing name and age

myList = [1,2,3]
print("A list: %s " % myList)
# 

# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
# 