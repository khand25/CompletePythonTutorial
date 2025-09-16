import math #import the math module to use more math functions
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
friends = 5
friends = friends + 1 #add 1 to friends
friends += 1 #add 1 to friends using shorthand operator (augmented assignment operator)
friends = friends -2 #subtract 2 from friends
friends -= 2 #subtract 2 from friends using shorthand operator (augmented assignment operator)
friends = friends * 3 #multiply friends by 3
friends *= 3 #multiply friends by 3 using shorthand operator (augmented assignment operator)
friends = friends / 2 #divide friends by 2 (result is a float and not an int like in Java or C++)
friends /= 2 #divide friends by 2 using shorthand operator (augmented assignment operator)
friends = friends **2 #raise friends to the power of 2
friends **= 2 #raise friends to the power of 2 using shorthand operator (augmented assignment operator)
#friends = friends % 3 #get the remainder of friends divided by 3
friends = 25
remainder = friends % 3 #get the remainder of friends divided by 3 and store it in a variable (using modulus operator)
print(remainder)
print(friends)

# Bulit in math functions
# notice that in Python, we can assign any data type to any variable
# We dont need to declare the data type of a variable like in Java or C++
x = 3.14
y = -4
z = 5
result = round(x) #rounds x to the nearest integer
print(result)
result = abs(y) #gets the absolute value of y
print(result)
result = pow(z, 3) #raises z to the power of 3
print(result)
result = max(x,y,z) #gets the maximum value of x, y, z
print(result)
result = min(x,y,z) #gets the minimum value of x, y, z
print(result)
#import math #import the math module to use more math functions
print(f"The value of pi is: {math.pi}")  #prints the value of pi
print(math.e) #prints the value of e
result = math.sqrt(16) #gets the square root of 16 and returns it as a float
print(result)
print(f"X value: {x}")
print(f"X using math.ceil: {math.ceil(x)}") #rounds x up to the nearest integer
x = 9.9
print(f"X using math.floor: {math.floor(x)}") #rounds x down to the nearest integer

# Math excerises
# Calculuate circumference of a circle
# formula: C = 2 * pi * r
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference,2)}") #rounds the circumference to 2 decimal places
# Calculate area of a circle
# formula: A = pi * r^2
area = math.pi * math.pow(radius,2)
print(f"The area of the circle is: {round(area,2)}") #rounds