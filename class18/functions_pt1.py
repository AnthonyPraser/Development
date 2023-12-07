import mymodules
import math




'''
Exercise - We will create 2 functions. One function will take your first and last name as arguments and return your full name. The second function will determine if a number is odd or even and return a boolean. Lets import our functions into a new file and use them there. 
'''
# calling functions with return
# print(mymodules.full_name('joe', 'smith')) # calling the function from the other file
# print(mymodules.even_num(8))


# calling functions with print
# mymodules.full_name('joe', 'smith') # calling the function from the other file
# mymodules.even_num(7)





'''
Exercise
Write a function that will loop through a string and print whether a character is or is not a vowel.
'''
# def vowel(word):
#     ''' Is it a vowel or not? '''
#     vowels = 'aeiou'
#     for w in word:
#         if w in vowels:
#             print(f"{w} is a vowel")
#         else:
#             print(f"{w} is a consanant")

# vowel('hello')




'''
Example
Write a function that returns the surface area of a box (rectangular prism).
Surface Area = (2*l*w) + (2*l*h) + (2*w*h)
'''

# def surface_area(l, w, h):
#     surface_area_1 = (2*l*w) + (2*l*h) + (2*w*h)

#     return surface_area_1

# surface_area(5,10,5)

# def surface_area_box(width, length, height):
#     ''' Find the surface area of a box '''
#     surface_area = (2*length*width) + (2*length*height) + (2*width*height) 
#     return surface_area

# print(surface_area_box(4, 3, 1))





'''
Exercise
Write a function that returns the surface area of a sphere.
Surface Area = 4 * pi * radius^2
'''

# def finding_pi(radius):
#     Surface_Area = 4 * math.pi * radius ^ 2
#     return Surface_Area

# print(finding_pi(10))



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


# def remove_and_count(my_list, my_value):
#     ''' Remove values from list and return a count '''
#     counter = 0
#     while my_value in my_list:
#         my_list.remove(my_value)
#         counter += 1
#     return counter

    
# my_list = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5]
# my_value = 2

# print(remove_and_count(my_list, my_value))






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


def get_user_transaction(transactions):
    ''' Get totals for user transaction '''
    output = {}

    # Separate our ID's
    cust1 = [i for i in transactions if (i['id'] == 'a')]
    cust2 = [i for i in transactions if (i['id'] == 'b')]
    
    #
    transaction_total_customer_1 = sum(s('amount') for s in cust1 if (s['type']) == 'deposit') - sum(s('amount'))
    pass

get_user_transaction(transactions)







































































