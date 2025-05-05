# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0.
# calculate_area_triangle(7, 3) should return 10.5.
#
# Define your function and call it below.
def calculate_area_triangle(base, height): # Base and height are the parameters of the function
    if base <= 0 or height <= 0: # Check if base and height are positive numbers and greater than zero
        return "Error: Base and height must be positive numbers." # Return an error message if not
    
    area = (base * height) / 2 # Calculate the area using the formula
    return area # Return the computed area of the triangle

print('Exercise 1:', calculate_area_triangle(10, 5)) # output: 25.0 (which is a float)
print('Exercise 1:', calculate_area_triangle(7, 3)) # output: 10.5 (which is a float)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula (principal * rate * time) / 100.
#
# Examples:
# simple_interest(1000, 5, 2) should return 100.
# simple_interest(1500, 3.5, 5) should return 262.5.
#
# Define your function and call it to see the result.
def simple_interest(principal, rate, time): # Principal, rate and time are the parameters of the function

    if principal <= 0 or rate <= 0 or time <= 0: # Check if principal, rate and time are positive numbers and greater than zero
        return "Error: Principal, rate and time must be positive numbers."
    
    interest = (principal * rate * time) / 100 # Calculate the simple interest using the formula provided
    return interest # Return the computed simple interest

print('Exercise 2:', simple_interest(1000, 5, 2)) # output: 100.0 (which is a float)
print('Exercise 2:', simple_interest(1500, 3.5, 5)) # output: 262.5 (which is a float)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.
#
# Examples:
# apply_discount(100, 25) should return 75.
# apply_discount(80, 10) should return 72.
#
# Define your function and call it to display the discounted price.
def apply_discount(price, discount_percent): # Price and discount are the parameters of the function
    if price < 0:
        return "Error: Price must be a positive number."
    if discount_percent < 0 or discount_percent > 100:
        return "Error: Discount percentage must be between 0 and 100."
    
    discount_amount = (price * discount_percent) / 100 # Calculate the discount amount

    final_price = price - discount_amount # Calculate the final price after applying the discount

    return final_price # Return the final price after discount

print('Exercise 3:', apply_discount(100, 25)) # output: 75.0 (which is a float)
print('Exercise 3:', apply_discount(80, 10)) # output: 72.0 (which is a float)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.
# The formula for converting Celsius to Fahrenheit is (Celsius * 9/5) + 32.
# The formula for converting Fahrenheit to Celsius is (Fahrenheit - 32) * 5/9.
#
# Examples:
# convert_temperature(0, 'C') should return 32.0.
# convert_temperature(32, 'F') should return 0.0.
#
# Define the function and then call it below.

def convert_temperature(temperature, unit): # Temperature and unit are the parameters of the function
    
    unit = unit.upper() # Convert the unit to uppercase to handle both 'C' and 'c' or 'F' and 'f'

    if unit == 'C':
        converted = (temperature * 9/5) + 32 # Convert Celsius to Fahrenheit 
    else:
        converted = (temperature - 32) * 5/9 # Convert Fahrenheit to Celsius
    
    return round(converted, 1) # Return the converted temperature rounded to one decimal place

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C')) # output: 32.0 (which is a float)
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F')) # output: 0.0 (which is a float)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n and returns the sum of all integers from 1 to n.
#
# Examples:
# sum_to(6) should return 21.
# sum_to(10) should return 55.
#
# Define the function and then call it below.
def sum_to(n): # n is the parameter of the function
    if n < 1: # Check if n is a positive integer; ensure the user doesn't enter a negative number or zero
        return "Error: Please enter an integer greater than or equal to 1."

    total = n * (n + 1) // 2 # Calculate the sum using the formula n * (n + 1) / 2; // is integer division to avoid getting a float
    return total # Return the computed sum

print('Exercise 5:', sum_to(6)) # output: 21 (which is an integer)
print('Exercise 5:', sum_to(10)) # output: 55 (which is an integer)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments and returns the largest of them.
#
# Examples:
# largest(1, 2, 3) should return 3.
# largest(10, 4, 2) should return 10.
#
# Define your function and test it with different inputs.
def largest(a, b, c): # a, b and c are the parameters of the function
    return max(a, b, c) # Use the built-in max function to find the largest number among a, b and c

print('Exercise 6:', largest(1, 2, 3)) # output: 3 (which is an integer)
print('Exercise 6:', largest(10, 4, 2)) # output: 10 (which is an integer)

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.
#
# Examples:
# calculate_tip(50, 20) should return 10.
#
# Write your function and test its output below.



# print('Exercise 7:', calculate_tip(50, 20))

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers, multiplies them, and returns the product.
# Review your notes on *args for handling an arbitrary number of arguments.
#
# Examples:
# product(-1, 4) should return -4.
# product(2, 5, 5) should return 50.
#
# Define the function and call it with different sets of numbers to test.



# print('Exercise 8:', product(2, 5, 5))

# -----------------------------------------------------------------------------------------------------------------------

# Exercise 9: Basic Calculator
#
# Create a function named `basic_calculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basic_calculator(10, 5, 'subtract') should return 5.
# basic_calculator(10, 5, 'add') should return 15.
# basic_calculator(10, 5, 'multiply') should return 50.
# basic_calculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.



# print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
# print('Exercise 9 Result:', basic_calculator(10, 5, "add"))
# print('Exercise 9 Result:', basic_calculator(10, 5, "multiply"))
# print('Exercise 9 Result:', basic_calculator(10, 5, "divide"))

# -----------------------------------------------------------------------------------------------------------------------



