name = 'Danyal'

# To get the length or total number of chracters in a String use the len function
print(name)
# To get the length or total number of characters in a String use the len function
print(len(name))
# find function is used to determine if a char is present in a String and if so,
# then the first index occurence of that character or substring is returned.
# if not present, then -1 is returned

print(name.find('y'))
print(name.find('z'))
# Used to ONLY capitlize the first letter of the String it is called upon
print(name.capitalize())
# Used to MAKE THE ENTIRE STRING ALL IN CAPS!
print(name.upper())
# Used to make string in lower case letters!
print(name.lower())
# return true if the String contains only String numbers! False otherwise
print(name.isdigit())
number = "123"
print(number.isdigit())
# Returns true is the string contains only letters and no whitepsaces or special characters or numbers
print(name.isalpha())
# Counts total number of frequencys of substring or character passed in as
# an argument to the count function
print(name.count("a"))
# replace each first argument charater with the second argument character
print(name.replace("a","o"))
print(name)
# concateneate the same String with each other n number of times where n
# is the number after the '*' sign 
print(name*12)