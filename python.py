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

# String Indexing 
# username = "Mohammed Mohsin"
# first_letter = username[0] # in this we are printing first letter from username
# print(first_letter)
# last_letter = username[-1] # in this we are printing last letter from username
# print(last_letter)

# Exercise 1
# write a program that reads a single line of input and print the given input

# word = input("Enter Your words: ")
# print("You have taken Input =>", word)

# Exercise 2
# write a program that reads a word and prints the word and "###" should be print on two different lines take user input.

# word = input("Enter Your Input")
# hashed = "#"
# print(word)
# print(hashed * 3)

# Exercise 3
# Write a program that reads the tow words and prints the two words on tow lines

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")
# print(word1) 
# print(word2)

# Exercise 4 
# For this problem, you need to write code to read two lines of input and print the second line of input.

# word1 = input("First word: ")
# word2 = input("Second word: ")
# print(word2)

# Exercise 5 
# Write a program that reads two lines of input and prints 
# those two lines in the reverse order. 
# (Print the message given in the second line of input before the first line of input)

# word1 = input("First word: ")
# word2 = input("Second word: ")
# print(word2)
# print(word1)

# Exercise 6 
# Write a program that takes a word W as input and prints "Hello" followed by the given word W.

# w = input("Enter Your name: ")
# w2 = "Hello "
# print(w2 + w)

# Exercise 7
# For this problem, you need to write code to read 
# a single line of input and print the line after the message "Given input: ".

# word1 = input("Write Given Input: ")
# word2 = input("Write your message: ")
# result = word1 + word2
# print(result)

# Exercise 8
# Write a program that reads two words and prints the resultant word by joining the two words.

# word1 = input("first word: ")
# word2 = input("second word: ")
# result = word1 + " " + word2
# print(result)

# Exercise 9 
# A job applicant is filling out an application form. 
# He entered his first name and last name. 
# Your task is to print his full name by joining his first name and last name with a space.

# first_name = input("Enter Your first name: ")
# last_name = input("Enter Your last name: ")
# full_name = first_name + " " + last_name
# print(full_name)

# Exercise 10
# write a program that reads the name and age of a person and print them in the given format.
# Mohsin is 25 years old.

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# result = name + " is " + age + " years old." 
# print(result)

# Exercise 11
# write a program that reads input and print three times in single line.

# word = input("Enter the word you want to print 3 times: ")
# result = (word + " ") * 3
# print("the enter word is printing 3 time => " + result)

# Exercise 12 
# write a program the returns simple squares using asterisk (*)

# asterisk = "* " * 2
# print(asterisk)
# print(asterisk)

# Exercise 13 
# print a triangle using asterisk (*)

# asterisk = "* " 
# print(asterisk)
# print(asterisk * 2)

# Exercise 14
# Write a program that reads a word and prints the word in "* * * word * * *" format.

# word = input("Enter your word: ")
# asterisk = "* " * 3
# result = asterisk + word + " " + asterisk
# print(result)

# Exercise 15
# Write a program that reads a word and prints the first character of the word.

# word = input("enter your word: ")
# result = word[0]
# print(result)

# Exercise 16
# take a input and write a program that print a third character of the input.

# word = input("enter your word: ")
# third_character = word[2]
# print(third_character)

# Exercise 17 
# Give four digit number as N input, and write a program to print first and last digit number in two lines.

# number = input("Enter the three digit number: ")
# first_digit = number[0]
# last_digit = number[-1]
# print(first_digit)
# print(last_digit)

# Exercise 18
# take an two digit number as input, and reverse that digit like if input is 12 print 21.

# number = input("Enter the two digit number: ")
# reverse_digit = number[1] + number[0]
# print(reverse_digit)

# Exercise 19
# Take an input from the user and find out the length of the input.

# word = input("enter the word: ")
# length_word = len(word)
# print(length_word)

# Exercise 20
# take an input and print the number of asterisk as input length, like "Mohsin" length is 6 print ****** like that.

# username = input("enter the name: ")
# length_of_username = len(username)
# asterisk = "* " * length_of_username
# print(asterisk)

# Exercise 21
# take an input and print input length -1 like input is (Mohsin and length of the Mohsin is 6 if 6 - 1 = 5)

# username = input("enter the name: ")
# length_of_username = len(username)
# result = length_of_username - 1
# print(result)

# Exercise 22 
# take a input and print the last character of the input

# word = input("Enter the word and it will print last character of the input: ")
# length_of_word = len(word) - 1
# print("The last index of word is: ", length_of_word)

# Exercise 23
# take a input and print the last character of the input

# word = input("enter you word: ")
# last_character_of_word = word[-1]

# Exercise 24
# Take an Input and write a program that reads a word and prints the length of the word excluding the first and last character.
# The output should be an integer excluding the first and last character of the word
# Example "Mohsin" length is 6, 6-2 is 4 

# word = input("enter your word: ")
# length_of_word = len(word)
# result = length_of_word - 2
# print(result)

# Take a Input and wright a program that reads a word and print first letter of the 
# given word as (*) instead of the other letter.
# Example Mohsin => M***** 

