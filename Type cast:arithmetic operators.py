# Type cast and arithmetic operators tutorial!

#type casting = convert the data type of a value to another data type
x = 1 #int
y = 2.0 #float
z = "3" #str
w = "hello"
#w = int(w) #error as we can't direclty convert a string of characters to an integer

# Type cast y to an int using the int() function
y = int(y)
print(x)
print(y)
print(z)
#print(w)
# But we can use the int function to convert a string of numbers to an integer. 
# Similar to Integer.parseInt() in Java!
z = int(z)
print(type(z))
x = float(x) #type cast x to a float using the float() function
y = float(y) #type cast y to a float using the float() function
z = float(z) #type cast z to a float using the float() function
print(x)
print(y)
print(z)
# Lets use the str() function to type cast x, y, z to strings
x = str(x)
y = str(y)
z = str(z)
# In python we can concatenate strings using the + operator but not with other data types
# Use f-strings or the str() function to convert other data types to strings
#print("X is:" + float(x)) #concatenate string with string
print(f"X is: {float(x)}")

### Arithmetic operators
