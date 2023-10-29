import math
'''

'What tasks should I be able to complete comfortably?'

 

1. Use built in print function to display strings

2. create snake-cased descriptive variable names

3. Use arithmetic operators

4. calculate based on an equation that utilizes pemdas

5. Identify datatypes (bool, Int, Float, Strings) with type function

6. Shortcut operators

7. Boolean operators

8. Strings

9. User Input & misc

10. Conditionals

11. For and while loops

'''

 

'''

1. Use built in print function to display strings

'''

 

# # Print Hello World
# print("Hello World")
 

# # Print What a wonderful day
# print("What a wonderful day")
 

# # Print Today is Wednesday
# print("Today is Wednesday")
 

# # Print Onward and upward
# print("Onward and upward")
 

# # Print This year really flew by
# print("This year really flew by")
 

'''

2. create snake-cased descriptive variable names, than print

'''

 

# # car color equal to blue
# car_color = "blue"
# print(car_color)

 

# # favorite ice cream equal to strawberry
# fav_ice_cream = "starwberry"
# print(fav_ice_cream)
 

# # first name equal to your first name
# first_name = "Anthony"
# print(first_name)
 

# # system password equal to nevada12
# sys_pass = "nevada12"
# print(sys_pass)

# # favorite food equal to pizza
# fav_food = "pizza"
# print(fav_food)
 

'''

3. Use arithmetic operators (PEMDAS) What does PEMDAS stand for? Parenthesis, exponents,

multiply, divide, add subtract.

'''

 

# In a variable called 'result' solve (2 + 5) * 6, than print.
# result = (2 + 5) * 6
# print(result)

# In the variable called 'answer' solve 5 + 4 * 3, than print
# answer = 5 + 4 * 3
# print(answer)

# in a variable called birth year, assign your year of birth. In a variable called current year,
# birth_year = 1992
# current_year = 2023


# assign the current year.  create a variable for 'age  in a decade'  which subtracts your birth
# age_in_a_decade = (current_year - birth_year)  + 10


# year from the current year, and adds ten, print the result
# print(age_in_a_decade)

 

'''

4. calculate based on an equation that utilizes pemdas, utlize f strings to display good output

for the user

 

'''

 

# Circumference of a circle,  C=2πr, lets import the math module and try something new,



# math.pi for pi, solve for radius being 3, than print

# radius = 3
# circumference_of_a_circle = 2 * math.pi * radius
# print(f'The circumference of the circle with a radius of {radius} is {circumference_of_a_circle: .2f}')
 

# average of 3 test scores (95, 82, 90), the old-fashioned way so we can manually utilize PEMDAS



# use variables for every value, than print

 
# test_1 = 95
# test_2 = 82
# test_3 = 90

# test_average = (test_1 + test_2 + test_3) / 3
# print(f'Congratulations the average of your test scores are {test_average}')

'''

5. Identify datatypes (bool, Int, Float, Strings) - type function

'''

 

# dog_name = 'fido'
# print(type(dog_name))
 

# age = 27
# print(type(age))
 

# weather_is_hot = True
# print(type(weather_is_hot))
 

# average_weight = 165.23
# print(type(average_weight))
 

# last_name = 'jenkins'
# print(type(last_name))
 

# phrase_of_the_week = 'I love coding!'
# print(type(phrase_of_the_week))
 

# is_logged_in = False
# print(type(is_logged_in))
 

# temp_f = 74
# print(type(temp_f))
 

# scores = [75, 45, 23, 99]
# print(type(scores))
 

# my_vals = {'heart', 12, 'mazda', 'springtime'}
# print(type(my_vals))
 

# my_dog = {


#     "size":"small",

#     "appetite": "big"

# }

# print(type(my_dog))

'''

6. Shortcut operators

'''

 

# num_one is assigned value of 6, using shortcut operator, subtract 3
# num_one = 6
# num_one -= 3 # subtracting 3
# num_one = num_one - 3
# print(num_one)
 

# num_two is assigned value of 10, using shortcut operator, add 2
# num_two = 10
# num_two += 2
# print(num_two)
 

# num_three is assigned value of 12, using shortcut operator, divide by 2.5
# num_three = 12
# num_three /= 2.5
# print(num_three)
 

# num_four is assigned value of 3, using shortcut operator, add 12
# num_four = 3
# num_four += 12
# print(num_four)

# num_five is assigned value of 8, using shortcut operator, multiply 2
# num_five = 8
# num_five *= 2
# print(num_five)
 

'''

7. Boolean operators - Print results

'''

 

# Is 5 is less than 7?
# result = 5 < 7
# print(f'Is 5 less than 7? {result}')
 

# Is 16 divided by 2 equal to 8?
# result = (16 / 2) == 8
# print(f'Is 16 divided 2 equal to 8? {result}')
 

# Is 12 greater than 19?
# result = 12 > 19
# print(f'Is 12 greater than 19? {result}')
 

# Variable ice_cream_tasty is set to True. Apply 'not' and print the new result
# ice_cream_tasty = True
# print(not ice_cream_tasty)
 

# Set the variable food to spaghetti. Using the boolean operator 'in', is there a letter g in



# spaghetti? Is there a letter z in spaghetti?
# food = "spaghetti"
# print('z' in food) 
# print('g' in food)

# Is the string dog not equal to cat?
# print('dog' == 'cat')
 
# pet_one = 'cat'
# pet_two = 'dog'

# print(pet_one == pet_two)


'''

8. Strings

'''