# word = input("enter the word: ") # Mohsin
# length_of_word = len(word) -1
# first_letter_of_word = word[0]
# asterisk_of_remaining_word = "*" * length_of_word
# result = first_letter_of_word + asterisk_of_remaining_word
# print(result)

# word = input()
# result = word[0] + (len(word) - 1)* "*"
# print(result)

# Take a Input and write a program that reads a word and print a half of the word the output should be integer
# Example Mohsin length is 6 half of 6 is 3 the output should be 3.0 and try to make 3

# word = input("enter your word: ")
# length_of_word = len(word) / 2
# print(length_of_word)

# Assignment 1

# Q1 Write a program that prints simple Rectangle using Asterisk (*)

# asterisk = "* "
# print(asterisk * 2)
# print(asterisk * 2)
# print(asterisk * 2)

# Q2 Write a program that prints simple Square shape using Asterisk(*)

# asterisk = "* " * 3
# print(asterisk)
# print(asterisk)
# print(asterisk)

# Q3 Write a program that prints simple Triangle Using Asterisk (*)

# asterisk = "* "
# print(asterisk)
# print(asterisk * 2)
# print(asterisk * 3)
# print(asterisk * 4)

# Q4 Take an input as word and print the word as given format ****** Python ****** and **** Code ****

# word = input("enter the word: ")
# length_of_word = len(word)
# asterisk = ("*" * length_of_word) + " " + word + " " + ("*" * length_of_word)
# print(asterisk)

# Q5 Take Two inputs as words the second input word1 and word2 and print the index of word1 where the word2 ends the output should be Integer.
# Example Midterm is word1 and Mid is word2 Mid last index is 2 so the output should be 2, One-Thousand and One-

# word1 = input("first word: ")
# word2 = input("second word: ")
# length_word2 = len(word2) -1
# print(length_word2)

# Q6 Take a Two Inputs A and B and reverse the inputs with separated by ###
# Example A is Cat B is Rat reverse it and print
# Rat 
# ###
# Cat

# a = input("first word: ")
# b = input("second word: ")
# hash = "###"
# print(b)
# print(hash)
# print(a)

# Q7 Take a Input and print the first letter and the last letter of the word.

# word = input("enter your word: ")
# first_letter_of_word = word[0]
# last_letter_of_word = word[-1]
# print(first_letter_of_word)
# print(last_letter_of_word)

# Q8 Take Three Strings as Input and print first character of each string in same line.

# string1 = input("first string: ")
# string2 = input("second string: ")
# string3 = input("third string: ")

# string1 = string1[0]
# string2 = string2[0]
# string3 = string3[0]
# result = string1 + string2 + string3
# print(result)

# Q9 Take an input as word and print first and last letter character from the word 
# Example (Mohammed is the input the output should be M******d).

# word = input("enter the word: ")
# first_character_of_word = word[0]
# last_character_of_word = word[-1]
# length_of_word = len(word) -2
# asterisk = "*" * length_of_word
# result = first_character_of_word + asterisk + last_character_of_word
# print(result)

# String Slicing 

# What is String Slicing?
# Obtaining a part of a string is called string slicing.
# Syntax of string slicing.
# variable_name[start_index : end_index]
# Starts from the start_index and stops at end_index
# end_index is not included in the slice 

# Example 
# message = "Hello World"
# part = message[0 : 5]
# print(part) # the output is "Hello"

# Slicing to End: If end index is not specified slicing stops at the end of the string.

# Example
# message = "Hello World"
# part = message[5 : ]
# print(part) # the output is World

# Slicing from start: If start index is not specified, slicing start from the index 0.
# Example 
# message = "Hello World"
# part = message[ : 5]
# print(part) # the output is Hello

# Checking Data Types: Check the datatype of the variable or value using type()
# Example 
# print(type("string")) # type of string
# print(type(10)) # type of integer
# print(type(float)) # type of float
# print(type(True)) # type of boolean


# Type Conversion 

# What is Type Conversion?
# Converting the value of one Date Type to another Data Type is know as Type Conversion or Type Casting.
# We can convert 
# String to Integer
# Integer to Float 
# Float to String and so on..

# String To Integer Conversion
# int() convert valid data of any value into Integer
# Example 

# a = "5"
# a = int(5)
# print(a)

# Invalid Integer Conversion

# a = "Five"
# a = int(a)
# print(a) # ValueError: invalid literal for int()

# Adding two numbers 
# a = input("enter the number")
# b = input("enter the number")
# a = int(a)
# b = int(b)
# result = a + b
# print(result)

# Note Whenever we are taking input by default it is string. If we don't convert the number with integer the output should be different.
# Example 
# a = input() # take input as 10
# b = input() # take input as 10
# result = a + b 
# print(result) # the output will come 1010 
# # This will do string Concatenation 

# Summary 
# int() => convert into integer DT
# str() => convert into string DT
# float() => convert into float DT
# bool() => convert into boolean DT


# coding practice 

# Exercise 1
# Take a two inputs as number and print the sum of two numbers

# num1 = input("first number: ")
# num2 = input("second number: ")
# result = int(num1) + int(num2)
# print(result)

