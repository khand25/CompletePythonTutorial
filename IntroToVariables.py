# Variable = A container for a value (string, integer, float, boolean)
# A variable behaves as if it is the value it contains

# In python, we do not have to explicitly declare the datatype of a variable
# as Python interpepter is not storngly typed langauge (varaibles can change datatypes later)
# and not explicltiy typed as well.
# Python will automatically infer the datatype of a variable based upon the value
# it is assigned to

# String variables
first_name = "Danyal"
food = "pizza"
email = 'danyalrkhan@gmail.com'
# Integers variables (variables that store whole numbers)
age = 23
quantity = 3
num_of_students = 30

# Floats variables

price = 10.99
gpa = 3.91
distance = 5.5

# Boolean variables
is_student = True
am_tall = False

print(first_name)

# We can use 'f' Strings or format strings to better integrate variables values
# into string literals

# Example below
print(f'Hello my name is {first_name}')
print(f'You like {food}')
print(f'Your email is: {email}')
print(f'You are {age} years old')
print(f'You are buying {quantity} items')
print(f'Your class has {num_of_students} students')
print(f'The price is ${price}')
print(f'Your GPA is: {gpa}')
print(f'You ran {distance} km')
print(f'Are you a student: {is_student}')
print(f'Are you tall: {am_tall}')

# Typecasting Tutorial

# Typecasting = the process of converting a varaible from one datatype to another
# str(), int(), float(), bool()

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

# below print statment will print out the datatype of the variable being passed in 
# as an arugment to the type function
print(type(age))
print(type(name))
print(type(is_student))

# We can manually typecast a varaible to another datatype by using the datatype
# varaible functions
# below we are typecasting a float varaible (gpa) into a int version (gpa)
gpa = int(gpa)
print(f'Your gpa is: {gpa}')
age = float(age)
print(f'Your gpa is: {age}')

age = str(age)

print(type(age))

name = bool(name)
print(name)

# if we typecast a String into a boolean, like above, then the result of the
# boolean varible will always be True. UNLESS THE STRING PEREVIOSULY WAS EMPTY RESULTING
#IN A FALSE VALUE