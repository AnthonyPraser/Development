import statistics

# Functions Part 2

# With documentation and type hinting (optional)

# def my_function(country: str = 'Norway') -> None:
#     '''Print out user's country

#     -country - user's country
    
    
#     '''
#     print("I am from", country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


'''
Exercise
Write a function called center that returns either the mean or median of a list of numbers.
This function should take two parameters: A list of numbers, and an optional parameter called use_median which should default to False.
If use_median is False, return the mean of the list.
If use_median is True, return the median of the list.
Test your function by calling it with different arguments.
'''

'''No documentation or type hinting'''

def center(my_list, use_median=False):
    if use_median == False:
        result = statistics.mean(my_list)
        return result
    else:
        result = statistics.median(my_list)
        return result





test_list1 = [1,2,2,2,3,4,5,6,7,8]
test_list2 = [3,6,7,9,10,11,2]

# print(center(test_list1)) # 4
# print(center(test_list2)) # 6.85


# '''Documentation, type hinting, shorthand if-then-else'''

def center(my_list: list, use_median: bool=False) -> float:
    '''Return mean and median of list

    -my_list: calculate mean and median from collection
    -use_median: optional, boolean to default to mean
    
    
    '''
    return statistics.mean(my_list) if use_median == False else statistics.median(my_list)

# print(center(test_list1)) # 4
# print(center(test_list2)) # 6.85

# print(center(test_list1, True))
# print(center(test_list2, True))




# Returning multiple values


def get_vowels_and_consonants(word):
    vowels = ''
    consonants = ''
    for letter in word:
        if letter in 'aeiou':
            vowels += letter
        elif letter in 'bcdfghjklmnpqrstvwxyz':
            consonants += letter
    return vowels, consonants

vowels, consonants = get_vowels_and_consonants("apple")

# print(vowels)
# print(consonants)


'''
Exercise
Write a Python function called get_stats that takes in a list of numbers and returns the following three values: The mean, the median, and the mode of the list.
Call the function on a list, and print each statistic on a separate line.
my_list = [1,2,4,5,5]
Output:
Mean: 3.4
Median: 4
Mode: 5
'''

my_list = [1,2,4,5,5]

def get_stats():
    















    '''Global variables'''

x = 'challenging'
def change_x():
    x = 'fun'

change_x()
# print("Programming is", x)


x = 'challenging'
def change_x():
    global x
    x = 'fun'
    
change_x()
# print("Programming is", x)

'''
A lambda is a small anonymous function. It can take any number of arguments, but it can only have one expression, which is returned.
Syntax: lambda arguments : expression
'''

# Function to add two numbers
def add_two(x,y):
    return x + y

# print(add_two(2,3))

add_two_lambda = lambda x,y : x + y
# print(add_two_lambda(2,3))
# print((add_two_lambda)(2,3))

# Written as a Lambda


# Write the following functions as Lambdas

# def greeting(fname):
#     print(f'Hello, {fname}')

# greeting("Sally")

# greeting = lambda fname : f"Hello, {fname}"
# print(greeting("Sally"))


# def double_me(num):
#     return num + num

# print(double_me(500))

# double_me = lambda num : num + num
# print(double_me(500))


'''
Exercise
Write a lambda that computes the n-th power of a number, given two arguments, num and n.
Now, write a function that is equivalent to the lambda.
'''
# def to_the_power(x: int, y: int) -> int:
#     '''return n-th power of a number '''
#     return pow(x,y)
    
    
# print(to_the_power(5,3))





# to_the_power = lambda x,y :  pow(x,y)
# print(to_the_power(5,3))


''' Higher Order Functions
These are functions that may accept a function as an argument or return a function as its output. In Python, reduce(), map() and filter() are some of the most important higher-order functions. When combined with simpler functions, they can be used to execute complex operations.

filter - The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not. 

map - returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

'''
# Let's use filter() to find the even numbers in a list 
# filter(fun, iter)

def even_number(n):
    return n % 2 == 0

# print(even_number(3))

lambda n : n % 2 == 0  # True or False for an even number
my_list = [0,1,2,3,4,5,6,7,8,9,10]

even_num_filter = filter(lambda n : n % 2 == 0, my_list)
# print(list(even_num_filter))



# Let's use map() to multiply every value in this list by 3
# map(fun, iter)




    

triple_me = [0,1,2,3,4,5,6]

def multiply_by_three(n: float) -> float:
    '''return 3x the parameter'''
    return n * 3

# print(multiply_by_three(3))

lambda n : n * 3






# Lambda with sort
# sorted(iterable, key=lambda, reverse=True/False)


students = [{"name":"Kim","grade":98},
            {"name":"Joe","grade":65},
            {"name":"Ted","grade":93},
            {"name":"Keisha","grade":80},
            {"name":"Torrie","grade":65},
            {"name":"Simon","grade":78}]

students_by_name = sorted(students, key = lambda s: s['name'], reverse = True)
students_by_grade = sorted(students, key = lambda s: s['grade'], reverse = True)

# print(students_by_name)
# print(students_by_grade)


'''
Assignment 6
Write a simple function that returns a person's net worth. Here are your requirements:
Docstring which includes what function does and information on your parameters (brief)
Function name - net_worth
parameters - assets, liabilities
Must contain type hinting for the parameters as well as what the function will be returning
Call the function in a print statement with needed arguments
'''

def net_worth(assets: float, liabilities: float) -> float:
    '''Function for figuring out someones net worth through their 
    assets and liabilities'''
    
    return assets - liabilities

print(net_worth(1500, 800))









































