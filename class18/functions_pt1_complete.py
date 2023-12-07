import my_modules
import re
import math

'''
Exercise - We will create 2 functions. One function will take your first and last name as arguments and return your full name. The second function will determine if a number is odd or even and return a boolean. Lets import our functions into a new file and use them there. 
'''

# with print
# my_modules.full_name('Jean', 'Juste')
# odd_or_even = my_modules.even_num(6)

# with return
# print(my_modules.full_name('Jean', 'Juste'))
# print(my_modules.even_num(5))

# print(mm.full_name('Jean', 'Juste'))
# print(mm.even_num(5))



'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
# our function
# def is_a_vowel(word):
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             print("I am a vowel")
#         else:
#             print("I am not a consonant")

# shorter version
# def is_a_vowel(word):
#     vowels = 'aeiou'
#     for w in 'aeiou':
#         print("I am a vowel") if w in vowels else print("I am a consanant")

'''
Example
Write a function that returns the surface area of a box (rectangular prism).
Surface Area = width*2 + length*2 + height*2
'''

# def surface_area_box(w, l, h):
#     surface_area = (2*l*w) + (2*l*h) + (2*w*h)
#     return surface_area

# print(surface_area_box(4, 3, 1))

'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''

# def surface_area_sphere(radius):
#     surface_area = 4 * math.pi * radius**2
#     return surface_area

# print(surface_area_sphere(4))


# Lets break these two functions down 

# def get_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     return out

# my_word = 'strawberries'
# get_vowels(my_word) # doesnt print anything, function returns out
# print(get_vowels(my_word)) # prints return value


# def print_vowels(word):
#     out = ''
#     for letter in word:
#         if letter in "aeiou":
#             out += letter
#     print(out)

# my_word = 'strawberries'
# print_vowels(my_word) # executes function that ends with a print statement
# print(print_vowels(my_word)) # first our function prints our vowels, next our print built in function prints return value of None

# Lets see how it shows a none without a return
# def show_none(word):
#     print(word)

# print(show_none('hello'))




''' 
Exercise
Write a function that takes a list and a value, and removes the value until it no longer exists in the list.
Return how many times the value was removed.
'''

# def cleanup_list(cleanup_list, value):
#     counter = 0
#     while value in cleanup_list:
#         cleanup_list.remove(my_value)
#         counter += 1
#     print(counter)


# my_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# my_value = 5

# cleanup_list(my_list, my_value)










'''
Suppose you work for a bank, and you have a list of transactions with the following information for each one: customer ID, transaction amount, and transaction type (deposit or withdrawal).
Write a function that takes in the list of customer transactions and returns a dictionary where the keys are the customer IDs and the values are the total transaction amounts for each customer.
Example:

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]
     Output: {'a': 50, 'b': 350}
'''

transactions = [{'id': 'a', 'amount': 500, 'type': 'deposit'},\
                {'id': 'b', 'amount': 350, 'type': 'deposit'},\
                {'id': 'a', 'amount': 450, 'type': 'withdrawal'}]


def get_user_transactions(transactions):
    ''' Get our user transactions'''
    output = {} 
    # Separate ID's
    cust1 = [i for i in transactions if (i['id'] == 'a')] 
    cust2 = [i for i in transactions if (i['id'] == 'b')]

    # Transaction Totals
    transaction_total_cus_1 = sum(s['amount'] for s in cust1 if (s['type'] == 'deposit')) - sum(s['amount'] for s in cust1 if (s['type'] == 'withdrawal')) 
    transaction_total_cus_2 = sum(s['amount'] for s in cust2 if (s['type'] == 'deposit')) - sum(s['amount'] for s in cust2 if (s['type'] == 'withdrawal')) 

    # Update and return dictionary
    output.update({"a": transaction_total_cus_1})
    output.update({"b": transaction_total_cus_2})
    return output

print(get_user_transactions(transactions))







































