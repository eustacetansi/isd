#Exercise 1 task: variable and types
var_1 = True #type = bool
var_2 = 1 #Type = int
var_3 = 3.14159 #Type = float
var_4 = "Hello Word" #Type = string

print(type(var_1))
print(type(var_2))
print(type(var_3))
print(type(var_4))


# 1. Create a variable called my_int and assign it the value 5.
# 2. Create a variable called my_float and assign it the value 5.5.
# 3. Create a variable called my_bool and assign it the value True.
my_int = 5
my_float = 5.5
my_bool = True
# 4. Print the value of each variable.
print(my_int)
print(my_float)
print(my_bool)

# 5. Cast my_int to a float and store the result in a variable called my_int_float.
# 6. Cast my_float to an integer and store the result in a variable called my_float_int.
# 7. Cast my_bool to an integer and store the result in a variable called my_bool_int
my_int_float = float(my_int)
my_float_int = int(my_int)
my_bool_int = float(my_bool)
# 8. Print the value of each variable.
#print(my_int)
print(my_int_float)
print(my_float_int)
print(my_bool_int)


# Exercise 2: Arithmetic Operators
#Exercise 2 Arithmetic operators
result_addition = 10 + 5
print("Addition:", result_addition)

#subtraction
result_subtraction = 20 - 8
print("Subtraction:", result_subtraction)

#Multiplication
result_multibplication = 6 * 4
print("Multiplication:", result_multibplication)

#Division
result_division = 15 / 3
print("Division:", result_division)

#Floor division
result_floor_division = 17 // 4
print("Floor Division:", result_floor_division)

#Modulus
result_modulus = 17 % 4
print("Modulus:", result_modulus)

#Expontiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)


#Task 2: Calculating the Average: 
# 1. Create two variables, num1 and num2, with any numeric values.
# 2. Calculate their average using the arithmetic operators and assign it to a variable called average.
# 3. Print a message that displays the values of num1, num2, and the calculated average.
num1 = 10
num2 = 20
average = (num1 + num2) / 2
print("Average of ", num1, num2, " = ", average)

# Task 3: Calculate the Area of a Rectangle:
# 1. Create two variables, length and width, representing the dimensions of a rectangle.
# 2. Calculate the area of the rectangle using the arithmetic operators and assign it to a variable
# called area.
# 3. Print a message that displays the values of length, width, and the calculated area.
length = 15
width = 20
area = length * width
print("The Area  of a triangle with length and width as ", length, " ", width, "respectively is ", area)


# Exercise 3: Strings and f-Strings
# f-Strings allow for easy string formatting. Strings are objects in Python, and you can use methods on them.


# Task 1: Modify Strings
# 1. Create a new variable called my_string and store the following in it: “This class covers ISD.”
# 2. Print the my_string variable

my_string = "This class covers ISD"
print(my_string)
# 3. Using the documentation in the link above, look through the examples and do the following:
# a. Create a new variable my_uppercase_string that stores the my_string converted to
# uppercase
# b. Create a new variable my_lowercase_string that stores the my_string converted to
# lowercase
# c. Create a new variable my_new_string that replaces the word “ISD” in the string with
# “Interactive Software Design”.
# d. Create a new variable my_string_length that stores the length of the string (Note: use a
# search engine or the lecture slides to help you how to do this).
my_uppercase_string = my_string.upper()
my_lowercase_string = my_string.lower()
my_new_string = my_string.replace("ISD", "Interactive Software Design" )
print(my_uppercase_string)
print(my_lowercase_string)
print(my_new_string)

# Task 2: f-Strings
# 1. Create variables called my_name, number_of_classes, campus. Store your name, the number of
# classes you are taking this term and then the campus you are studying at.
# 2. Create an f-string using the instructions above called my_text that combines the text to the
# following scheme. (Example: my_name = Peter, number of classes = 10, campus = Paisley):
# “My name is Peter and I am studying 10 classes in Paisley”.
# 3. Print the string, run the program, and ensure that you have done everything correctly.
my_name = "Eustace Nnolum"
number_of_classes = 3
campus = "Paisely"
my_text = f"My name: {my_name}; Number of classes: {number_of_classes}; Campus: {campus}"
print(my_text)