# assign your first name to a variable, assign your last name to a variable, concatenate them to



# a new variable called full_name, include an additional string for the space in between
# firstname = 'Anthony'
# lastname = 'Prasertsinh'
# fullname = firstname + ' ' + lastname
# print(fullname)


# Store the string 'Saturday' in a variable called, 'day'. Multiply it so that appears 4 times in

# day = "Yay today is Saturday "
# fav_day = day * 4
# print(fav_day)


# a new variable

 

# store the length of the string 'peanut butter" in variable my_food
# food = 'peanut butter'

# my_food_length = len('peanut butter')

# print(f'The length of my {food} is {my_food_length}')
 

# store the length of the string 'coffee' in variable my_drink
# drink = 'coffee'

# my_drink_length = len('coffee')

# print(f'The length of my {drink} is {my_drink_length}')
 

# apply capitalize to 'hello', reassign to new variable
# greeting = 'hello'

# greeting = greeting.capitalize()

# print(greeting)
 

# apply upper to 'chair', reassign to new variable
# furniture = 'chair'
# furniture = furniture.upper()
# print(furniture)
 

# Use isupper to test 'AMAZING'
# word = 'AMAZING' # our variable
# result = word.isupper() # testing to see if this is uppercase
# print(result)
 
# day = 'wednesday'

# result = day.find('d')
# print(result)


# Use istitle to test 'welcome to earth"
# greeting = 'Welcome To Earth'

# result = greeting.istitle()
# print(result)
 

# apply count to the letter b on the string baseball
# sport = 'baseball'
# result = sport.count('b')
# print(result)
 

# apply find to the letter g to grapes
# fruit = 'grapes'
# result = fruit.find('p')
# print(result)

 

# apply index to the letter y to crayon
# toy = 'crayon'
# result = toy.index('y')
# print(result)

'''

9. User Input & misc

'''

# Ask user for their age, cast to a int, check the type
# age = int(input('What is your age? '))
# print(type(age)) # What is the type from this input?

 

# Ask user for first name, Ask user for last name, output "Your name is  " and include the




# concatenated output in a formatted string
# first_name = input('What is your first name? ')
# last_name = input('What is your last name? ')
 

# print(f'Hello, your name is {first_name} {last_name}')

# ask the user for 2 numbers, multiply the two numbers and show the user output in formatted string

# num_one = int(input ('What is your first number? '))
# num_two = int(input('What is your second number? '))
 
# product = num_one * num_two

# print(f'The product of {num_one} and {num_two} is {product}')


# Pull the first 4 characters from the string burger, assign to a variable food

# food = 'burger'
# food = food[0:4]
# print(food)


 

# Pull the last 3 characters from the string couch, assign to variable furniture

# [start:stop]

# furniture = 'laptop'
# stop = len(furniture) # always go to the end of my string
# start = stop - 3 # always go to 3 characters is less than the end 

# result = furniture[start:stop]
# print(result)


 

# Assign the string "Apple Pie" to variable dessert. Create and print a new string that captures




# every other letter in the string dessert

# dessert = 'Apple pie'
# dessert = dessert[0:len(dessert):2]
# print(dessert)

 

# Reverse the string dodgeball and assign it to variable game
# game = 'dodgeball'
# game = game[::-1]
# print(game)
 

# print the values 1 through 5 and separate each number with an asterisk, using sep parameter
# print(1,2,3,4,5, sep="*")
 

# Two print statements, "Lets" and "Party", use the end parameter to create a space between the

# two. Test the newline and tab escape characters with these print statements

# print("lets", end="\t")
# print("Party")


 

'''

Conditionals

'''

 

# If the variable myname is equal to the string version of your first name, let's print,

# and tell ourselves hello with a formatted string

# my_name = 'Anthony'

# if my_name == 'Anthony':
#     print(f'Hello {my_name}')


 

# if our current year is an odd number, let's print in a formatted string that the current year

# is an odd number

# current_year = 2023

# if (current_year % 2) == 1:
#     print(f'{current_year} is an odd year')
# else:
#     print(f'{current_year} is an even year')



# lets set a variable good_weather to false. If this is false, lets print grab an umbrella. In

# the else let's say, no jacket needed. Change variable to true and lets see the new result

# good_weather = True

# if good_weather == False:
#     print("lets grab an umbrella")
# else:
#     print("No jacket needed")




 

# lets set a variable gas tank to 30. If gas tank is less than or equal to 30 let's print "Get

# Gas" otherwise we will print,no gas needed

# gas_tank = 50

# if gas_tank <= 30:
#     print("get gas")
# else:
#     print("no gas needed")





'''

10. For & While Loops

'''

 

# Lets write a while loop, using a counter that will print Happy Halloween 5 times

# counter = 0 # initialization

# while counter <= 100: # condition
#     print("Happy Halloween", counter)
#     counter += 1 # update / increment / decrement



# Lets write a while loop that will count from 1 to 10
# counter = 1

# while counter <= 10:
#     print("Happy Halloween", counter)
#     counter += 1

# i = 0 # initializing

# while i <= 100: # condition
#     print(i)
#     i += 5 # increment
 




# Lets write a loop that will take user input, and keep prompting for the input until the user adds that input

day_of_the_week = input("What day is it today? ")

while day_of_the_week == '': # while day of the week is equal to nothing
    print("You have to tell me the day") # you have to tell me something 
    day_of_the_week = input("What day is it today? ") # ask them again

print(f'Happy {day_of_the_week}')
    






