# Exercise 2
# Take a two inputs as number and do the division of the two numbers

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# result = num1 / num2
# print(result)

# Exercise 3 
# Write a program to calculate the area of the rectangle.
# Note: Area of Rectangle = length of rectangle * Breadth of rectangle 
# take input as length is 10 and breadth is 2

# length = int(input("enter the length of the rectangle: "))
# breadth = int(input("enter the breadth of the rectangle: "))
# area_of_rectangle = length * breadth
# print(area_of_rectangle)

# Exercise 4 
# Write a program to calculate a perimeter of rectangle.
# Note: the formula is p=2(l+w)

# length = int(input("enter the length of rectangle: "))
# breadth = int(input("enter the breadth of rectangle: "))
# perimeter_of_rectangle = (length + breadth) * 2
# print(perimeter_of_rectangle)

# Exercise 5 
# Take two inputs as numbers and print division of two numbers (num1 / num2) the output should be an integer

# num1 = int(input("enter first number: "))
# num2 = int(input("inter second number: "))
# division_of_two_numbers = num1 / num2
# print(int(division_of_two_numbers))

# Exercise 6
# Take two inputs as float and print subtraction of two float numbers (num1 - num2 ) the output should be and float.

# num1 = float(input("enter the float number: "))
# num2 = float(input("enter the float number: "))
# subtract_of_two_numbers = num1 - num2
# print(float(subtract_of_two_numbers))

# Exercise 7 
# Take an input of total class strength and total girls strength and print the percentage of boys.

# class_strength = int(input("Enter the class strength: "))
# girls = int(input("enter girls strength: "))
# percentage_of_boys = class_strength * girls / 100
# percentage_of_boys = int(class_strength - girls)
# print(percentage_of_boys)

# Exercise 8
# Take two inputs as float and print the sum of two numbers as given format Sum: 7.0

# num1 = float(input())
# num2 = float(input())
# sum_of_two_numbers = num1 + num2
# print("Sum: " + str(sum_of_two_numbers))


# Exercise 9
# Write a program to take the number of kilometers as input and convert into meters and print the number of meters.
# Note: 1 Kilometer = 1000 Meters

# kilometers = float(input("enter the kilometers: "))
# meters = 1000
# result = int(kilometers) * meters
# print(result)

# Exercise 10 
# Write a program that reads input as Dividend and Divisor and print the output Remainder.

# dividend = int(input("Enter the dividend number: "))
# divisor = int(input("Enter the divisor number: "))
# quotient = int(dividend / divisor)
# remainder = dividend - (quotient * divisor)
# print(remainder)


# Exercise 11
# Take a input as three digit number and print the sum of three digit number.

# num = input("enter the three digit number: ")
# first_digit = int(num[0])
# second_digit = int(num[1])
# third_digit = int(num[2])
# sum_of_three_digits = first_digit + second_digit + third_digit
# print(sum_of_three_digits)

# Exercise 12
# Take a two inputs one is String of greater than 10 letters and another is single digit integer and print the letter of string as integer taken.

# string = input("enter the string: ")
# integer = int(input("Enter the single digit number: "))
# result = string[integer]
# print(result)

# Exercise 13
# Take a two input one is string and another is integer print a word as number of times on integer.

# word = input("Enter the word: ")
# integer = int(input("enter the number: "))
# repetition = word * integer
# print(repetition)

# Exercise 14
# Write a program that reads single line of input and print the first three letters of the input.

# word = input("Enter the word: ")
# first_three_characters = word[0 : 3]
# print(first_three_characters)

# Exercise 15
# Take an string input of > 10 and integer of single digit print the last characters of string using starting index as given integer.
# Example "Unhappy" => is string, "2" is Integer the output is happy.

# string = input("enter the string: ")
# integer = int(input("enter the integer: "))
# last_characters_of_string = string[integer : ]
# print(last_characters_of_string)

# Exercise 16
# Write a program that reads a word and two indices (X, Y) and 
# prints a part of the word from the index X to the index Y.
# Note string should be > 15 characters and the indices should be single digit.

# word = input("enter the words: ")
# first_index = int(input("enter the first index: "))
# second_index = int(input("enter second index: "))
# part_of_word = word[first_index : second_index ]
# print(part_of_word)

# Exercise 17 
# Write a program that reads a word and a number N and prints the first N characters of the word.

# word = input("Enter the 10 words: ")
# num = int(input("enter the single digit number: "))
# part_of_word = word[ : num]
# print(part_of_word)

# Exercise 18
# Write a program that reads a word and a number N and prints the last N characters of the word.
# Example Forgive bring output give

# word = input("Enter Forgive: ")
# num = int(input("enter input as 4: "))
# length_word = len(word) - num
# part_of_word = word[length_word : ]
# print(part_of_word)

# Exercise 19
# Write a program that reads a string and prints the first part of the string that has numbers.The output should be integer.

# word = input("take string as 10y: ")
# length_of_word = len(word) - 1
# first_part_of_string = word[ : length_of_word]
# print(first_part_of_string)

# Coding Practice 1F