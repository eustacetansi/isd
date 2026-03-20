# Section 2: First Program in Python
# In this exercise, you will write a Python program that allows the user to convert temperatures from
# Celsius to Fahrenheit and Kelvin.
# Your Task is to look at the following requirements and implement the program in the file called
# temperature_converter.py.
# Requirements:
# • The user stores the Celsius value as a number in a variable called celsius_input
# • The Celsius value then gets converted to Fahrenheit and stored in a variable called
# degree_f
# • The Celsius value then gets converted to Kelvin and stored in a variable called degree_k
# • (Note: Use the internet to find out the formulas on how to convert C to K and F and
# implement that using Python operators
# • Generate and print an output that follows the following format:

print("Welcome to Temperature Converter")

#obtaining the data
celsis_input = float(input("Enter a temperature in celsis:"))

#converting to Fahrenheit
degree_f = (celsis_input * 9/5) + 52

#converting to kelvin
degree_k = celsis_input + 273.15

print(f"The temperature you have entered is {celsis_input} degree Celsis")
print("Converted temperatures")
print(f"{celsis_input} degree celsius is equal to {degree_f} Fahrenheit")
print(f"{celsis_input} degree celsius is equal to {degree_k} Kelvin")

print("Thank you for using this Temperature Converter")