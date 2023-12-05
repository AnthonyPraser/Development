import statistics

''' Lists Containing Other Lists '''

# Exercise - Months of the year

first_quarter = ['january', 'february', 'march'] 
second_quarter = ['april', 'may', 'june'] 
third_quarter = ['july', 'august', 'september'] 
fourth_quarter = ['october', 'november', 'december'] 

year = [first_quarter, second_quarter, third_quarter, fourth_quarter]
# print(year)

# Access february with indexing
# print(year[0][1])

# # Access june with indexing
# print(year[1][2])

# # Access july with indexing
# print(year[2][0])

# # Access october with indexing
# print(year[3][0])


''' *** '''
''' *** '''

# Lets loop through rows and columns

year = [
    ['january', 'february', 'march'], 
    ['april', 'may', 'june'], 
    ['july', 'august', 'september'], 
    ['october', 'november', 'december']
    ]

# Accessing rows
# for rows in year:
#     print(rows)


# Accessing columns
# for rows in year: # accessing rows
#     for columns in rows: # accessing columns
#         print(columns, end=' ') # printing the column items
#     print() # looks like a carriage return



''' *** '''
''' *** '''

# Lets practice some more indexing

my_super_list = [
    ['superman', 'wonderwoman','batman'],
    ['spiderman','captain america','ironman'],
    ['aquaman']]

# # Create a variable and assign it to wonderwoman via indexing
# wonderwoman = my_super_list[0][1]
# print(wonderwoman)

# # Create a variable and assign it to spiderman via indexing
# spiderman = my_super_list[1][0]
# print(spiderman)

# # Create a variable and assign it to aquaman via indexing
# aquaman = my_super_list[2][0]
# print(aquaman)


'''
How do you access each element in this list by index?
my_list = ["hello", 1, ["dog", 3], "cat", [True, ["frog", 5]]]
For example, "hello" is my_list[0]. How do you access all the other elements?

'''

my_list = ["hello", 1, ["dog", 3], "cat",[True, ["frog", 5]]]

# Access each list item in the print statements below

# print(my_list[0]) # hello

# print(my_list[1])  # 1
# print(my_list[2][0])  # dog
# print(my_list[2][1])  # 3
# print(my_list[3])  # cat
# print(my_list[4][0])  # True
# print(my_list[4][1][0])  # frog
# print(my_list[4][1][1])  # 5

# Use cases -  animation, 3d modeling, complex math

''' 2D Lists'''

'''
Exercise
Write a 2D list that is a 3x3 grid of numbers.
Write some code that prints out that grid nicely with proper formatting.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 2 3
4 5 6
7 8 9
'''

# lis = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# for rows in lis: # looping through our rows
#     for columns in rows:
#         print(columns, end= ' ')
#     print() # get our returns for formatting


    

'''
Write some code that goes through a 2D list and prints the columns.
Example:
lis = [[1,2,3],[4,5,6],[7,8,9]]
1 4 7
2 5 8
3 6 9
Hint: First create a new 2D list with swapped rows and columns. (You will need 2 nested for loops.) Then it's the same as the last problem.
'''

lis = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

# final_list =[] # this will hold our swapped columns

# for i in range(len(lis[0])): # this will get the length of our 2d lists, set stop parameter
#     temp_list = [] # this list will place our column items
#     for item in lis:
#         # appending list values and indexes
#         temp_list.append(item[i])
#     final_list.append(temp_list) # rows and columns have swapped

# for row in final_list:
#     for columns in row:
#         print(columns, end=' ')
#     print()




'''
You are given a 2D list representing a table of data with rows and columns. Write a Python program to calculate the sum and average of each column in the table.
For example, if this is your list:
data = [[45,56,89],[67,34,78],[23,67,34]]
This would be your output:
Column 1: Sum = 135, Average = 45.0
Column 2: Sum = 157, Average = 52.33
Column 3: Sum = 201, Average = 67.0
Hint: Make a list to store the sums, and a list to store the averages.

'''

# List Comprehension

# For Loop

# vegetables = ['broccoli', 'kale', 'onion', 'garlic', 'kale']
# short_vegetables = []

# for v in vegetables:
#     if len(v) < 6:
#         short_vegetables.append(v)
# print(short_vegetables)


# List comprehension

vegetables = ['broccoli', 'kale', 'onion', 'garlic', 'kale']

# new_list = [x for x in original_list if condition]
short_vegetables = [v for v in vegetables if len(v) < 6]

# print(short_vegetables)


# Using a for loop, create a new list that contains any students without the letter j

# For Loop
students = ['samuel', 'tanja', 'majestic', 'judith', 'julie']

# students_without_letter_j = []

# for s in students:
#     if 'j' not in s:
#         students_without_letter_j.append(s)
# print(students_without_letter_j)


# Using list comprehension, create a new list that contains any students without the letter j
# List Comprehension - new_list = [x for x in original_list if condition]
# students = ['samuel', 'majestic', 'judith', 'julie']




# List Comprehension - new_list = [expression for x in original_list]
# original_list = [1, 2, 3, 4, 5, 6]
# new_list = []
# for o in original_list:
#     new_list.append(o + 1)
# print(new_list)
    

    

# Using list comprehension, create new list with 1 added to each number (no append needed)
# new_list = [o + 1 for o in original_list]
# print(new_list)



'''
# Exercise
# You are given a list of integers. Write a Python program to create a new list that only includes the even numbers from the original list.
# You can do this in one line with a list comprehension.
# Example:
# original_list = [34, 57, 81, 92, 2, 13]
# new_list = [34, 92, 2]
'''

# For loop
original_list = [34, 57, 81, 92, 2, 13]
# new_list = []
# for o in original_list:
#     if o % 2 == 0:
#         new_list.append(o)
# print(new_list)

# List comprehension
# new_list = [x for x in original_list if x % 2 == 0]
# print(new_list)

        

'''
# Exercise

# You work for a sales company and must generate a list of all customers who get a certain discount. The criteria for getting a discount is that they're over 60 years old and have made at least 5 purchases.
# You have a list of customers over 60, and a list of customers who have made at least 5 purchases. Use a list comprehension to output a list of customers that fit both criteria for the discount. You can do this in one line of code.
# Example:
# over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
# over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']
# Output: ['Dominic', 'Simone']

'''

over_60_years = ['Dominic', 'Linda', 'Simone', 'Swathi', 'Olaf']
over_5_purchases = ['Finn', 'Simone', 'Aaron', 'Dominic']

# customer_discount = []

# for c in over_60_years:
#     if c in over_5_purchases:
#         customer_discount.append(c)
# print(customer_discount)

customer_discount = [i for i in over_60_years if i in over_5_purchases]
print(customer_discount)























