a,b = 0,1
while b < 69: #while loop - stays true until the condition is met. If b >= 69 loop will break 
    print(b)
    a, b = b, a+b

a, b = 0,1 
while b < 1000:
    print(b, end = ' ') #end prevents creating a new line, just adds a space
    a, b = b, a+b
