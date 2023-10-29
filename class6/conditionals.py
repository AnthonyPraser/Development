# Code in if runs

# x = 20
# y = 15
# if x > y:
#     print(x)

# Code in if does not run

# x = 20
# y = 20
# if x > y:
#     print(x)

# Find odd or even

# num = 99
# print(num % 2) # if the result is 1, the number is odd, if the result is o the number is even

# user_input = (input("What is your number? "))
# user_input = 9.2

# user input is a string

# if '.' in user_input:
#     print("Unknown")
# elif (int(user_input % 2)) != 0:
#     print("This is odd")
# elif (int(user_input % 2)) == 0:
#     print("This is even")



# else If (Elif) Statements

# x = 40
# y = 40

# if x > y:
#     print("x is bigger")
# elif y > x: # in case y is bigger
#     print("y is bigger")
# else:
#     print("They are the same")

# Ternary Operators
# x = 20
# y = 30

# result = "X is bigger" if x > y else "Y is Bigger" if y > x else "They are the same"
# print(result)



# user_input = input("What is your input? ")

# if user_input == int:
#     print("This is a number")
# if user_input == str:
#     print("This is a word")
# else:
#     print("This is something else")

# Input
# user_input = input("What is your input? ")

# if user_input.isdigit(): # test for a number
#     print("This is a number")
# elif user_input.isalpha(): # test for a word
#     print("This is a word")
# else:
#     print("This is something else")

# our temperature
# temp_f = 75

# if temp_f > 70:
#     print("It's hot outside!")
# elif temp_f > 40:
#     print("It's moderate outside")
# else:
#     print("It's cold outside")


# temp_f = 35

# if temp_f > 70:
#     print("It's hot outside!")
# if temp_f > 40:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")


# temp_f = 45

# if temp_f > 70:
#     print("It's hot outside!")
# if temp_f > 40 and temp_f <= 70:
#     print("It's moderate outside")
# if temp_f <= 40:
#     print("It's cold outside")

# me = "I Exist"
# if me:
#     print("I exist")


# not > and > or

# print(True or False and False) # and gets evaluated firat
# print((True or False) and False) # parenthesis take precedence


# x = True
# print(not x)

# print(not (False or True))



# Nested Conditionals

# num = 5

# if num % 2 == 1:
#     if num < 10:
#         if num > 0:
#             print("This is a single-digit odd number.")


# num = 5

# if num % 2 == 1 and num < 10 and num > 0:
#     print("This is a single-digit odd number.")


# Exercise

# Variable
user = "Anthony Prasertsinh"
passw = "Hello World!"

# User input
username = input("What is your username? ")
password = input("What is your password? ")

# Conditionals
if username == user and password == passw:
    print("Login successful")
    
else:
    print("Login not successful")


# Login System
# username_input = input("Username: ")
# password_input = input("Password: ")

# # Get username and password
# username = "admin"
# password = "password"

# # logic for check
























