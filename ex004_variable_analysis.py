variable = input("Enter something: ")

print(f"The primitive type is: {type(variable)}")
print(f"Does it contain only spaces? {variable.isspace()}")
print(f"Is it a number? {variable.isnumeric()}")
print(f"Is it a alphabetic? {variable.isalpha()}") # Return False if contains spaces
print(f"Is it alphanumeric? {variable.isalnum()}")
print(f"Is it uppercase? {variable.isupper()}")
print(f"Is it lowercase? {variable.islower()}")
print(f"Is it capitalized? {variable.istitle()}")