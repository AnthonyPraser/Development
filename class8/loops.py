'''
Loops
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
6. Write a loop that loops through a string, counts all the letters, and then print how long the
string is.
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.

'''

'''
1. While loops - Run as long as a given condition is true
2. Example - Create a while loop that prints every integer from 1 to 10
'''
# i = 1 # initilization

# while i <= 10: # condition
#     print(i) # output
#     i += 1 # increment by 1

# print("I am out of the loop") # We are out of the loop



'''
3. Create a while loop that will keep asking a user for their user id, until they type 'stop'.
'''
# prompt the user
# user_id = input("User Id:") # If I type stop

# while user_id != "stop": # While the user id is anything but "stop"
#     user_id = input("User Id:")
#     print("This is where we are")

# print("Have a nice day") # This is outside of our while loop






'''
4. Improved login system - Rewrite the username and login program. If the user enters the
incorrect username or login, they will keep receiving a prompt.
'''
# System Id and Password
# sys_id = 'admin'
# sys_password = 'password'

# # Prompt user for credentials
# user_id = input("User id:")
# user_password = input("Password:")

# while sys_id != user_id and sys_password != user_password:
#     print("Incorrect User Id or Password")
#     # reprompt User for credentials, # Will run back to line 64 if incorrect
#     user_id = input("User id:")
#     user_password = input("Password:")


# print("Login Successful, have a nice day!") # When user get correct credentials





'''
5. For Loops - Iterate through strings, lists, tuples, dictionaries, sets....
'for item in collection'
'''

'''
Lets loop through the string "Hello World"

'''
# my_string = 'Hello World'

# for i in my_string: # for item in collection
#     print(i, end=" ")







'''
Lets loop through a list of colors
# my_colors = ['red', 'green', 'orange', 'yellow']
'''
# my_colors = ['red', 'green', 'orange', 'yellow']

# for i in my_colors:
#     print(i)





'''Lets loop through a tuple
my_fav_food = ('pizza', 'subs', 'chicken')
'''
# my_fav_food = ('pizza', 'subs', 'chicken')

# for i in my_fav_food:
#     print(i)

# Ranges range(start, stop, step)

# for i in range(16):
#     print(i)

# for i in range(5, 26):
#     print(i)

# for i in range(0, 30, 2):
#     print(i)




'''
6. Write a for loop that loops through a string, counts all the letters, and then print how long
the string is.
'''
# current_feeling = 'hello'
# i = 0 # our counter

# for c in current_feeling:
#     i += 1 # each time through our string we will increment 1
# print(i) # our output








'''
7. Take a string from the user, verify that it's a number. Write a loop that adds all the digits
together, then print the total.
'''
# test_string = '14253'

# total = 0 # Our running total

# for t in test_string: # We have to test to make sure this is a number
#     if t.isalnum(): # test each character 
#         t = int(t) # cast to our integer
#         total += t # add to total
# print(total) # our output
   







'''
8. Adding conditionals to loops - Write some code that will loop through a string and print
whether each letter is a vowel or a consonant.
'''
# Old solution 
# my_string = 'hello'
# solution = my_string.count('a') +  my_string.count('e') +  my_string.count('i') +  my_string.count('o') +  my_string.count('u')
# print(solution)

# List for reference
# my_vowel_list = ['a', 'e', 'i', 'o', 'u'] # our list collection

# my_vowel_tuple = ('a', 'e', 'i', 'o', 'u') # our tuple collection

# my_vowel_string = 'aeiou' # our string

# my_string = 'hello'

# for letter in my_string:
#     if letter in my_vowel_string:
#         print(letter, "is a vowel")
#     else:
#         print(letter, "is a consonant")



    

    







'''
9. You’re working on a data analysis project for a company that looks at written text. You’re only interested in letters from A-Z because you’re analyzing language. However, the data you’re given has some values that shouldn’t be there.
Write a Python program that takes a string as input from the user, removes anything from the string that isn’t a letter, and prints the new string.
You can loop through the string in a for loop, use the .isalpha() string method, and remember that strings are immutable, so you will have to build a new string from scratch using string concatenation.
'''

test_string = "antBEE123!@#$%&"

# my code
# user_input = input("What is your written text: ")

# for letter in user_input:
#     if letter.isalpha():
#         print(letter, end= "")

# jean code 
new_string = '' # this will be our new string

for t in test_string:
    if t.isalpha(): # checks for anything that is a letter
        new_string += t # if its a letter, concatenate to new_string variable
print(new_string)































