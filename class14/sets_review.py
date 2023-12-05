'''
Fun Facts about Sets

-unordered, unchangeable*, and unindexed.
* The items are unchangeable, but you can add and remove items.
Sets do not allow duplicates, so they are used to store a set of unique values. You use curly brackets for sets: { }
Because sets are unordered, you can't index them like a list. They don't have indexes at all. You can still loop through a set with a for loop.

'''

# Create a set


# What am I?


# Pass in a list
my_fav_colors_list = ['green', 'blue', 'red']


# Unordered
my_unordered_set = {'blue', 'green', 'red', 'orange'}


# Unchangeable
my_unchangeable_set = {'hello', 'welcome', 'to', 'newyork'}


# Unindexed
my_unindexable_set = {'I', 'cant', 'be', 'indexed'}

# Break up a string
first_name = set('jean')

first_name = {'jean'}


# No duplicates allowed
my_cars = {'chevy', 'toyota', 'ford', 'ford', 'honda', 'honda'}


# No duplicates - How did we solve this problem before?

'''
8. Exercise: Removing All Duplicates
You have a list storing important data for your company, but it contains some duplicate entries. 
Go through your list and remove all the duplicates. When you're done, each item should appear in 
the list exactly once.
'''
''' With a for loop and appending'''

#original list
states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']

# # this will capture our unique states
states_no_duplicates = []

'''we will loop through states, and append only the first occurence of each state into our empty list'''

# for s in states:
#     if s not in states_no_duplicates:
#         states_no_duplicates.append(s)
# print(states_no_duplicates)

''' With sets and returning a list '''

states = ['alaska', 'alaska', 'alaska', 'alabama', 'alabama', 'new york', 'new york', 'new york']


# We can loop through sets
top_ten_movies = {'shawshank redemption', 'avatar', 'avengers', 'its a wonderful life'}

# Lets look at some methods

# Let's add silver .add()
colors = {'blue', 'green', 'red'}


# Lets clear all our items .clear()
transportation = {'cars', 'bikes', 'plane'}


# Lets create a copy into a set called comedy .copy()
sitcoms = {'friends', 'seinfeld', 'honeymooners'}


# Remove vermont from our set
states = {'california', 'new york', 'vermont', 'connecticut'}



# Difference - What's different? -
student_set = {'judith', 'majestic', 'samuel'}
student_set_2 = {'judith', 'majestic', 'mike'}

# Intersect - What do we have in common? &
my_schedule = {'mon', 'wed', 'thurs'}
majestik_schedule = {'wed', 'fri', 'sat'}


# Union - All pets that appear in any set  |
reynelles_pets = {'dog', 'cat', 'bird'}
julie_samuels_pets = {'chickens', 'dog', 'fish'}
kat_pollans_pets = {'bird', 'dog', 'fish'}
majestic_pets = {'turtle'}


# Symmetric difference - Items outside of matching items ^
robins_books = {'catcher in the rye', 'richest man in babylon'}
anthonys_books = {'catcher in the rye', 'richest man in babylon', 'sounder'}

'''
Exercise - Sets
You work for a sales company and must generate a set of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
You have a set of customers over 60, and a set of customers who have made at least 5 purchases. Use a set operation to output a set of customers that fit both criteria for the discount. You can do this in one line of code.
Example:
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}
Output: {'Dominic', 'Simone'}
'''

# Solve with 1 or 2 lines of code
over_60_years = {'Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf'}
over_5_purchases = {'Finn', 'Simone', 'Aaron', 'Dominic'}


'''
Exercise - Sets
You work at a company where some people know Python, some people know JavaScript, and some people know both.
In a loop, prompt the user to input an employee name, whether they know Python, and whether they know JavaScript. Use this to build two sets: a set of employees that know Python, and a set of employees that know JavaScript.
Use set operators to compute the following sets:
The set of employees that know both Python and JavaScript
The set of employees that know JavaScript, but not Python
The set of employees that know Python or JavaScript, but not both
'''

# Framework for my comments

# My set variables

# User input variables

# Error messages

# User Instructions

# Loop

    # Input

    # Conditionals & Logic
  
    # Output
    













































