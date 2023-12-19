import math



''' Compile time errors / static errors'''
# print('wed) SyntaxError: unterminated string literal (detected at line 6)
# print("Have a nice day!" SyntaxError: '(' was never closed
# if x = 10: SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
# if x == 10 SyntaxError: expected ':'



''' Exceptions / Runtime errors'''



''' ValueError '''
# print(float("testing")) ValueError: could not convert string to float: 'testing'
# print(math.sqrt(-5)) ValueError: math domain error
# fname, lname, middlename = 'fritz', 'lewis' ValueError: not enough values to unpack (expected 3, got 2)



''' AttributeError '''
# num = 10
# num.append(5) AttributeError: 'int' object has no attribute 'append'


# str1 = 'hello'
# str1.append('there') AttributeError: 'str' object has no attribute 'append'




''' NameError '''
# print(x) NameError: name 'x' is not defined

# for i in range(c):
#     print(i) NameError: name 'c' is not defined
 

''' TypeError '''
# color = 'blue'
# age = 25
# result = color + age TypeError: can only concatenate str (not "int") to str

# car = 'chevy'
# car() TypeError: 'str' object is not callable

# fav_animals = ['dog', 'cat', 'bird']
# index_value = '1'
# print(fav_animals[index_value]) TypeError: list indices must be integers or slices, not str

# for i in 155:
#     print(i) TypeError: 'int' object is not iterable

# def add_num(num1, num2):
#     return num1 + num2

# num1 = 5
# num2 = 'hello'




# print(add_num(num1, num2)) TypeError: unsupported operand type(s) for +: 'int' and 'str'

# i = 2
# while i > 0:
#     i += 1
#     print(i) KeyboardInterrupt





# Lets prevent a user from dividing by zero
# numerator = int(input("Please enter your numerator: "))
# denominator = int(input("Please enter your denominator: "))

# quotient = numerator / denominator
# print(quotient)


# Lets implement a try, except, than test

# Try, except, and else, than test

# numerator = int(input("Please enter your numerator: "))
# denominator = int(input("Please enter your denominator: "))

# try:
#     quotient = numerator / denominator
# except ZeroDivisionError:
#     print("Sorry, you cannot divide by zero")
# else:
#     print(quotient)
# finally:
#     print("This will run no matter what, you can use this to do cleanup")


# lets implement try catch


# userin = input("Enter a number: ")
# num_list = []

# try:
#     num_list.append(float(userin))
# except ValueError:
#     print("Must enter a number")
# else:
#     print(num_list)
    




'''
Exercise - Handling Invalid User Input
Write a Python program that takes a customeris age as user input and determines whether they're eligible for a senior discount.
Sometimes the age might not be in the correct format. Handle this using try-except, and print a descriptive error message if the age can't be cast to an int.
If the age is greater than or equal to 65, the customer is eligible for the discount. Otherwise, they're not eligible. Print whether the customer is eligible or not.

'''

# customers_age = int(input("Enter age please: "))
# if customers_age >= 65:
#     print("Eligible for discount")
# else:
#     print("Not eligible for discount")



''' Exercise 

You can add a finally block that will be executed regardless if the try block raises an error. 
This is good for cleaning up resources, because it will always be run.

'''

# def append_user_input(lis):
#     try:
#         # Tries to add a float to a list
#         lis.append(float(input("Enter a number: ")))
#     except ValueError:
#         # What to do if the user input can't be cast to a float
#         print("Invalid input")
#         return None
#     finally:
#         # This gets run no matter what, even if
#         # the function returns in the except block
#         print("your list:", lis)

# lis = []
# append_user_input(lis)


''' Exercise - Raising exceptions
Write a program to take the square root of user input.
Use a try-except statement to ensure the user inputs a float.
If the user inputs a negative number, raise a ValueError that will also be caught by the except statement. Make sure to write a descriptive message in the exception you raise.
'''

# Propogating exceptions (functions)



# Function that calculates average of two numbers


'''
Exercise
You have been assigned the task of creating a sales tax calculator for an e-commerce company. Write a Python function called calculate_final_price that takes the price of a product and the sales tax rate, and return the final price including tax.
The price should be a positive number, and the tax rate should be between 0 and 1 (exclusive). If either of them are outside of the valid range, raise a custom ValueError with an appropriate error message.
Now, test your implementation by asking the user to input a product price and sales tax rate, and call your function. Catch any potential ValueError raised by the function.
'''





















































