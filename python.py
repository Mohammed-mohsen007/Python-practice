# print("Hello World")
# print(2+2)
# print(2-2)
# print(2*2)
# print(2/2)
# print(2**3)
# print(5%2)
# print(5//2)
# print((2+3)*4)
# print("Goodbye World")


# print("Variables and Data Types Starts Here")
# # Variables and Data Types in Python
# # Variables are used to store data values.
# # In Python, you don't need to declare the type of a variable; it is inferred from the value assigned.
# # Common data types include integers, floats, strings, and booleans.
# # Example:
# x = 10          # Integer a positive and negative whole numbers without a decimal point and fractional part are know as integers.
# y = 3.14        # Float a number that has a decimal point or is in exponential (scientific) notation are know as floats.
# name = "Alice"  # String a sequence of characters enclosed in single or double quotes are know as strings.
# is_active = True # Boolean a data type that can hold one of two values: True or False are know as booleans. Booleans start with a capital letter in Programming languages like Python.
# list_example = [1, 2, 3, 4, 5] # List an ordered collection of items which can be of different data types are know as lists.
# dict_example = {"key1": "value1", "key2": "value2", "key3": "value3"} # Dictionary a collection of key-value pairs where each key is unique are know as dictionaries.
# tuple_example = (1, 2, 3) # Tuple an ordered collection of items which cannot be changed (immutable) are know as tuples.
# set_example = {1, 2, 3} # Set as unordered collection of unique items are know as sets.

# print(x)
# print(y)
# print(name)
# print(is_active)
# print(list_example)
# print(dict_example)
# print(tuple_example)
# print(set_example)

# name = "Mohsin"
# age = 25
# height = 5.7
# is_student = True
# print("Name:", name , "\nAge:", age, "\nHeight:", height, "\nIs Student:", is_student) 
# # how to define next line in print statement?
# # print("Name:", name + "\nAge:" , str(age) + "\nHeight:", str(height) + "\nIs Student:", str(is_student))
# print("End of Variables and Data Types")

# print("Type Conversion Starts Here")
# # Type Conversion 
# # Type conversion is changing the data type of a value to another data type.
# # Example:
# int_str = "100" # String
# int_num = int(int_str) # Convert string to integer
# float_num = float(int_str) # Convert string to float
# # Why do we need type conversion? Type conversion is necessary when performing operations that require specific data types, such as mathematical calculations or string manipulations.
# # Because user input always comes aa a string, so we need to convert it to the appropriate date type before performing any operations on it.
# # Example of user input conversion:
# # user_age = input("Enter your age: ") # User input is always a string 
# # print("Your age is: " + int(user_age)) # Convert string to integer for display.
# # Common type conversions:
# # str() - Convert to string
# # int() - convert to integer
# # float() - Convert to float
# # boolean() - convert to boolean

# string = "40"
# number_int = int(string) + 5 # Convert string to integer and add 5
# number_float = float(string) + 5.5 # Convert string to float and add 5.5

# age = 25
# age = str(age) # Convert integer to string for display
# print("My age is: " + age)

# # boolean conversion
# print(bool(0)) # False
# print(bool(1)) # True
# print(bool("")) # False
# print(bool("Hello")) # True
# print(bool([])) # False

# # Real life example (Student In)

# print("End of Type Conversion")



# print("Basic Arithmetic Operations Starts Here")
# # Basic Arithmetic Operations
# # Python supports standard arithmetic operations such as addition  (+), subtraction (-), multiplication (*), division (/), exponentiation (**), modulus (%), and floor division (//).
# # Example:
# a = 15
# b = 4
# sum_result = a + b # Addition Example 5 + 2 = 7
# diff_result = a - b # Subtraction Example 5 - 2 = 3
# prod_result = a * b # Multiplication Example 5 * 2 = 10
# div_result = a / b # Division Example 5 / 2 = 2.5
# exp_result = a ** b # Exponentiation Example 2 ** 3 = 2 * 2 * 2 = 8
# mod_result = a % b # Modulus Example 5 % 2 = 1 (Remainder of 5 divided by 2)
# floor_div_result = a // b # Floor Division Example 5 // 2 = 2 (Quotient without the remainder)
# # how Floor Division works
# print(7 // 2)  # Result is 3 because 7 divided by 2 is 3.5, and floor division rounds down to the nearest whole number
# print(8 // 3)  # Result is 2 because 8 divided by 3 is approximately 2.67, and floor division rounds down to 2
# print(9 // 4)  # Result is 2 because 9 divided by 4 is 2.25, and floor division rounds down to 2
# print(10 // 3) # Result is 3 because 10 divided by 3 is approximately 3.33, and floor division rounds down to 3

# print("Arithmetic Additions results")
# print(sum_result)
# print("Arithmetic Subtraction results")
# print(diff_result)
# print("Arithmetic Multiplication results")
# print(prod_result)
# print("Arithmetic Division results")
# print(div_result)
# print("Arithmetic Exponentiation results")
# print(exp_result)
# print("Arithmetic Modulus results")
# print(mod_result)
# print("Arithmetic Floor Division results")
# print(floor_div_result)
# print("End of Basic Arithmetic Operations")

