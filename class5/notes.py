# Box around a string

# Get the user input
# user_input = input('What is your word?')

# top_or_bottom = ((len(user_input) * '*') + '**')


# # Output
# print(top_or_bottom)
# print('*' )


# Strings are immutable

# apply method
# first_name = 'JEAN'
# first_name = first_name.lower()

# print(first_name)

# my_string = 'hello'

# my_string.upper()
# print(my_string)

# my_string = my_string.upper()
# print(my_string)

# INDEXING
# animal = 'kangaroo'

# print(animal[4])

# last_letter = animal[len(animal) - 1] # remember me, last letter of a string
# print(last_letter)

# mystr = 'hello'
# print(mystr[-1])
# print[mystr[-4]]

# greeting = 'Hello World'
# print(greeting[-1])
# print(greeting[-2])
# print(greeting[-3])
# print(greeting[-4])
# print(greeting[-5])

# SLICLING [start:stop:step]
# my_fav_food = 'cheeseburger'
# # first six letters
# first_six_letters = my_fav_food[0:6:2]
# print(first_six_letters)

# my_fav_day = 'anthony'
# new_world = my_fav_day[0:4:2]
# print(new_world)

# last_name = 'Prasertsinh'
# result = last_name[0:2]
# print(result)

# mystr = 'hello'
# print(mystr[::-1])

# my_fav_music = 'classical'
# backwards = my_fav_music[::-1]
# print(backwards)

# print(my_fav_music[1::-1])
# print(my_fav_music[2::-1])
# print(my_fav_music[3::-1])
# print(my_fav_music[4::-1])
# print(my_fav_music[5::-1])


# printing the second half of the string

# mystr = 'python'
# print(mystr[3:6])

# Exercise Print the second half of a string

# Get my string from user
# second_half = input('What is your word? ')

# # find the middle of my string
# start_val = int(len(second_half) / 2)


# # find the end of my string
# stop_val = len(second_half)


# # output to user
# print(second_half[start_val:stop_val])

# def second_half(word):
#     start_val = int((len(word) / 2))
#     stop_val = len(word)
#     print(word[start_val:stop_val])

# 1 - Get Input from the user
user_email = input('What is your email? ') # this gets our email address

# 2 - Sanitize with .strip()
user_email = user_email.strip()
# user_email = 'jrjuste@gmail.com'

# 3 - Test 1 - '.' before top leave domain (com, org, edu)
test_1 = (user_email[-4] == '.')
print("Test 1: Check for '.' before top level domain:",test_1)

# 4 - Test 2 - One '@' symbol at the fifth to last index or earlier 
test_2 = ('@' in user_email[0:-5])
print("Test 2: Check for one '@' symbol before your '.' and top level domain:",test_2)


# 5 - Test 3 - At least 1 character before the '@' symbol (email can't start with '@')
stop_value = user_email.index('@') # index position of my @ symbol
test_3 = (len(user_email[0:stop_value]) >=1)
print("Test 3: At least 1 character before the @ symbol", test_3)

# 6 - Test 4 - No spaces within the string itself
test_4 = user_email.count(' ') == 0
print("Test 4: Check for white space within the email address:", test_4)



# 7 - Confirm with boolean statements that all test either passed or failed 
final_result = (test_1 and test_2 and test_3 and test_4)
print("Does your email address pass all testing:",final_result)



























