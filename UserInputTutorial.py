# User Input in Python!!!!!

# input() = A function that prompts the user to enter data
            # Always Returns the entered data as a STRING
# Similiar to scan function from Java

# Instead of using a print statment before the function to prompt the user
# what type of info to enter via the keyboard, we can pass in the string as a 
# param to the input function itself.

# Below we are prompting a user to enter their name and have it get stored in
# a string varaible called 'name
name = input("What is you name?: ")

print(f'Your name is {name}')

age = input("How old are you?: ")
print(f'You are {age} years old')

# Remember that the return value of user input functon is always a String.
# If we want to convert an string to an int we can do this as below

age = int(age)
print(type(age))
age+=1 # age = age + 1
print(age)

# Excercise 1 Rectangle Area Calc

# Here we ask for the user to both enter a length and width String ints values
# from the keyboard, convert them into ints and return the area.
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width
print(f'The area is {area} cm')