# print("Control Flow Statements Starts Here")
# # Control Flow Statements
# # Control flow statements in Python include conditional statements (if, elif, else) and loops (for, while).
# # Example of conditional statements:
# num = 7
# if num > 0:
#     print(f"{num} is a positive number.") # Why we using f string here? to embed the variable num directly within the string for formatted output. Can we use + operator instead? Yes we can use + operator to concatenate strings and variables.


# import pandas as pd

# # Creating a simple dataset (like a mini spreadsheet)
# data = {
#     'Student': ['Alice', 'Bob', 'Charlie', 'David'],
#     'Score': [85, 92, 78, 95]
# }

# # Convert it into a "DataFrame"
# df = pd.DataFrame(data)

# print("--- Your First DataFrame ---")
# print(df)

# # Calculate the average score
# average = df['Score'].mean()
# print(f"\nThe average score is: {average}")


# import pandas as pd
# import numpy as np
# import requests

# print(f"Pandas version {pd.__version__}")
# print(f"Numpy version {np.__version__}")
# print(f"requests version {requests.__version__}")

# Variables and Data Types in python

# name = "Mohsin" # String a sequence of characters enclosed in single or double quotes are know as strings.
# age = 25 # Integer a positive and negative whole numbers without a decimal point and fractional part are know as integers.
# height = 5.7 # Float a number that has a decimal point or is in exponential notation are know as floats.
# is_student = True # Boolean a data type that can hold one of two values: True or False are know as booleans.
# list_example = [1,2,3,4,5, "Hello"] # List an ordered collection of items which can be of different data types are know as List and are defined using square brackets [].It is mutable, meaning you can change its content after creating it.
# tuple_example = (1,2,3, "Mohsin", 5.7 , True) # Tuple an ordered collection of items which cannot be changed (immutable) are know as tuples and are defined using parentheses ().Tuples are often used to group related data together.
# dict_example = {"key1" : "Value1", "key2": "Value2", "key3": "Value3"} # Dictionary a collection of key-value pairs where each key is unique are know as dictionaries and are defined using curly braces {}.

# print(name)
# print(age)
# print(height)
# print(is_student)
# print(list_example)
# print(tuple_example)
# print(dict_example)

# Creating a Calculator using Two numbers

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# sum_of_two_numbers = "The Addition of Two numbers " + str(int(num1) + int(num2))
# subtraction_of_two_numbers = "The Subtraction of Two numbers " + str(int(num1) - int(num2))
# multi_of_two_numbers = "The Multiplication of Two numbers" + str(int(num1) * int(num2))
# division_of_tow_numbers = "The Division of Two numbers " + str(int(num1) / int(num2))
# floor_of_tow_numbers = "The Floor of Two numbers " + str(int(num1) // int(num2))
# exponentiation_of_two_numbers = "The Exponentiation of Two numbers " + str(int(num1) ** int(num2))
# modulus_of_two_numbers = "The Modulus of Two numbers " + str(int(num1) % int(num2))

# print(sum_of_two_numbers)
# print(subtraction_of_two_numbers)
# print(multi_of_two_numbers)
# print(division_of_tow_numbers)
# print(floor_of_tow_numbers)
# print(exponentiation_of_two_numbers)
# print(modulus_of_two_numbers)

# num1 = 5
# num2 = 10
# # sum_result = "The sum of Two Numbers are:", num1, "+", num2, "=", num1 + num2
# print("The sum of Two Numbers are:", num1, "+", num2, "=", num1 + num2)
# print("The Subtraction of Two Numbers are:", num1, "-", num2, "=", num1 - num2)
# print("The Multiplication of Two Numbers are:", num1, "*", num2, "=", num1 * num2)
# print("The Division of Two Numbers are:", num1, "/", num2, "=", num1 / num2)
# print("The Floor of Two Numbers are:", num1, "//", num2, "=", num1 // num2)
# print("The Modulus of Two Numbers are:", num1, "%", num2, "=", num1  % num2)
# print("The Exponentiation of Two Numbers are:", num1, "**", num2, "=", num1  ** num2)

# string = "5"
# num = 7
# sum_of_result = "The sum of Two Numbers is: " + str(int(string) + num) 
# print(sum_of_result)

# Implicit
# num1 = 5.7
# num2 = 10
# sum_result = num1 + num2
# print(sum_result)
# print(type(sum_result))l

# name = input("Enter Your Name: ")
# print("My name is " + name)

# num1 = input("Enter your first number: ")
# num2 = input("Enter  your second number: ")

# sum_result = int(num1) + int(num2)
# print(sum_result)

# name = input("Enter Your name: ")
# age = input("Enter Your age: ")

# result = name + age
# print("My name is", name, "My age is", age)


# String concatenation 
# asterisk = "* " * 3
# name = input("Enter Your name: ")
# result = asterisk + name + asterisk
# print(result)

# length of string 
# username = input("Enter Your Username: ")
# length = len(username)
# print(length)



